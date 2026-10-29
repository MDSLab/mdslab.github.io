import os
import re
import sys
from collections import defaultdict

BIB_FILE = "_data/publications.bib"
MD_FILE = "publications.md"
LINKS_FILE = "_data/publication_links.yml"

HEADER = """---
layout: page
title: Publications
permalink: /publications/
---

<style>
/* Colori, riquadri e pillole stanno in /assets/css/mdslab.css */
.pub-list {
  list-style: none;
  padding: 0;
}

.pub-item {
  margin-bottom: 1.2em;
}

.pub-title {
  font-size: 1em;
  margin-bottom: 0.3em;
}

.pub-authors {
  font-size: 0.85em;
  margin-bottom: 0.3em;
}

.pub-venue {
  font-size: 0.85em;
  font-style: italic;
}

.pub-year {
  margin-left: 0.5em;
}
</style>

"""

def extract_entries(bib_text):
    """Estrae manualmente le entry BibTeX dal testo."""
    entries = []
    # Trova ogni entry @type{key, ...}
    pattern = re.compile(r'@(\w+)\s*\{([^,]+),', re.MULTILINE)
    
    positions = [(m.start(), m.group(1), m.group(2).strip()) for m in pattern.finditer(bib_text)]
    
    seen_keys = {}
    
    for i, (start, entry_type, key) in enumerate(positions):
        # Determina la fine dell'entry (inizio della prossima)
        end = positions[i + 1][0] if i + 1 < len(positions) else len(bib_text)
        entry_text = bib_text[start:end]
        
        # Deduplica chiavi
        if key in seen_keys:
            seen_keys[key] += 1
            suffix = chr(ord('a') + seen_keys[key])
            new_key = f"{key}_{suffix}"
            print(f"Warning: duplicate key '{key}' renamed to '{new_key}'")
            key = new_key
        else:
            seen_keys[key] = 0
        
        # Estrai campi con regex
        fields = {}
        field_pattern = re.compile(r'(\w+)\s*=\s*[\{"](.+?)[\}"](?:\s*,|\s*\})', re.DOTALL)
        for fm in field_pattern.finditer(entry_text):
            fname = fm.group(1).lower()
            fval = fm.group(2).replace('\n', ' ').replace('{', '').replace('}', '').strip()
            fields[fname] = fval
        
        if fields.get('title') and fields.get('year'):
            entries.append({
                'key': key,
                'type': entry_type.lower(),
                'fields': fields
            })
        else:
            print(f"Warning: skipping entry '{key}' (missing title or year)")
    
    return entries

def normalize(title):
    """Titolo ridotto a sole lettere e cifre minuscole, così la corrispondenza
    non dipende da punteggiatura, accenti o spaziatura."""
    return re.sub(r'[^a-z0-9]', '', title.lower())

# Collegamenti inseriti a mano per le voci che Scopus restituisce senza DOI:
# tipicamente atti CEUR, che non ne assegnano. Stanno in un file separato perché
# fetch_scopus.py rigenera il .bib da zero e cancellerebbe qualsiasi aggiunta.
manual_links = {}
excluded = set()
if os.path.exists(LINKS_FILE):
    with open(LINKS_FILE, encoding="utf-8") as f:
        current = None
        for line in f:
            line = line.split('#')[0].rstrip()
            if not line.strip():
                continue
            if line.startswith('- title:'):
                current = line.split(':', 1)[1].strip().strip('"\'')
            elif line.strip().startswith('url:') and current:
                manual_links[normalize(current)] = line.split(':', 1)[1].strip().strip('"\'')
                current = None
            elif line.strip().startswith('exclude:') and current:
                excluded.add(normalize(current))
                current = None
    print(f"Loaded {len(manual_links)} manual links and {len(excluded)} exclusions from {LINKS_FILE}.")

# Leggi file

def normalizza_venue(v):
    """Ripulisce il nome della sede dalle ridondanze che arrivano da Scopus.

    Scopus toglie la punteggiatura e lascia l'anno dentro il titolo, che la
    pagina mostra comunque di fianco: ne esce "SmartComp Companion 2026 2026".

    Qui si tolgono solo le cose che non possono cambiare il nome di una sede.
    In particolare NON si tocca "Proceedings": sembra un prefisso di servizio,
    ma "Proceedings of the ACM on Measurement and Analysis of Computing
    Systems" e` il nome vero di una rivista, e toglierlo la inventerebbe.

    Restano lunghi i nomi dei congressi co-locati, dove Scopus concatena i
    titoli di tutte le conferenze: accorciarli richiede una tabella scritta a
    mano, perche` solo chi li conosce sa quale sia la sede giusta.
    """
    v = re.sub(r"\s+(19|20)\d\d$", "", v)                 # l'anno finale, gia` mostrato a fianco
    v = re.sub(r"^(Proceedings)\s+(19|20)\d\d\s+", r"\1 ", v)   # e quello subito dopo "Proceedings"
    v = re.sub(r"^Lecture Notes in Computer Science Including Subseries.*$",
               "Lecture Notes in Computer Science", v)
    # Scopus toglie il trattino da "On-Line" e ne esce "on on Line Testing":
    # qui il nome si corregge, non si accorcia.
    v = v.replace("Symposium on on Line Testing", "Symposium on On-Line Testing")
    return v.strip()


with open(BIB_FILE, "r", encoding="utf-8") as f:
    bib_text = f.read()

entries = extract_entries(bib_text)
print(f"Parsed {len(entries)} entries.")

before = len(entries)
entries = [e for e in entries if normalize(e['fields'].get('title', '')) not in excluded]
if before != len(entries):
    print(f"Excluded {before - len(entries)} entries listed in {LINKS_FILE}.")

# Ordina per anno decrescente
entries.sort(key=lambda e: int(e['fields'].get('year', 0)), reverse=True)

# Raggruppa per anno
by_year = defaultdict(list)
for entry in entries:
    year = entry['fields'].get('year', 'Unknown')
    by_year[year].append(entry)

md = HEADER

for year in sorted(by_year.keys(), reverse=True):
    md += f"## {year}\n\n<ul class=\"pub-list\">\n"
    for entry in by_year[year]:
        fields = entry['fields']

        title = fields.get('title', 'Untitled')
        authors = fields.get('author', '')
        # Formatta autori: "Last, First and Last, First" → "First Last, First Last"
        author_list = [a.strip() for a in authors.split(' and ')]
        formatted_authors = []
        for a in author_list:
            if ',' in a:
                parts = a.split(',', 1)
                formatted_authors.append(f"{parts[1].strip()} {parts[0].strip()}")
            else:
                formatted_authors.append(a)
        author_str = ', '.join(formatted_authors)

        venue = fields.get('journal') or fields.get('booktitle') or fields.get('publisher') or ''
        venue = normalizza_venue(venue)

        url = fields.get('url', '') or fields.get('doi', '')
        if url and url.startswith('10.'):
            url = f"https://doi.org/{url}"
        if not url:
            url = manual_links.get(normalize(title), '')

        title_html = f'<a href="{url}" target="_blank">{title}</a>' if url else title

        md += f"""  <li class="pub-item">
    <div class="pub-title">{title_html}</div>
    <div class="pub-authors">{author_str}</div>
    <div class="pub-venue">{venue}<span class="pub-year">{year}</span></div>
  </li>\n"""

    md += "</ul>\n\n"

with open(MD_FILE, "w", encoding="utf-8") as f:
    f.write(md)

print(f"Generated {MD_FILE} with {len(entries)} entries.")
