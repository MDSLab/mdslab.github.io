import sys
from docxlib import *
from testi import IT, EN

C, R, L = "center", "right", "left"
G, K, E = "Guida", "Codice", "Esempio"

def frontespizio(t):
    """Titolo circa a meta` pagina, relatore e candidato verso il fondo sulle
    stesse righe, anno accademico ancorato al margine inferiore. Il correlatore
    compare solo dove la domanda di tesi lo prevede, cioe` nella magistrale."""
    righe = [(run(t["relatore"]), run(t["tesi_di"])),
             (run(t["prof"], bold=True), run(t["candidato"], bold=True),
              1270 if t.get("correlatore") else 60)]
    if t.get("correlatore"):
        righe += [(run(t["correlatore"]), run("")),
                  (run(t["prof2"], bold=True), run(""))]
    return [image("rId10", 3.2, 3.2),
            para(run(t["ateneo"], bold=True, size=17.2), align=C, space_after=80),
            para(run(t["dipartimento"], size=14.35), align=C, space_after=140),
            para(run(t["corso"], bold=True, size=14.35), align=C, space_after=60, border_bottom=True),
            para("", space_after=3400),
            # Con il correlatore ci sono tre righe in piu`: lo spazio sotto il
            # titolo si accorcia di conseguenza, altrimenti la pagina sfora.
            para(run(t["titolo"], bold=True, size=20.65), align=C,
                 space_after=930 if t.get("correlatore") else 2820),
            tabella_invisibile(righe),
            ancorato_in_fondo(run(t["anno"], bold=True))]


def voci(t):
    """(livello, testo della voce, token da cercare nel PDF) in ordine."""
    c, s = t["cap"], t["sez"]
    sot, sos = t["sottosez"], t["sottosottosez"]
    cp = t["parola_capitolo"]
    v = [(1, t["abstract"], t["g_abstract"][:40]),
         (1, f"{cp} 1 {c[0]}", f"{cp} 1"),
         (2, f"1.1 {s[0]}", s[0]), (2, f"1.2 {s[1]}", s[1]), (2, f"1.3 {s[2]}", s[2]),
         (1, f"{cp} 2 {c[1]}", f"{cp} 2"),
         (2, f"2.1 {s[3]}", s[3]), (3, f"2.1.1 {sot}", sot), (4, f"2.1.1.1 {sos}", sos),
         (2, f"2.2 {s[4]}", s[4]), (3, f"2.2.1 {sot}", sot), (4, f"2.2.1.1 {sos}", sos),
         (1, f"{cp} 3 {c[2]}", f"{cp} 3"),
         (2, f"3.1 {s[5]}", s[5]), (2, f"3.2 {s[6]}", s[6]), (2, f"3.3 {s[7]}", s[7]),
         (1, f"{cp} 4 {c[3]}", f"{cp} 4"),
         (1, t["bibliografia"], t["bibliografia"]),
         (1, f'{t["appendice"]} A {t["titolo_appendice"]}', f'{t["appendice"]} A')]
    f = [(2, f'{t["fig"]} 1{t["cap_fig"]}', t["cap_fig"].lstrip(": ")),
         (2, f'{t["fig"]} 2{t["cap_graf"]}', t["cap_graf"].lstrip(": "))]
    tb = [(2, f'{t["tab"]} 1{t["cap_tab"]}', t["cap_tab"].lstrip(": "))]
    return v, f, tb


def pagine_dal_pdf(pdf, token, prima_numerata):
    """Pagina stampata in cui compare ciascun token, scorrendo in avanti.

    Lo scarto fra pagina del PDF e pagina stampata non e` fisso: davanti
    all'indice ci sono il frontespizio e la dedica, che non portano numero e
    non si contano. Lo si ricava cercando l'indice stesso, che e` la pagina 1.
    """
    import subprocess
    n = int(subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
            .stdout.split("Pages:")[1].split()[0])
    import re
    spazi = lambda x: re.sub(r"\s+", " ", x)
    testo = [spazi(subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"],
                                  capture_output=True, text=True).stdout) for p in range(1, n + 1)]
    token = [spazi(x) for x in token]
    scarto = next(i for i, t in enumerate(testo) if spazi(prima_numerata) in t)
    fuori = []
    p, pos = 0, 0
    for tk in token:
        while p < len(testo):
            i = testo[p].find(tk, pos)
            if i >= 0:
                fuori.append(p - scarto + 1)
                pos = i + len(tk)
                break
            p += 1
            pos = 0
        else:
            raise SystemExit("token non trovato nel PDF: " + tk)
    return fuori


