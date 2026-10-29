# Grafico di esempio per i modelli di tesi: tempo medio di risposta al crescere
# del carico, due configurazioni, con intervalli di confidenza al 95%.
# Si disegna in SVG e si converte in PNG, cosi` lo stesso file finisce sia nel
# .docx sia nel .tex e le due uscite sono identiche.
import subprocess, sys

LINGUA = sys.argv[1] if len(sys.argv) > 1 else "it"
ASSE_X, ASSE_Y, LEGENDA = {
    "it": ("Richieste al secondo", "Tempo medio di risposta (ms)", "Configurazione"),
    "en": ("Requests per second", "Mean response time (ms)", "Configuration"),
}[LINGUA]

X = [100, 200, 400, 800, 1600]
SERIE = [("A", [12.4, 13.1, 15.0, 19.8, 28.5], [0.8, 0.9, 1.1, 1.6, 2.4], "#1f4e79", "cerchio"),
         ("B", [31.7, 33.0, 36.4, 44.1, 61.2], [2.1, 2.3, 2.8, 3.9, 5.5], "#b2560d", "quadrato")]

L, R, T, B = 95, 25, 28, 68
W, H = 1000, 620
YMAX = 70
FONT = "Times New Roman, Nimbus Roman, Liberation Serif, serif"

def px(i):   return L + i * (W - L - R) / (len(X) - 1)
def py(v):   return H - B - v * (H - B - T) / YMAX

d = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     f'<rect width="{W}" height="{H}" fill="white"/>',
     f'<g font-family="{FONT}" font-size="21" fill="#000">']

# griglia e asse y
for v in range(0, YMAX + 1, 10):
    y = py(v)
    d.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#d9d9d9" stroke-width="1"/>')
    d.append(f'<text x="{L-12}" y="{y+7:.1f}" text-anchor="end">{v}</text>')
# asse x
for i, x in enumerate(X):
    d.append(f'<text x="{px(i):.1f}" y="{H-B+30}" text-anchor="middle">{x}</text>')
d.append(f'<line x1="{L}" y1="{py(0):.1f}" x2="{W-R}" y2="{py(0):.1f}" stroke="#000" stroke-width="1.4"/>')
d.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{py(0):.1f}" stroke="#000" stroke-width="1.4"/>')
# titoli degli assi
d.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-8}" text-anchor="middle">{ASSE_X}</text>')
d.append(f'<text transform="translate(26,{(T+py(0))/2:.0f}) rotate(-90)" text-anchor="middle">'
         f'{ASSE_Y}</text>')

for nome, y, ic, colore, segno in SERIE:
    punti = " ".join(f"{px(i):.1f},{py(v):.1f}" for i, v in enumerate(y))
    d.append(f'<polyline points="{punti}" fill="none" stroke="{colore}" stroke-width="2.4"/>')
    for i, (v, e) in enumerate(zip(y, ic)):
        x = px(i)
        d.append(f'<line x1="{x:.1f}" y1="{py(v-e):.1f}" x2="{x:.1f}" y2="{py(v+e):.1f}" '
                 f'stroke="{colore}" stroke-width="1.8"/>')
        for q in (v - e, v + e):
            d.append(f'<line x1="{x-7:.1f}" y1="{py(q):.1f}" x2="{x+7:.1f}" y2="{py(q):.1f}" '
                     f'stroke="{colore}" stroke-width="1.8"/>')
        if segno == "cerchio":
            d.append(f'<circle cx="{x:.1f}" cy="{py(v):.1f}" r="6" fill="{colore}"/>')
        else:
            d.append(f'<rect x="{x-5.5:.1f}" y="{py(v)-5.5:.1f}" width="11" height="11" fill="{colore}"/>')

# legenda
lx, ly = L + 28, T + 22
for k, (nome, _, _, colore, segno) in enumerate(SERIE):
    yy = ly + k * 30
    d.append(f'<line x1="{lx}" y1="{yy}" x2="{lx+38}" y2="{yy}" stroke="{colore}" stroke-width="2.4"/>')
    if segno == "cerchio":
        d.append(f'<circle cx="{lx+19}" cy="{yy}" r="6" fill="{colore}"/>')
    else:
        d.append(f'<rect x="{lx+13.5}" y="{yy-5.5}" width="11" height="11" fill="{colore}"/>')
    d.append(f'<text x="{lx+50}" y="{yy+7}">{LEGENDA} {nome}</text>')

d.append('</g></svg>')
open(f"grafico-{LINGUA}.svg", "w", encoding="utf-8").write("\n".join(d))
subprocess.run(["inkscape", f"grafico-{LINGUA}.svg", "--export-type=png",
                f"--export-filename=grafico-{LINGUA}.png", "--export-width=1300"],
               check=True, capture_output=True)
print(f"grafico-{LINGUA}.png scritto")
