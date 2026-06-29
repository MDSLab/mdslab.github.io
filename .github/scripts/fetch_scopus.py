import requests
import os
import sys

API_KEY = os.environ.get("SCOPUS_API_KEY", "")
if not API_KEY:
    print("Error: SCOPUS_API_KEY environment variable not set.")
    sys.exit(1)

QUERY = "AU-ID(34868328300) OR AU-ID(59757039100) OR AU-ID(60225938300) OR AU-ID(60097846900) OR ORCID(0009-0006-2908-1475)"

BIB_FILE = "_data/publications.bib"

HEADERS = {
    "X-ELS-APIKey": API_KEY,
    "Accept": "application/json",
}

def fetch_all(query):
    url = "https://api.elsevier.com/content/search/scopus"
    results = []
    start = 0
    count = 25
    while True:
        params = {
            "query": query,
            "count": count,
            "start": start,
            "field": "dc:identifier,dc:title,dc:creator,prism:publicationName,prism:coverDate,prism:doi,subtypeDescription,prism:pageRange,volume,issue,author,authname",
        }
        r = requests.get(url, headers=HEADERS, params=params)
        print(f"  Request start={start}: HTTP {r.status_code}")
        if r.status_code != 200:
            print(f"  Response: {r.text[:300]}")
            break
        data = r.json()
        entries = data.get("search-results", {}).get("entry", [])
        if not entries or entries[0].get("error"):
            break
        results.extend(entries)
        total = int(data["search-results"].get("opensearch:totalResults", 0))
        print(f"  Got {len(entries)} entries, total={total}")
        start += len(entries)
        if start >= total:
            break
    return results

def get_authors(entry):
    """Estrae tutti gli autori dall'entry, provando i vari formati dell'API."""
    creator = entry.get("dc:creator", "Unknown")

    # 1) Campo "author" (lista di dict con surname/given-name)
    authors_raw = entry.get("author", [])
    if isinstance(authors_raw, list) and authors_raw:
        names = []
        for a in authors_raw:
            if isinstance(a, dict):
                surname = a.get("surname", "")
                given = a.get("given-name", "") or a.get("initials", "")
                if surname:
                    names.append(f"{surname}, {given}".strip().rstrip(","))
                elif a.get("authname"):
                    names.append(a.get("authname"))
        if names:
            return " and ".join(names)

    # 2) Campo "authname" (puo' essere lista di dict {"$": "Nome"} o lista di stringhe)
    authnames = entry.get("authname", [])
    if isinstance(authnames, list) and authnames:
        names = []
        for a in authnames:
            if isinstance(a, dict):
                val = a.get("$", "")
                if val:
                    names.append(val)
            elif isinstance(a, str):
                names.append(a)
        if names:
            return " and ".join(names)
    elif isinstance(authnames, dict):
        val = authnames.get("$", "")
        if val:
            return val

    # 3) Fallback: solo il creator
    return creator

def entry_to_bibtex(entry, seen_keys):
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

    author_str = get_authors(entry)

    first_last = creator.split(",")[0].strip().replace(" ", "")
    key_base = f"{first_last}{year}"
    key = key_base
    suffix_num = 0
    while key in seen_keys:
        suffix_num += 1
        key = f"{key_base}_{chr(ord('a') + suffix_num - 1)}"
    seen_keys.add(key)

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

print("Fetching papers from Scopus...")
all_entries = fetch_all(QUERY)
print(f"\nTotal unique papers: {len(all_entries)}")

seen_keys = set()
bib_output = ""
for entry in sorted(all_entries, key=lambda e: e.get("prism:coverDate", "0000"), reverse=True):
    try:
        key, bib = entry_to_bibtex(entry, seen_keys)
        bib_output += bib + "\n"
    except Exception as ex:
        print(f"Warning: skipping entry due to error: {ex}")

with open(BIB_FILE, "w", encoding="utf-8") as f:
    f.write(bib_output)

print(f"Written {len(seen_keys)} entries to {BIB_FILE}")
