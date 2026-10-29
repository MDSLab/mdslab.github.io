---
layout: home
title: MDSLab
image:
  path: /images/hero.jpg
---

<style>
.masthead {
  margin-bottom: 0 !important;
}

.main-content {
  padding-top: 0 !important;
}

.page-image {
  margin-top: 0 !important;
  padding-top: 0 !important;
  margin-bottom: 6px !important;
}

/* Altezza legata al viewport: su schermi bassi la testata si ritira
   invece di spingere il testo sotto la piega. */
.entry-feature-image {
  height: 22vh;
  min-height: 160px;
  max-height: 350px;
  width: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.page-header h1 {
  font-size: 2.5rem;
}

.page-content p {
  margin-bottom: 0.9em;
}

/* Il nome per esteso, subito sotto la sigla del laboratorio. Il selettore
   nomina .page-content perche' li' dentro i paragrafi sono giustificati, e
   questo va centrato. */
.page-content p.acronimo {
  text-align: center;
  margin: -0.4em 0 1.6em;
  font-size: 1.02em;
  line-height: 1.4;
  color: var(--muted);
  letter-spacing: 0.3px;
}

.site-footer {
  margin-top: 10px !important;
  margin-bottom: 10px !important;
  padding-top: 14px !important;
  padding-bottom: 14px !important;
}

/* I loghi hanno proporzioni molto diverse fra loro e non stanno in una riga
   larga quanto la colonna di testo: questa fascia sfonda il contenitore. */
.partners-section {
  margin: 1.1em 0;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  width: 94vw;
  max-width: 1040px;
}

.partners-section h3 {
  text-align: center;
  margin-bottom: 0.9em;
}

.partners-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 1.5em;
}

.partners-grid a {
  display: inline-flex;
  align-items: center;
  border-bottom: none;
}

.partners-grid img {
  height: 60px;
  width: auto;
  max-width: 120px;
  object-fit: contain;
  filter: grayscale(100%);
  opacity: 0.7;
  transition: all 0.3s ease;
}

.partners-grid a:hover img {
  filter: grayscale(0%);
  opacity: 1;
}
</style>

<p class="acronimo">Mobile and Distributed Systems Laboratory</p>



{% if site.data.partners.size > 0 %}
---

<div class="partners-section" id="partners">
  <h3>Our Partners</h3>
  <div class="partners-grid">
{%- for p in site.data.partners %}
    <a href="{{ p.url }}" target="_blank" rel="noopener" title="{{ p.name }}"><img src="{{ p.logo | relative_url }}" alt="{{ p.name }}"></a>
{%- endfor %}
  </div>
</div>
{% endif %}
