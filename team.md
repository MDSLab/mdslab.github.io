---
layout: page
title: Team
permalink: /team/
---

<style>
.lab-director {
  display: flex;
  gap: 2em;
  align-items: center;
  margin: 2em 0 2.5em;
}

.director-photo {
  flex: 0 0 210px;
  border-radius: 8px;
  overflow: hidden;
  border: 3px solid var(--line);
}

.director-photo img {
  width: 100%;
  display: block;
  border: none !important;
  border-radius: 0 !important;
  margin: 0 !important;
  max-width: none !important;
}

.director-name {
  display: block;
  font-weight: bold;
  font-size: 1.35em;
  color: var(--ink);
}

.director-role {
  display: block;
  margin-bottom: 0.8em;
}

.director-bio {
  margin: 0 0 1em;
}

/* Sotto i 700px la foto va sopra il testo invece che accanto */
@media (max-width: 700px) {
  .lab-director {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .director-photo { flex-basis: auto; width: 180px; }
  .director-bio { text-align: left; }
}

.people-section {
  margin: 2em 0;
}

.people-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5em;
}

.person-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 160px;
}

.img-circle {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--line);
  margin-bottom: 0.8em;
  transition: border-color 0.3s ease;
}

/* Segnaposto per chi non ha ancora una foto: iniziali su fondo neutro */
.img-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: bold;
  font-size: 2.2em;
  letter-spacing: 1px;
}

.person-dialog-photo-placeholder {
  flex: 0 0 150px;
  width: 150px;
  height: 150px;
  border-radius: var(--radius);
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: bold;
  font-size: 2.6em;
}

/* Le foto dei membri attuali sono collegamenti: aprono la scheda */
a.img-circle {
  display: block;
  border-bottom: none;
}

a.img-circle:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.img-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0 !important;
  border: none !important;
  margin: 0 !important;
  max-width: none !important;
  display: block;
}

.person-name {
  font-weight: bold;
  font-size: 0.95em;
  color: var(--ink);
  margin-bottom: 0.2em;
}

/* Stessa tipografia del ruolo del direttore, ma in grigio: l'azzurro resta
   riservato a chi guida il gruppo. Allineato in fondo alla scheda, così resta
   alla stessa altezza anche quando il nome accanto occupa due righe. */
/* Ruolo e parole chiave stanno attaccati al nome. Prima `margin-top: auto`
   li spingeva in fondo alla scheda per allinearli fra colonne, ma con nomi di
   lunghezza diversa si staccavano dalla persona a cui si riferiscono. */
.person-role {
  font-size: 0.7em;
  text-transform: uppercase;
  letter-spacing: 1px;
  line-height: 1.4;
  margin-top: 0.1em;
}

/* Le tre cose su cui la persona lavora, sotto il ruolo: chi cerca un relatore
   o un collaboratore le legge senza aprire la scheda. */
.person-keywords {
  font-size: 0.68em;
  line-height: 1.45;
  color: var(--muted);
  margin-top: 0.45em;
}

/* Gli ex membri restano volutamente più sobri di chi c'è ora: la pagina
   deve parlare prima del gruppo attuale. */
.alumni-section {
  margin-top: 3em;
  border-top: 1px solid var(--line);
  padding-top: 1.5em;
}

.alumni-section h2 {
  margin-bottom: 1em;
}

/* ── Scheda della persona ─────────────────────────────────────────────── */

.person-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  z-index: 900;
}

.person-dialog {
  position: fixed;
  z-index: 901;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(680px, calc(100vw - 2em));
  max-height: calc(100vh - 3em);
  overflow-y: auto;
  background: #fff;
  border-radius: var(--radius);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.person-dialog-inner {
  display: flex;
  gap: 1.4em;
  padding: 1.6em;
}

.person-dialog-photo {
  flex: 0 0 150px;
  width: 150px;
  height: 150px;
  border-radius: var(--radius);
  object-fit: cover;
  display: block;
  margin: 0 !important;
  max-width: none !important;
  border: none !important;
}

.person-dialog h2 {
  margin: 0;
  font-size: 1.3em;
  color: var(--accent);
}

.person-dialog-role {
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: var(--muted);
  margin: 0.2em 0 0.9em;
}

.person-dialog-bio {
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0 0 1em;
}

.person-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
}

.person-links a {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-bottom: none;
  background: var(--accent-soft);
  color: var(--accent);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s ease, color 0.2s ease;
}

.person-links a:hover,
.person-links a:focus-visible {
  background: var(--accent);
  color: #fff;
}

.person-dialog-close {
  position: absolute;
  top: 0.5em;
  right: 0.7em;
  background: none;
  border: none;
  font-size: 1.6em;
  line-height: 1;
  cursor: pointer;
  color: var(--muted);
  padding: 0.2em;
}

.person-dialog-close:hover { color: var(--ink); }