def corpo(t, pag_toc, pag_fig, pag_tab):
    b = frontespizio(t)
    b.append(page_break())
    b.append(para(run(t["g_dedica"], italic=True), style=G))
    b.append(fine_frontespizio())

    b.append(para(run(t["indice"], bold=True, size=25), align=L, space_before=1734, space_after=800, line=240))
    b.append(para(run(t["g_indice"], italic=True), style=G))
    b.append(field('TOC \\o "1-4" \\h \\z \\u',
                   [(l, s, p) for (l, s, _), p in zip(voci(t)[0], pag_toc)]))
    b.append(page_break())
    b.append(para(run(t["elenco_fig"], bold=True, size=25), align=L, space_before=1734, space_after=800, line=240))
    b.append(field('TOC \\h \\z \\c "%s"' % t["fig"],
                   [(l, s, p) for (l, s, _), p in zip(voci(t)[1], pag_fig)]))
    b.append(page_break())
    b.append(para(run(t["elenco_tab"], bold=True, size=25), align=L, space_before=1734, space_after=800, line=240))
    b.append(field('TOC \\h \\z \\c "%s"' % t["tab"],
                   [(l, s, p) for (l, s, _), p in zip(voci(t)[2], pag_tab)]))

    b.append(para(run(t["abstract"]), style="TitoloNonNumerato", align=L,
                 space_before=1734, space_after=800, line=240))
    b.append(para(run(t["g_ai"], italic=True), style=G))
    b.append(para(run(t["g_grigi"], italic=True), style=G))
    b.append(para(run(t["g_abstract"], italic=True), style=G))

    # Capitolo 1
    b.append(titolo_capitolo(t["cap"][0], t["sugg_cap"][0]))
    b.append(para(run(t["g_apertura"], italic=True), style=G))
    b.append(para(run(t["e_intro"]), style=E))
    b.append(para(run(t["sez"][0]), style="Heading2"))
    b.append(para(run(t["g_contesto"], italic=True), style=G))
    b.append(para(run(t["sez"][1]), style="Heading2"))
    b.append(para(run(t["g_obiettivo"], italic=True), style=G))
    b.append(para(run(t["sez"][2]), style="Heading2"))
    b.append(para(run(t["g_struttura"], italic=True), style=G))

    # Capitolo 2: la gerarchia completa compare qui, una volta sola
    b.append(titolo_capitolo(t["cap"][1], t["sugg_cap"][1]))
    b.append(para(run(t["g_back1"], italic=True), style=G))
    b.append(para(run(t["e_back"]), style=E))
    b.append(para(run(t["g_organizzazione"], italic=True), style=G))
    b.append(para(run(t["sez"][3]), style="Heading2"))
    b.append(para(run(t["g_sez"], italic=True), style=G))
    b.append(para(run(t["e_sez"]), style=E))
    b.append(para(run(t["g_cite"], italic=True), style=G))
    b.append(para(run(t["e_cite"]), style=E))
    b.append(para(run(t["sottosez"]), style="Heading3"))
    b.append(para(run(t["g_sottosez"], italic=True), style=G))
    b.append(para(run(t["sottosottosez"]), style="Heading4"))
    b.append(para(run(t["g_sottosottosez"], italic=True), style=G))
    b.append(para(run(t["sez"][4]), style="Heading2"))
    b.append(para(run(t["sottosez"]), style="Heading3"))
    b.append(para(run(t["sottosottosez"]), style="Heading4"))

    # Capitolo 3
    b.append(titolo_capitolo(t["cap"][2], t["sugg_cap"][2]))
    b.append(para(run(t["g_lav1"], italic=True), style=G))
    b.append(para(run(t["e_lav"]), style=E))
    b.append(para(run(t["g_organizzazione"], italic=True), style=G))
    b.append(para(run(t["sez"][5]), style="Heading2"))
    b.append(para(run(t["g_lav3"], italic=True), style=G))
    b.append(para(run(t["g_fig"], italic=True), style=G))
    b.append(para(run(t["e_fig"]), style=E))
    b.append(image("rId10", 4.0, 4.0))
    b.append(para(run(t["fig"] + " ") + seq(t["fig"]) + run(t["cap_fig"]), style="Caption"))
    b.append(para(run(t["sez"][6]), style="Heading2"))
    b.append(para(run(t["g_lav2"], italic=True), style=G))
    b.append(para(run(t["g_lst"], italic=True), style=G))
    b.append(para(run(t["e_lst"]), style=E))
    for n, riga in enumerate(["int somma(int a, int b) {", "    return a + b;", "}"], 1):
        b.append(para(numero_riga(n) + run(riga), style=K, space_after=0))
    b.append(para(run(t["lst"] + " ") + seq(t["lst"]) + run(t["cap_lst"]), style="Caption"))
    b.append(para(run(t["sez"][7]), style="Heading2"))
    b.append(para(run(t["g_misure"], italic=True), style=G))
    b.append(para(run(t["g_ic"], italic=True), style=G))
    b.append(para(run(t["g_tab"], italic=True), style=G))
    b.append(para(run(t["e_tab"]), style=E))
    b.append(para(run(t["tab"] + " ") + seq(t["tab"]) + run(t["cap_tab"]), style="Caption", keep_next=True))
    b.append(tabella(t["tabella"], [3200, 2600, 2700]))
    b.append(para(run(t["g_graf"], italic=True), style=G))
    b.append(para(run(t["e_graf"]), style=E))
    b.append(image("rId11", 11.0, 6.82, name="grafico"))
    b.append(para(run(t["fig"] + " ") + seq(t["fig"]) + run(t["cap_graf"]), style="Caption"))

    # Capitolo 4
    b.append(titolo_capitolo(t["cap"][3], t["sugg_cap"][3]))
    b.append(para(run(t["g_apertura_ultimo"], italic=True), style=G))
    b.append(para(run(t["e_concl"]), style=E))
    b.append(para(run(t["g_concl"], italic=True), style=G))

    b.append(para(run(t["bibliografia"]), style="TitoloNonNumerato", align=L,
                 space_before=1734, space_after=800, line=240))
    b.append(para(run(t["g_bib"], italic=True), style=G))
    for r in t["bib"]:
        b.append(para(run(r), align=L))

    b.append(titolo_appendice(t["titolo_appendice"]))
    b.append(para(run(t["g_app1"], italic=True), style=G))
    b.append(para(run(t["g_app2"], italic=True), style=G))
    b.append(para(run(t["g_app3"], italic=True), style=G))
    b.append(para(run(t["e_app"]), style=E))
    b.append(para(run(t["g_app4"], italic=True), style=G))
    return b

