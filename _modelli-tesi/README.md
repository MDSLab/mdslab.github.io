# Modelli di tesi

Sorgenti dei modelli che il sito offre in scaricamento da `teaching/thesis/`.
La cartella comincia con un trattino basso, quindi Jekyll non la pubblica.

Quattro modelli, due per la triennale in italiano e due per la magistrale in
inglese, ciascuno in versione Word e LaTeX. Le due versioni devono produrre lo
stesso PDF: stesse misure dei caratteri, stesse posizioni dei titoli, stesso
indice con gli stessi numeri di pagina.

## Rigenerare tutto

```sh
./pubblica.sh
```

Disegna il grafico, scrive i quattro `.docx`, prepara i due `.zip` per Overleaf
e copia il risultato in `../teaching/thesis/` con questi nomi:

```
tesi-triennale-frontespizio.docx      masters-thesis-title-page.docx
tesi-triennale-modello.docx           masters-thesis-template.docx
tesi-triennale-modello-latex.zip      masters-thesis-template-latex.zip
```

Radice fissa per lingua, poi che cos'è, poi il formato solo dove l'estensione
non basta. I nomi stanno in `testi.py`, non nello script.

Servono `python3`, `inkscape`, `zip` e LibreOffice (`soffice`).

## Da dove viene cosa

| file | cosa fa |
|---|---|
| `testi.py` | tutte le stringhe e i nomi dei file pubblicati, nei due dizionari `IT` e `EN`. Le due chiavi devono coincidere |
| `build.py` | monta frontespizio e corpo, e scrive i `.docx` |
| `docxlib.py` | scrive OOXML a mano: stili, numerazione, campi di Word, tabelle, immagini |
| `grafico.py` | disegna in SVG il grafico di esempio con gli intervalli di confidenza e lo converte in PNG |
| `latex-triennale/`, `latex-magistrale/` | i due progetti LaTeX, che finiscono negli `.zip` |

Il testo dei modelli Word sta in `testi.py`; quello dei modelli LaTeX sta nei
rispettivi `tesi.tex`. **Una modifica va fatta in tutti e due i posti**, salvo
dove la differenza è voluta: l'indice si aggiorna con «Aggiorna campo» in Word e
ricompilando in LaTeX, e la bibliografia si costruisce a mano in Word e con
BibTeX in LaTeX.

## Due cose che Word fa e LaTeX no

**L'indice è già compilato dentro al `.docx`.** `build.py` genera il file, lo
converte in PDF, legge a che pagina cade ogni titolo e riscrive il file con quei
numeri dentro al campo indice, ripetendo finché i numeri non si stabilizzano.
Serve perché lo studente deve vedere l'indice giusto appena apre il file, senza
premere niente. Resta un campo: `F9` lo ricostruisce.

**Le immagini hanno identificativi che partono da `rId10`.** I numeri bassi sono
già presi da stili, numerazione, impostazioni e piè di pagina. Una collisione non
dà errore: l'immagine semplicemente sparisce e resta il buco bianco. `write_docx`
controlla che ogni immagine richiamata abbia la sua relazione e si ferma se non
ce l'ha.
