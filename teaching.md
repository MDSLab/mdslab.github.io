---
layout: page
title: Teaching
permalink: /teaching/
---

<style>
.teaching-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5em;
  margin: 2em 0;
}

.course-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5em;
  background: #fafafa;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  border-left: 4px solid #6a0dad;
}

.course-card:hover {
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transform: translateY(-3px);
}

.course-title {
  font-size: 1.1em;
  font-weight: bold;
  color: #1a1a2e;
  margin-bottom: 0.5em;
}

.course-degree {
  font-size: 0.85em;
  color: #555;
  margin-bottom: 0.8em;
  line-height: 1.5;
}

.course-degree span {
  font-style: italic;
}

.course-badge {
  display: inline-block;
  font-size: 0.75em;
  padding: 0.2em 0.7em;
  border-radius: 20px;
  background: #ede7f6;
  color: #6a0dad;
  margin-bottom: 0.8em;
}

.course-professor {
  font-size: 0.85em;
  color: #888;
  display: flex;
  align-items: center;
  gap: 0.4em;
}

.course-professor i {
  color: #6a0dad;
}

@media (max-width: 600px) {
  .teaching-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="teaching-grid">

  <div class="course-card">
    <div class="course-title">Fondamenti di Informatica</div>
    <span class="course-badge">Bachelor's Degree</span>
    <div class="course-degree">Bachelor's Degree Programme in <span>"Ingegneria Elettronica ed Informatica"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </div>

  <div class="course-card">
    <div class="course-title">CyberSecurity</div>
    <span class="course-badge">Master's Degree</span>
    <div class="course-degree">Master's Degree Programme in <span>"Engineering in Computer Science"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </div>

  <div class="course-card">
    <div class="course-title">Embedded Systems</div>
    <span class="course-badge">Master's Degree</span>
    <div class="course-degree">Master's Degree Programme in <span>"Engineering in Computer Science"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </div>




</div>
