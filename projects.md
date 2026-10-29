---
layout: page
title: Projects
permalink: /projects/
---

Research projects carried out by MDSLab.

<style>
/* Riquadri, pillole e colori arrivano da /assets/css/mdslab.css */
.project-section h2 {
  font-size: 0.9em;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--muted);
  margin: 2.2em 0 1.2em;
}

.project-item {
  background: var(--surface);
  border: 1px solid var(--line);
  border-left: 4px solid var(--accent-bright);
  border-radius: var(--radius);
  padding: 1.2em 1.4em;
  margin-bottom: 1.2em;
}

.project-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.6em;
  margin-bottom: 0.2em;
}

.project-acronym {
  font-weight: bold;
  font-size: 1.15em;
  color: var(--ink);
}

.project-role {
  font-size: 0.7em;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--accent);
  background: var(--accent-soft);
  border-radius: 20px;
  padding: 0.25em 0.8em;
}

.project-title {
  font-size: 0.95em;
  font-style: italic;
  color: var(--body-text);
  margin-bottom: 0.7em;
}

/* Il periodo era sepolto nella riga del programma, fra il decreto ministeriale
   e la cifra: è la seconda cosa che si cerca dopo il nome, e sta in testa. */
.project-period {
  font-size: 0.8em;
  color: var(--muted);
}

/* Le etichette tematiche. Le stesse tre chiavi di _data/areas.yml che marcano
   persone e progetti: qui sono il primo posto in cui si vedono. */
.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4em;
  margin-top: 0.8em;
}

.project-tag {
  font-size: 0.72em;
  letter-spacing: 0.5px;
  color: var(--muted);
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 20px;
  padding: 0.2em 0.7em;
}

/* I dati di riferimento — bando, cifra, partner — stanno sotto e staccati:
   servono a chi valuta, non a chi legge per capire cosa fa il progetto. */
.project-ref {
  margin-top: 1em;
  padding-top: 0.8em;
  border-top: 1px solid var(--line);
}

.project-scope {
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--body-text);
  margin-bottom: 0.3em;
}

/* Il titolo del progetto padre sta nella riga gerarchica, ma è un titolo
   proprio: non va in maiuscoletto come il resto della riga. */
.project-parent {
  text-transform: none;
  letter-spacing: normal;
  font-style: italic;
  color: var(--muted);
}

.project-meta {
  font-size: 0.8em;
  color: var(--muted);
  margin: 0;
  line-height: 1.6;
}

.project-meta b {
  color: var(--body-text);
  font-weight: normal;
}

.project-partners b {
  color: var(--body-text);
  font-weight: normal;
}

.project-description {
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0;
}

.project-partners {
  font-size: 0.8em;
  color: var(--muted);
  margin: 0.7em 0 0;
}
</style>

<div class="project-section">
{% assign current = site.data.projects | where: "status", "current" %}
{% assign past = site.data.projects | where: "status", "past" %}

{% if current.size > 0 %}
  <h2>Ongoing</h2>
{% endif %}
{% for p in current %}
  <div class="project-item" id="{{ p.id }}">
    <div class="project-head">
      <span class="project-acronym">{{ p.acronym }}</span>
      <span class="project-period">{{ p.period }}</span>
      <span class="project-role">{{ p.role }}</span>
    </div>
    <div class="project-title">{{ p.title }}</div>
    <p class="project-description">{{ p.description }}</p>
    {%- if p.areas %}
    <div class="project-tags">
      {%- for key in p.areas -%}
        {%- assign a = site.data.areas | where: "key", key | first -%}
        <span class="project-tag">{{ a.tag }}</span>
      {%- endfor -%}
    </div>
    {%- endif %}
    <div class="project-ref">
      {%- if p.scope != "" or p.project != "" %}
      <div class="project-scope">{{ p.scope }}{% if p.project != "" %}{% if p.scope != "" %} &mdash; {% endif %}Project {{ p.project }}{% if p.project_title != "" %} <span class="project-parent">{{ p.project_title }}</span>{% endif %}{% endif %}</div>
      {%- endif %}
      <div class="project-meta">
        {{ p.programme }}{% if p.funding != "" %} &middot; <b>{{ p.funding }}</b>{% endif %}
      </div>
      {% if p.partners != "" %}<p class="project-partners"><b>Main research partners:</b> {{ p.partners }}</p>{% endif %}
    </div>
  </div>
{% endfor %}

{% if past.size > 0 %}
  <h2>Concluded</h2>
{% endif %}
{% for p in past %}
  <div class="project-item" id="{{ p.id }}">
    <div class="project-head">
      <span class="project-acronym">{{ p.acronym }}</span>
      <span class="project-period">{{ p.period }}</span>
      <span class="project-role">{{ p.role }}</span>
    </div>
    <div class="project-title">{{ p.title }}</div>
    <p class="project-description">{{ p.description }}</p>
    {%- if p.areas %}
    <div class="project-tags">
      {%- for key in p.areas -%}
        {%- assign a = site.data.areas | where: "key", key | first -%}
        <span class="project-tag">{{ a.tag }}</span>
      {%- endfor -%}
    </div>
    {%- endif %}
    <div class="project-ref">
      {%- if p.scope != "" or p.project != "" %}
      <div class="project-scope">{{ p.scope }}{% if p.project != "" %}{% if p.scope != "" %} &mdash; {% endif %}Project {{ p.project }}{% if p.project_title != "" %} <span class="project-parent">{{ p.project_title }}</span>{% endif %}{% endif %}</div>
      {%- endif %}
      <div class="project-meta">
        {{ p.programme }}{% if p.funding != "" %} &middot; <b>{{ p.funding }}</b>{% endif %}
      </div>
      {% if p.partners != "" %}<p class="project-partners"><b>Main research partners:</b> {{ p.partners }}</p>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
