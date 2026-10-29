# Costruzione di file .docx con la sola libreria standard: un .docx e` uno ZIP
# di XML. Qui ci sono gli stili (Titolo 1/2/3, Didascalia), i campi di Word per
# indice ed elenchi di figure e tabelle, e l'inserimento di un'immagine.
import zipfile, struct
from xml.sax.saxutils import escape

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
      'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
      'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"')

def run(text, bold=False, italic=False, size=None, caps=False):
    rpr = "<w:rPr>"
    if bold: rpr += "<w:b/>"
    if italic: rpr += "<w:i/>"
    if caps: rpr += "<w:caps/>"
    if size: rpr += f'<w:sz w:val="{round(size*2)}"/><w:szCs w:val="{round(size*2)}"/>'
    rpr += "</w:rPr>"
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'

def para(runs="", style=None, align=None, space_before=0, space_after=120, border_bottom=False, line=360, keep_next=False):
    ppr = "<w:pPr>"
    if style: ppr += f'<w:pStyle w:val="{style}"/>'
    if keep_next: ppr += "<w:keepNext/>"
    if border_bottom:
        ppr += '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="000000"/></w:pBdr>'
    ppr += f'<w:spacing w:before="{space_before}" w:after="{space_after}" w:line="{line}" w:lineRule="auto"/>'
    if align: ppr += f'<w:jc w:val="{align}"/>'
    ppr += "</w:pPr>"
    return f"<w:p>{ppr}{runs}</w:p>"

