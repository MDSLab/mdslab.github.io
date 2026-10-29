# mdslab.github.io

Sito di MDSLab (Mobile and Distributed Systems Laboratory), Università di Messina.
Jekyll con il tema So Simple 3.2.0; stile in `assets/css/mdslab.css`.

## Dove si cambiano i contenuti

| Cosa | File |
|---|---|
| Aree di ricerca (Research e pagina tesi) | `_data/areas.yml` |
| Temi di ricerca | `_data/topics.yml` |
| Direttore, membri, ex membri | `_data/director.yml`, `_data/people.yml`, `_data/alumni.yml` |
| Progetti | `_data/projects.yml` |
| Partner in home | `_data/partners.yml` |
| Corsi | `_data/teaching.yml` + `teaching/courses/*.md` |
| Etichette tradotte IT/EN | `_data/i18n.yml` |
| Icone (SVG in linea) | `_data/icons.yml` |

Le sezioni con dati vuoti non compaiono. I punti ancora da compilare sono segnati `TODO`.

## Pubblicazioni

`python .github/scripts/fetch_scopus.py` (richiede `SCOPUS_API_KEY`) rigenera
`_data/publications.bib`; al push la Action `bib_to_md.yml` rigenera `publications.md`.
I link per le voci senza DOI stanno in `_data/publication_links.yml`.

## In locale

```
bundle install
bundle exec jekyll serve
```
