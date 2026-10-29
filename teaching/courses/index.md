---
layout: page
translation: /teaching/courses/it/
translation_label: Vai all'italiano
title: Courses
permalink: /teaching/courses/
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

Courses taught by Francesco Longo at the Department of Engineering of the University of Messina and in other departments and doctoral schools of the University. Questa pagina è disponibile anche in italiano: basta cliccare sul pulsante in alto a destra.

<div class="teaching-section">
{% assign current = site.data.teaching | where: "status", "current" %}
{% assign past = site.data.teaching | where: "status", "past" %}

  <h2>Currently taught</h2>
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
        <span class="course-badge">{{ c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} hours &middot; taught in {{ c.language }}
        {%- if c.since != "" %} &middot; since {{ c.since }}{% endif -%}
      </p>
      {%- if cp %}
      {% include course-more.html cp=cp %}
      {%- endif %}
    </div>
{% endfor %}
  </div>

  <h2>Previously taught</h2>
  <div class="teaching-grid">
{% for c in past %}
    {%- assign cp = site.pages | where: "course_id", c.id | first -%}
    <div class="course-card{% if cp %} course-card--link{% endif %}" id="{{ c.id }}">
      <div class="course-head">
        <span class="course-title">{% if cp %}<a href="{{ cp.url | relative_url }}">{{ c.title }}</a>{% else %}{{ c.title }}{% endif %}</span>
        <span class="course-badge">{{ c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} hours &middot; taught in {{ c.language }} &middot; {{ c.since }}
      </p>
      {%- if cp %}
      {% include course-more.html cp=cp %}
      {%- endif %}
    </div>
{% endfor %}
  </div>
</div>
