import requests
import os
import sys
from collections import defaultdict

# ── Configurazione ─────────────────────────────────────────────────────────────
API_KEY = os.environ.get("SCOPUS_API_KEY", "")
if not API_KEY:
    print("Error: SCOPUS_API_KEY environment variable not set.")
    sys.exit(1)

# Author IDs e ORCID del lab
AUTHOR_IDS = [
    "34868328300",
    "59757039100",
    "60225938900",
    "60097846900",
]
ORCID_IDS = [
    "0009-0006-2908-1475",
]

BIB_FILE = "_data/publications.bib"

HEADERS = {
    "X-ELS-APIKey": API_KEY,
    "Accept": "application/json",
}

# ── Funzioni ────────────────────────────────────────────────────────────────────

def search_by_author_id(author_id):
    """Cerca tutti i paper di un autore tramite AU-ID."""
    url = "https://api.elsevier.com/content/search/scopus"
    params = {
        "query": f"AU-ID({author_id})",
        "count": 200,
        "field": "dc:identifier,dc:title,dc:creator,prism:publicationName,prism:coverDate,prism:doi,prism:issn,citedby-count,subtypeDescription,prism:pageRange,volume,issue,authkeywords,author",
        "sort": "coverDate",
    }
    results = []
    start = 0
    while True:
        params["start"] = start
        r = requests.get(url, headers=HEADERS, params=params)
        if r.status_code != 200:
            print(f"Warning: API error for AU-ID {author_id}: {r.status_code}")
            break
        data = r.json()
        entries = data.get("search-results", {}).get("entry", [])
        if not entries or entries[0].get("error"):
            break
        results.extend(entries)
        total = int(data["search-results"].get("opensearch:totalResults", 0))
        start += len(entries)
        if start >= total:
            break
    print(f"  AU-ID {author_id}: {len(results)} papers found.")
    return results

def search_by_orcid(orcid):
    """Cerca tutti i paper di un autore tramite ORCID."""
    url = "https://api.elsevier.com/content/search/scopus"
    params = {
        "query": f"ORCID({orcid})",
        "count": 200,
        "field": "dc:identifier,dc:title,dc:creator,prism:publicationName,prism:coverDate,prism:doi,prism:issn,citedby-count,subtypeDescription,prism:pageRange,volume,issue,authkeywords,author",
        "sort": "coverDate",
    }
    r = requests.get(url, headers=HEADERS, params=params)
    if r.status_code != 200:
        print(f"Warning: API error for ORCID {orcid}: {r.status_code}")
        return []
    data = r.json()
    entries = data.get("search-results", {}).get("entry", [])
    if not entries or entries[0].get("error"):
        return []
    print(f"  ORCID {orcid}: {len(entries)} papers found.")
    return entries

def entry_to_bibtex(entry, seen_keys):
    """Converte una entry JSON Scopus in formato BibTeX."""
    title = entry.get("dc:title", "Unknown Title")
    creator = entry.get("dc:creator", "Unknown")
    venue = entry.get("prism:publicationName", "")
    date = entry.get("prism:coverDate", "0000-01-01")
    year = date[:4]
    doi = entry.get("prism:doi", "")
    subtype = entry.get("subtypeDescription", "Article")
    pages = entry.get("prism:pageRange", "")
    volume = entry.get("volume", "")
    issue = entry.get("issue", "")

    # Recupera tutti gli autori
    authors_raw = entry.get("author", [])
    if authors_raw:
        author_str = " and ".join(
            f"{a.get('surname', '')}, {a.get('given-name', '')}"
            for a in authors_raw
        )
    else:
        author_str = creator

    # Genera chiave BibTeX
    first_last = creator.split(",")[0].strip().replace(" ", "")
    key_base = f"{first_last}{year}"
    key = key_base
    suffix_num = 0
    while key in seen_keys:
        suffix_num += 1
        key = f"{key_base}_{chr(ord('a') + suffix_num - 1)}"
    seen_keys.add(key)

    # Tipo BibTeX
    if "Conference" in subtype or "Proceeding" in subtype:
        bib_type = "inproceedings"
        venue_field = f"  booktitle = {{{venue}}},"
    else:
        bib_type = "article"
        venue_field = f"  journal   = {{{venue}}},"

    bib = f"@{bib_type}{{{key},\n"
    bib += f"  author    = {{{author_str}}},\n"
    bib += f"  title     = {{{title}}},\n"
    bib += venue_field + "\n"
    bib += f"  year      = {{{year}}},\n"
    if volume:
        bib += f"  volume    = {{{volume}}},\n"
    if issue:
        bib += f"  number    = {{{issue}}},\n"
    if pages:
        bib += f"  pages     = {{{pages}}},\n"
    if doi:
        bib += f"  doi       = {{{doi}}},\n"
        bib += f"  url       = {{https://doi.org/{doi}}},\n"
    bib += "}\n"
    return key, bib

# ── Main ────────────────────────────────────────────────────────────────────────

print("Fetching papers from Scopus...")

all_entries = []
seen_scopus_ids = set()

for aid in AUTHOR_IDS:
    entries = search_by_author_id(aid)
    for e in entries:
        sid = e.get("dc:identifier", "")
        if sid and sid not in seen_scopus_ids:
            seen_scopus_ids.add(sid)
            all_entries.append(e)

for orcid in ORCID_IDS:
    entries = search_by_orcid(orcid)
    for e in entries:
        sid = e.get("dc:identifier", "")
        if sid and sid not in seen_scopus_ids:
            seen_scopus_ids.add(sid)
            all_entries.append(e)

print(f"\nTotal unique papers: {len(all_entries)}")

# Ordina per anno decrescente
all_entries.sort(
    key=lambda e: e.get("prism:coverDate", "0000-01-01"),
    reverse=True
)

# Converti in BibTeX
seen_keys = set()
bib_output = ""
for entry in all_entries:
    try:
        key, bib = entry_to_bibtex(entry, seen_keys)
        bib_output += bib + "\n"
    except Exception as ex:
        print(f"Warning: skipping entry due to error: {ex}")

# Scrivi file
with open(BIB_FILE, "w", encoding="utf-8") as f:
    f.write(bib_output)

print(f"Written {len(seen_keys)} entries to {BIB_FILE}")
