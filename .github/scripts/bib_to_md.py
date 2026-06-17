from pybtex.database import parse_string, PybtexError
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

# Leggi il file .bib come testo e rinomina le chiavi duplicate
with open(BIB_FILE, "r", encoding="utf-8") as f:
    bib_text = f.read()

# Rinomina chiavi duplicate aggiungendo suffisso _b, _c, ecc.
seen_keys = {}
cleaned_lines = []

for line in bib_text.splitlines():
    stripped = line.strip()
    if stripped.startswith("@") and "{" in stripped:
        key = stripped.split("{")[1].rstrip(",").strip()
        if key in seen_keys:
            seen_keys[key] += 1
            suffix = chr(ord('a') + seen_keys[key])
            new_key = f"{key}_{suffix}"
            print(f"Warning: duplicate key '{key}' renamed to '{new_key}'")
            line = line.replace("{" + key, "{" + new_key, 1)
        else:
            seen_keys[key] = 0
    cleaned_lines.append(line)

cleaned_bib = "\n".join(cleaned_lines)

try:
    bib_data = parse_string(cleaned_bib, bib_format="bibtex")
except PybtexError as e:
    print(f"Error parsing BibTeX file: {e}")
    sys.exit(1)

# Sort entries by year descending
entries = sorted(
    bib_data.entries.values(),
    key=lambda e: int(e.fields.get("year", 0)),
    reverse=True
)

# Group by year
by_year = defaultdict(list)
for entry in entries:
    year = entry.fields.get("year", "Unknown")
    by_year[year].append(entry)

md = HEADER

for year in sorted(by_year.keys(), reverse=True):
    md += f"## {year}\n\n<ul class=\"pub-list\">\n"
    for entry in by_year[year]:
        fields = entry.fields

        title = fields.get("title", "Untitled").replace("{", "").replace("}", "")

        try:
            authors = entry.persons.get("author", [])
            author_str = ", ".join(
                " ".join(filter(None, [
                    " ".join(str(n) for n in p.first_names),
                    " ".join(str(n) for n in p.last_names)
                ]))
                for p in authors
            )
        except Exception:
            author_str = fields.get("author", "")

        venue = (
            fields.get("journal") or
            fields.get("booktitle") or
            fields.get("publisher") or
            ""
        ).replace("{", "").replace("}", "")

        url = fields.get("url", "") or fields.get("doi", "")
        if url and url.startswith("10."):
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
