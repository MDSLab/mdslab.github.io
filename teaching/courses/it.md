---
layout: page
translation: /teaching/courses/
translation_label: Go to English
lang: it
title: Corsi
permalink: /teaching/courses/it/
---

<style>
/* Riquadri, pillole e colori stanno in /assets/css/mdslab.css */
.teaching-section h2 {
  font-size: 0.9em;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--muted);
  margin: 2.2em 0 1.2em;
}

.teaching-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2em;
}

.course-card {
  padding: 1.2em 1.4em;
}

.course-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.6em;
  margin-bottom: 0.4em;
}

.course-title {
  font-weight: bold;
  font-size: 1.05em;
  color: var(--ink);
}

.course-programme {
  font-size: 0.9em;
  font-style: italic;
  color: var(--body-text);
  margin-bottom: 0.6em;
}

.course-role {
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--body-text);
  margin-bottom: 0.3em;
}

.course-meta {
  font-size: 0.8em;
  color: var(--muted);
  margin: 0;
}

/* Invito a entrare nella pagina del corso: compare solo sulle schede che una
   pagina ce l'hanno, ed è nella lingua di erogazione del corso perché parla a
   chi quel corso lo segue. */
.course-more {
  font-size: 0.8em;
  color: var(--accent);
  margin: 0.7em 0 0;
}

@media (max-width: 700px) {
  .teaching-grid {
    grid-template-columns: 1fr;
  }
}
</style>

Corsi tenuti da Francesco Longo al Dipartimento di Ingegneria dell'Università degli Studi di Messina e in altri dipartimenti e scuole di dottorato dell'Ateneo. This page is also available in English: just click the button at the top right.

<div class="teaching-section">
{% assign current = site.data.teaching | where: "status", "current" %}
{% assign past = site.data.teaching | where: "status", "past" %}

  <h2>Insegnamenti attuali</h2>
  <div class="teaching-grid">
{% for c in current %}
    {%- comment -%}
    Un corso è cliccabile se esiste una pagina che lo dichiara con `course_id`:
    il collegamento compare creando il file, senza doverlo elencare anche qui.
    {%- endcomment -%}
    {%- assign cp = site.pages | where: "course_id", c.id | first -%}
    <div class="course-card{% if cp %} course-card--link{% endif %}" id="{{ c.id }}">
      <div class="course-head">
        <span class="course-title">{% if cp %}<a href="{{ cp.url | relative_url }}">{{ c.title }}</a>{% else %}{{ c.title }}{% endif %}</span>
        <span class="course-badge">{{ site.data.i18n.level[c.level] | default: c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ site.data.i18n.role[c.role] | default: c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} ore &middot; in {{ site.data.i18n.language[c.language] | default: c.language }}
        {%- if c.since != "" %} &middot; dal {{ c.since }}{% endif -%}
      </p>
      {%- if cp %}
      {% include course-more.html cp=cp %}
      {%- endif %}
    </div>
{% endfor %}
  </div>

  <h2>Insegnamenti passati</h2>
  <div class="teaching-grid">
{% for c in past %}
    {%- assign cp = site.pages | where: "course_id", c.id | first -%}
    <div class="course-card{% if cp %} course-card--link{% endif %}" id="{{ c.id }}">
      <div class="course-head">
        <span class="course-title">{% if cp %}<a href="{{ cp.url | relative_url }}">{{ c.title }}</a>{% else %}{{ c.title }}{% endif %}</span>
        <span class="course-badge">{{ site.data.i18n.level[c.level] | default: c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ site.data.i18n.role[c.role] | default: c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} ore &middot; in {{ site.data.i18n.language[c.language] | default: c.language }} &middot; {{ c.since }}
      </p>
      {%- if cp %}
      {% include course-more.html cp=cp %}
      {%- endif %}
    </div>
{% endfor %}
  </div>
</div>