import subprocess

for t, nome in ((IT, "triennale"), (EN, "magistrale")):
    write_docx(t["nome_frontespizio"] + ".docx", "".join(frontespizio(t)), immagini=("logo-unime.png",),
               parola_capitolo=t["parola_capitolo"], parola_appendice=t["appendice"])
    v, f, tb = voci(t)
    pag = ([0] * len(v), [0] * len(f), [0] * len(tb))
    for passata in range(4):
        nome_file = t["nome_modello"] + ".docx"
        write_docx(nome_file, "".join(corpo(t, *pag)), immagini=("logo-unime.png", f"grafico-{t['lingua']}.png"),
                   parola_capitolo=t["parola_capitolo"], parola_appendice=t["appendice"],
                   numeri_di_pagina=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", nome_file],
                       capture_output=True)
        pdf = nome_file.replace(".docx", ".pdf")
        dopo = t["g_abstract"][:40]      # gli elenchi in testa non devono trarre in inganno
        nuovo = (pagine_dal_pdf(pdf, [x[2] for x in v], t["indice"]),
                 pagine_dal_pdf(pdf, [dopo] + [x[2] for x in f], t["indice"])[1:],
                 pagine_dal_pdf(pdf, [dopo] + [x[2] for x in tb], t["indice"])[1:])
        if nuovo == pag:
            print(f"{nome}: indice stabile dopo {passata} passate")
            break
        pag = nuovo
    else:
        raise SystemExit(f"{nome}: la numerazione dell'indice non si stabilizza")
print("quattro .docx scritti")
