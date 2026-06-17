import re
import sys
from collections import defaultdict

BIB_FILE = "_data/publications.bib"
MD_FILE = "publications.md"

HEADER = """---
layout: page
title: Publications
permalink: /publications/
---

<style>
.pub-list {
  list-style: none;
  padding: 0;
}

.pub-item {
  border-left: 4px solid #6a0dad;
  padding: 1em 1.2em;
  margin-bottom: 1.2em;
  background: #fafafa;
  border-radius: 0 8px 8px 0;
}

.pub-title {
  font-weight: bold;
  font-size: 1em;
  color: #1a1a2e;
  margin-bottom: 0.3em;
}

.pub-authors {
  font-size: 0.85em;
  color: #555;
  margin-bottom: 0.3em;
}

.pub-venue {
  font-size: 0.85em;
  color: #888;
  font-style: italic;
}

.pub-year {
  display: inline-block;
  font-size: 0.75em;
  padding: 0.15em 0.6em;
  border-radius: 20px;
  background: #ede7f6;
  color: #6a0dad;
  margin-left: 0.5em;
  font-style: normal;
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

# Leggi file
with open(BIB_FILE, "r", encoding="utf-8") as f:
    bib_text = f.read()

entries = extract_entries(bib_text)
print(f"Parsed {len(entries)} entries.")

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

        url = fields.get('url', '') or fields.get('doi', '')
        if url and url.startswith('10.'):
            url = f"https://doi.org/{url}"

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