def field(instr, voci):
    """Campo indice di Word con dentro il risultato gia` calcolato: il documento
    mostra l'indice appena lo si apre, e F9 lo ricostruisce."""
    apre = ('<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> {escape(instr)} </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
    chiude = '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
    x = []
    for i, (livello, testo, pagina) in enumerate(voci):
        x.append(f'<w:p><w:pPr><w:pStyle w:val="TOC{livello}"/></w:pPr>'
                 + (apre if i == 0 else "")
                 + run(testo) + '<w:r><w:tab/></w:r>' + run(str(pagina))
                 + (chiude if i == len(voci) - 1 else "") + '</w:p>')
    return "".join(x)

def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

def image(rid, width_cm, height_cm, name="logo"):
    cx, cy = int(width_cm*360000), int(height_cm*360000)
    n = int(rid.replace("rId", ""))
    return (f'<w:p><w:pPr><w:keepNext/><w:jc w:val="center"/><w:spacing w:after="120"/></w:pPr><w:r><w:drawing>'
            f'<wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{n}" name="{name}"/>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic><pic:nvPicPr><pic:cNvPr id="{n}" name="{name}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            f'</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>')

STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults><w:rPrDefault><w:rPr>
    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/>
    <w:lang w:val="it-IT"/></w:rPr></w:rPrDefault></w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>
    <w:pPr><w:jc w:val="both"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:pageBreakBefore/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
      <w:outlineLvl w:val="0"/><w:spacing w:before="1000" w:after="800"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="50"/><w:szCs w:val="50"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TitoloNonNumerato"><w:name w:val="Titolo non numerato"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:pageBreakBefore/><w:outlineLvl w:val="0"/><w:spacing w:before="1000" w:after="800"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="50"/><w:szCs w:val="50"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Appendice"><w:name w:val="Appendice"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:pageBreakBefore/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="2"/></w:numPr>
      <w:outlineLvl w:val="0"/><w:spacing w:before="1734" w:after="800"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="50"/><w:szCs w:val="50"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:numPr><w:ilvl w:val="1"/><w:numId w:val="1"/></w:numPr>
      <w:outlineLvl w:val="1"/><w:spacing w:before="420" w:after="200"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="34"/><w:szCs w:val="34"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:numPr><w:ilvl w:val="2"/><w:numId w:val="1"/></w:numPr>
      <w:outlineLvl w:val="2"/><w:spacing w:before="360" w:after="180"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="29"/><w:szCs w:val="29"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading4"><w:name w:val="heading 4"/>
    <w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
    <w:pPr><w:numPr><w:ilvl w:val="3"/><w:numId w:val="1"/></w:numPr>
      <w:outlineLvl w:val="3"/><w:spacing w:before="260" w:after="140"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="8504"/></w:tabs>
      <w:spacing w:before="200" w:after="0"/><w:jc w:val="left"/></w:pPr>
    <w:rPr><w:b/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="TOC1"/>
    <w:pPr><w:ind w:left="340" w:hanging="340"/><w:spacing w:before="40" w:after="0"/></w:pPr>
    <w:rPr><w:b w:val="0"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="TOC3"><w:name w:val="toc 3"/><w:basedOn w:val="TOC2"/>
    <w:pPr><w:ind w:left="737" w:hanging="454"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="TOC4"><w:name w:val="toc 4"/><w:basedOn w:val="TOC2"/>
    <w:pPr><w:ind w:left="1247" w:hanging="567"/></w:pPr></w:style>
  <w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="caption"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:jc w:val="center"/><w:spacing w:before="120" w:after="240"/></w:pPr>
    <w:rPr><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Guida"><w:name w:val="Guida"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:after="180"/></w:pPr>
    <w:rPr><w:i/><w:color w:val="808080"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Esempio"><w:name w:val="Esempio"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:after="180"/></w:pPr>
    </w:style>
  <w:style w:type="paragraph" w:styleId="Codice"><w:name w:val="Codice"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:jc w:val="left"/><w:spacing w:after="0" w:line="240" w:lineRule="auto"/>
      <w:ind w:left="680" w:hanging="340"/><w:tabs><w:tab w:val="left" w:pos="680"/></w:tabs><w:pBdr><w:left w:val="single" w:sz="12" w:space="6" w:color="BFBFBF"/></w:pBdr></w:pPr>
    <w:rPr><w:rFonts w:ascii="Courier New" w:hAnsi="Courier New"/><w:sz w:val="22"/></w:rPr></w:style>
</w:styles>'''

def write_docx(path, body, immagini=(), parola_capitolo="Capitolo",
               parola_appendice="Appendice", numeri_di_pagina=False):
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>'
            '<Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>'
            + ('<Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>' if numeri_di_pagina else '')
            + "".join('<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/img%d.png"/>' % (10 + k, k) for k in range(len(immagini)))
            + '</Relationships>')
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Default Extension="png" ContentType="image/png"/>'
          '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
          '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
          '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
          '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
          + ('<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>' if numeri_di_pagina else '')
          + '</Types>')
    root_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
                 '</Relationships>')
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           f'<w:document {NS}><w:body>{body}'
           '<w:sectPr>'
           + ('<w:footerReference w:type="default" r:id="rId5"/>' if numeri_di_pagina else '')
           + PAGINA
           + ('<w:pgNumType w:start="1"/>' if numeri_di_pagina else '')
           + '</w:sectPr></w:body></w:document>')
    import re
    usati = set(re.findall(r'r:embed="(rId\d+)"', doc))
    dichiarati = set(re.findall(r'Id="(rId\d+)"[^>]*relationships/image', rels))
    if usati - dichiarati:
        raise SystemExit("%s: immagine senza relazione: %s" % (path, sorted(usati - dichiarati)))
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.writestr("_rels/.rels", root_rels)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING_TMPL.replace("{CAP}", parola_capitolo).replace("{APP}", parola_appendice))
        z.writestr("word/settings.xml", SETTINGS)
        if numeri_di_pagina:
            z.writestr("word/footer1.xml", FOOTER)
        z.writestr("word/_rels/document.xml.rels", rels)
        for k, sorgente in enumerate(immagini):
            z.write(sorgente, "word/media/img%d.png" % k)

def campo(instr, segnaposto):
    return ('<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r><w:instrText xml:space="preserve"> {instr} </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r><w:t>{segnaposto}</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>')

def seq(nome):
    """Numero di figura, tabella o snippet: contatore continuo su tutta la tesi."""
    return campo("SEQ %s \\* ARABIC" % nome, "1")


FOOTER = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          f'<w:ftr {NS}><w:p><w:pPr><w:jc w:val="center"/>'
          '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
          '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
          '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
          '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
          '<w:r><w:t>1</w:t></w:r>'
          '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')

PAGINA = ('<w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="1701" w:right="1701" w:bottom="1701" w:left="1701"'
          ' w:header="709" w:footer="1000"/>')

def fine_frontespizio():
    """Interruzione di sezione: il frontespizio resta senza numero di pagina e
    la numerazione riparte da 1 sulla pagina dopo."""
    return ('<w:p><w:pPr><w:sectPr><w:type w:val="nextPage"/>'
            + PAGINA + '</w:sectPr></w:pPr></w:p>')

NUMBERING_TMPL = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="multilevel"/>
    <w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/>
      <w:pStyle w:val="Heading1"/><w:lvlText w:val="{CAP} %1 "/><w:lvlJc w:val="left"/>
      <w:suff w:val="nothing"/>
      <w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr>
      <w:rPr><w:b/><w:sz w:val="50"/><w:szCs w:val="50"/></w:rPr></w:lvl>
    <w:lvl w:ilvl="1"><w:start w:val="1"/><w:numFmt w:val="decimal"/>
      <w:pStyle w:val="Heading2"/><w:lvlText w:val="%1.%2"/><w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr></w:lvl>
    <w:lvl w:ilvl="2"><w:start w:val="1"/><w:numFmt w:val="decimal"/>
      <w:pStyle w:val="Heading3"/><w:lvlText w:val="%1.%2.%3"/><w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr></w:lvl>
    <w:lvl w:ilvl="3"><w:start w:val="1"/><w:numFmt w:val="decimal"/>
      <w:pStyle w:val="Heading4"/><w:lvlText w:val="%1.%2.%3.%4"/><w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr></w:lvl>
  </w:abstractNum>
  <w:abstractNum w:abstractNumId="1">
    <w:multiLevelType w:val="singleLevel"/>
    <w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="upperLetter"/>
      <w:pStyle w:val="Appendice"/><w:lvlText w:val="{APP} %1 "/><w:lvlJc w:val="left"/>
      <w:suff w:val="nothing"/>
      <w:pPr><w:ind w:left="0" w:firstLine="0"/></w:pPr>
      <w:rPr><w:b/><w:sz w:val="50"/><w:szCs w:val="50"/></w:rPr></w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
  <w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>
</w:numbering>'''

SETTINGS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '</w:settings>')

def tabella_invisibile(righe, larghezza=8504):
    """Due colonne senza bordi: serve a tenere le righe di relatore e candidato
    alla stessa altezza. In LaTeX lo stesso risultato si ottiene con tabular."""
    w = larghezza // 2
    nb = ('<w:tblBorders>' + ''.join(f'<w:{b} w:val="none" w:sz="0" w:space="0"/>'
          for b in ("top","left","bottom","right","insideH","insideV")) + '</w:tblBorders>')
    out = [f'<w:tbl><w:tblPr><w:tblW w:w="{larghezza}" w:type="dxa"/>{nb}'
           '<w:tblLayout w:type="fixed"/></w:tblPr>'
           f'<w:tblGrid><w:gridCol w:w="{w}"/><w:gridCol w:w="{w}"/></w:tblGrid>']
    for riga in righe:
        sinistra, destra = riga[0], riga[1]
        dopo = riga[2] if len(riga) > 2 else 60      # spazio per la firma, dove serve
        out.append('<w:tr>')
        for contenuto, allineamento in ((sinistra, "left"), (destra, "right")):
            out.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/></w:tcPr>'
                       f'<w:p><w:pPr><w:spacing w:after="{dopo}" w:line="240" w:lineRule="auto"/>'
                       f'<w:jc w:val="{allineamento}"/></w:pPr>{contenuto}</w:p></w:tc>')
        out.append('</w:tr>')
    out.append('</w:tbl>')
    return "".join(out)

