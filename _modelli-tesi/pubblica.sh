#!/bin/sh
# Rigenera i modelli di tesi e li copia dove il sito li offre in scaricamento.
# I nomi dei file stanno in testi.py, uno solo posto, cosi` non si sfasano.
set -e
cd "$(dirname "$0")"

python3 grafico.py it
python3 grafico.py en
cp grafico-it.png latex-triennale/grafico.png
cp grafico-en.png latex-magistrale/grafico.png

# I quattro .docx. build.py converte in PDF a ogni passata per sapere a che
# pagina cade ogni titolo e scrivere l'indice gia` compilato dentro al file.
python3 build.py

mkdir -p ../teaching/thesis
python3 -c "
import testi
for t in (testi.IT, testi.EN):
    print(t['nome_frontespizio'], t['nome_modello'], t['cartella_latex'])
" > nomi.tmp

while read FRONTESPIZIO MODELLO CARTELLA; do
  cp "$FRONTESPIZIO.docx" "$MODELLO.docx" ../teaching/thesis/
  rm -f "../teaching/thesis/$MODELLO-latex.zip"
  (cd "$CARTELLA" && zip -q "../../teaching/thesis/$MODELLO-latex.zip" \
      tesi.tex frontespizio.tex bibliografia.bib logo-unime.png grafico.png)

  # Il solo frontespizio, in parallelo al .docx: e` lo stesso frontespizio.tex
  # del modello completo, che compilato da solo si tira dietro il preambolo che
  # gli serve. Un file unico, due usi: non ci sono due frontespizi da allineare.
  rm -f "../teaching/thesis/$FRONTESPIZIO-latex.zip"
  (cd "$CARTELLA" && zip -q "../../teaching/thesis/$FRONTESPIZIO-latex.zip" \
      frontespizio.tex logo-unime.png)
done < nomi.tmp

rm -f nomi.tmp *.pdf *.docx
echo "modelli aggiornati in teaching/thesis/"
ls -1 ../teaching/thesis/