@media (max-width: 600px) {
  .person-dialog-inner {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .person-dialog-bio { text-align: left; }
  .person-links { justify-content: center; }
}
</style>

The people of MDSLab. Each photograph opens a short profile.

{% assign d = site.data.director %}
{% if d.name and d.name != "" %}
<div class="lab-director">
  <div class="director-photo">
    {% if d.photo != "" %}<img src="{{ d.photo }}" alt="{{ d.name }}">{% endif %}
  </div>
  <div class="director-text">
    <span class="director-name">{{ d.name }}</span>
    <span class="director-role">{{ d.role }}</span>
    <p class="director-bio">{{ d.bio }}</p>
    {% include person-links.html links=d.links name=d.name %}
  </div>
</div>
{% endif %}

{% if site.data.people.size > 0 %}
<div class="people-section">
  <div class="people-grid">
{% for p in site.data.people %}
    <div class="person-card">
      {%- assign parts = p.name | split: " " -%}
      {%- capture initials -%}{{ parts.first | slice: 0 }}{{ parts.last | slice: 0 }}{%- endcapture -%}
      <a class="img-circle" href="#{{ p.id }}" aria-haspopup="dialog" aria-label="Open profile of {{ p.name }}">
        {% if p.photo != "" %}<img src="{{ p.photo }}" alt="{{ p.name }}"{% if p.photo_position %} style="object-position: {{ p.photo_position }} !important;"{% endif %}>{% else %}<span class="img-placeholder" aria-hidden="true">{{ initials }}</span>{% endif %}
      </a>
      <span class="person-name">{{ p.name }}</span>
      <span class="person-role">{{ p.role }}</span>
      {%- comment -%}
        La riga sotto il nome: i temi di _data/topics.yml per chi li ha mandati,
        le vecchie parole chiave scritte a mano per chi deve ancora rispondere.
      {%- endcomment -%}
      {%- if p.topics -%}
        {%- comment -%} l'ordine e` quello in cui la persona ha scritto i propri
          temi, non quello del vocabolario: il primo e` il tema principale. {%- endcomment -%}
        {%- assign righe = "" -%}
        {%- for k in p.topics -%}
          {%- assign t = site.data.topics | where: "key", k | first -%}
          {%- if righe == "" -%}{%- assign righe = t.label -%}
          {%- else -%}{%- assign righe = righe | append: " &middot; " | append: t.label -%}{%- endif -%}
        {%- endfor -%}
        <span class="person-keywords">{{ righe }}</span>
      {%- elsif p.keywords -%}
        <span class="person-keywords">{{ p.keywords }}</span>
      {%- endif -%}
    </div>
{% endfor %}
  </div>
</div>
{% endif %}

{% if site.data.alumni.size > 0 %}
<div class="alumni-section">
  <h2>Former Members</h2>
  <div class="people-grid">
{% for a in site.data.alumni %}
    <div class="person-card">
      <div class="img-circle">
        {%- assign aparts = a.name | split: " " -%}
        {% if a.photo and a.photo != "" %}<img src="{{ a.photo }}" alt="{{ a.name }}">{% else %}<span class="img-placeholder" aria-hidden="true">{{ aparts.first | slice: 0 }}{{ aparts.last | slice: 0 }}</span>{% endif %}
      </div>
      <span class="person-name">{{ a.name }}</span>
      <span class="person-role">{{ a.role }}</span>
    </div>
{% endfor %}
  </div>
</div>
{% endif %}

{% comment %}
Le schede stanno nel documento anche quando sono chiuse: restano leggibili
dai motori di ricerca e non dipendono dal JavaScript per esistere.
{% endcomment %}
{% for p in site.data.people %}
<div class="person-dialog" id="dialog-{{ p.id }}" role="dialog" aria-modal="true" aria-labelledby="name-{{ p.id }}" hidden>
  <button type="button" class="person-dialog-close" aria-label="Close">&times;</button>
  <div class="person-dialog-inner">
    {%- assign dparts = p.name | split: " " -%}
    {% if p.photo != "" %}<img class="person-dialog-photo" src="{{ p.photo }}" alt=""{% if p.photo_position %} style="object-position: {{ p.photo_position }} !important;"{% endif %}>{% else %}<span class="person-dialog-photo-placeholder" aria-hidden="true">{{ dparts.first | slice: 0 }}{{ dparts.last | slice: 0 }}</span>{% endif %}
    <div>
      <h2 id="name-{{ p.id }}">{{ p.name }}</h2>
      <p class="person-dialog-role">{{ p.role }}</p>
      {% if p.bio != "" %}<p class="person-dialog-bio">{{ p.bio }}</p>{% endif %}
      {% include person-links.html links=p.links name=p.name %}
    </div>
  </div>
</div>
{% endfor %}

<script>
(function () {
  var dialogs = {};
  document.querySelectorAll('.person-dialog').forEach(function (d) {
    dialogs[d.id.replace('dialog-', '')] = d;
  });
  if (!Object.keys(dialogs).length) return;

  var backdrop = null, current = null, lastFocus = null;

  function focusables(el) {
    return el.querySelectorAll('a[href], button:not([disabled])');
  }

  function open(id) {
    var d = dialogs[id];
    if (!d || current === d) return;
    close(true);
    lastFocus = document.activeElement;
    backdrop = document.createElement('div');
    backdrop.className = 'person-backdrop';
    backdrop.addEventListener('click', function () { close(); });
    document.body.appendChild(backdrop);
    d.hidden = false;
    current = d;
    var f = focusables(d);
    (f[0] || d).focus();
  }

  function close(silent) {
    if (!current) return;
    current.hidden = true;
    current = null;
    if (backdrop) { backdrop.remove(); backdrop = null; }
    if (!silent) {
      // toglie l'ancora senza aggiungere una voce alla cronologia
      history.replaceState(null, '', location.pathname + location.search);
      if (lastFocus) lastFocus.focus();
    }
  }

  // Esc chiude, Tab resta dentro la scheda
  document.addEventListener('keydown', function (e) {
    if (!current) return;
    if (e.key === 'Escape') { close(); return; }
    if (e.key !== 'Tab') return;
    var f = focusables(current);
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  document.querySelectorAll('.person-dialog-close').forEach(function (b) {
    b.addEventListener('click', function () { close(); });
  });

  function fromHash() {
    var id = location.hash.replace('#', '');
    if (dialogs[id]) open(id); else close(true);
  }

  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
</script>