def ancorato_in_fondo(runs, larghezza=8504):
    """Paragrafo ancorato al margine inferiore della pagina: l'anno accademico
    resta a fondo pagina qualunque sia la lunghezza del titolo. Non e` un pie`
    di pagina, e` una cornice ancorata al margine."""
    return (f'<w:p><w:pPr><w:framePr w:w="{larghezza}" w:hAnchor="margin" w:xAlign="center" '
            f'w:vAnchor="margin" w:yAlign="bottom" w:wrap="around"/>'
            '<w:pBdr><w:top w:val="single" w:sz="6" w:space="6" w:color="000000"/></w:pBdr>'
            '<w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/></w:pPr>'
            f'{runs}</w:p>')


def tabella(righe, larghezze):
    """Tabella con bordi sottili: prima riga di intestazione in grassetto."""
    bordo = '<w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>' \
            '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>' \
            '<w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>' \
            '<w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
    x = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>' % sum(larghezze),
         '<w:tblBorders>%s'
         '<w:insideH w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
         '<w:insideV w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
         '</w:tblBorders></w:tblPr><w:tblGrid>' % bordo]
    x += ['<w:gridCol w:w="%d"/>' % w for w in larghezze]
    x.append('</w:tblGrid>')
    for i, riga in enumerate(righe):
        x.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>')
        tieni = "<w:keepNext/>" if i < len(righe) - 1 else ""
        for j, cella in enumerate(riga):
            allin = '<w:jc w:val="left"/>' if j == 0 else '<w:jc w:val="right"/>'
            x.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr>'
                     '<w:p><w:pPr>%s%s<w:spacing w:after="40" w:line="240" w:lineRule="auto"/>'
                     '</w:pPr>%s</w:p></w:tc>'
                     % (larghezze[j], tieni, allin, run(cella, bold=(i == 0))))
        x.append('</w:tr>')
    x.append('</w:tbl><w:p><w:pPr><w:spacing w:after="120"/></w:pPr></w:p>')
    return "".join(x)


def titolo_appendice(testo):
    """Come il titolo di un capitolo, ma la numerazione e` alfabetica."""
    salto = '<w:r><w:rPr><w:sz w:val="48"/></w:rPr><w:br/><w:br/></w:r>'
    return para(salto + run(testo), style="Appendice",
                space_before=1734, space_after=800, line=240)

def titolo_capitolo(testo, suggerimento=""):
    """Il numero ("Capitolo N") arriva dalla numerazione, il titolo va a capo:
    e` la stessa resa del \\chapter di LaTeX."""
    salto = '<w:r><w:rPr><w:sz w:val="48"/></w:rPr><w:br/><w:br/></w:r>'
    if not suggerimento:
        return para(salto + run(testo), style="Heading1",
                    space_before=1734, space_after=800, line=240)
    return (para(salto + run(testo), style="Heading1",
                 space_before=1734, space_after=40, line=240)
            + para(run(suggerimento, italic=True), style="Guida",
                   align="left", space_after=800, line=240))


def numero_riga(n):
    """Numero di riga dello snippet, grigio e piccolo come in LaTeX."""
    return ('<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/>'
            f'<w:szCs w:val="16"/></w:rPr><w:t xml:space="preserve">{n}</w:t></w:r>'
            '<w:r><w:tab/></w:r>')
