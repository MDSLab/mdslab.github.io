---
layout: page
title: Embedded Systems
permalink: /teaching/courses/embedded-systems/
course_id: embedded-systems
---

{% assign c = site.data.teaching | where: "id", page.course_id | first %}
{% include course-header.html %}

<details class="faq-item" id="topics">
  <summary><h2>What is the course about?</h2></summary>
  <p>Designing and building embedded and cyber-physical systems: programming a microcontroller, acquiring data from analog and digital sensors, and driving actuators. The course works on three families of boards: Arduino UNO, with its ATmega microcontroller; Nucleo, built on STM32; and FPGA boards. It covers digital and analog I/O, serial communication, shift registers and motor control, and the design of a complete system under real-time, cost and power consumption constraints.</p>
  <p>The official programme is on the <a href="{{ c.links.catalogue }}">course page in the University catalogue</a>.</p>
</details>

<details class="faq-item" id="material">
  <summary><h2>Where do I find the course material?</h2></summary>
  <p>The most up-to-date material is on the University e-learning platform. Always refer to the latest academic year, which at the moment is <a href="{{ c.links.elearning }}">2026/2027</a>. Enrolment in the course is needed to reach the files.</p>
  <p>The homework marks are published there as well.</p>
</details>

<details class="faq-item" id="contact">
  <summary><h2>How do I contact the professor and where do I find announcements?</h2></summary>
  <p>Prof. Longo can be reached at <a href="mailto:francesco.longo@unime.it">francesco.longo@unime.it</a>, on WhatsApp or on Teams at any time: students are never an interruption.</p>
  <p>Office hours are on Tuesdays and Thursdays from 15.00 to 16.00, at the Department of Engineering, block B, seventh floor, room 743. It is best to send an email or a message beforehand, to make sure Prof. Longo is there.</p>
  <p>Last-minute announcements go through the class WhatsApp chat, which is the same one used for <a href="{{ '/teaching/courses/cybersecurity/' | relative_url }}">CyberSecurity</a>: that page explains how to join.</p>
</details>

<details class="faq-item" id="exam">
  <summary><h2>How is the exam structured?</h2></summary>
  <p>Two things are assessed: the homework assigned during the course, and the project with the oral examination that goes with it.</p>
  <p>Homework takes the form of slides, reports or videos, to be delivered by the deadline set for each assignment. It goes into a shared OneDrive folder that Prof. Longo creates on request. Every assignment is given a mark: one that is not delivered is marked 16, and one delivered late carries a penalty of five points, with 16 as the floor in any case. The marks are published on the e-learning platform.</p>
  <p>At the oral examination a single mark is given to the project and the discussion together. The final mark is the average of all the marks assigned.</p>
  <p>Registration for an exam session is on Esse3, which is also where the project deadline for that session is announced.</p>
</details>

<details class="faq-item" id="prep-project">
  <summary><h2>What do I need to know before submitting the project?</h2></summary>
  <p>The project has to result in a fully working embedded system, and it is developed individually. The best way to propose one is to write on Teams, where a chat dedicated to the project is then created and stays available for whatever comes up along the way. The proposal has to state the objectives and the functionalities of the system, the hardware platform and the development tools, and the software architecture with its main design choices.</p>
  <p class="faq-warning">The topic must be agreed with Prof. Longo before any implementation work begins. A project started on one's own initiative, without explicit approval, is not admitted to the oral examination.</p>
  <p>There are three modalities, each with its own maximum grade.</p>
  <ul>
    <li><b>A custom system on Arduino</b>, written in C: an embedded system of the student's own choosing. Maximum grade 24/30.</li>
    <li><b>Advanced AVR examples on Arduino</b>, written in C: one or more examples from <i>Make: AVR Programming</i>, taken from chapters and topics not covered in the lectures. Maximum grade 27/30.</li>
    <li><b>An advanced project on STM32 or FPGA</b>: an advanced or research-oriented topic, with a higher level of design complexity, system integration and technical depth. Maximum grade 30/30, with honours.</li>
  </ul>
  <p class="faq-warning">On the Arduino boards only standard C with direct hardware access is allowed. The Arduino programming model, with <code>setup()</code> and <code>loop()</code>, and every Arduino function or library, such as <code>digitalRead()</code> and <code>digitalWrite()</code>, are forbidden: a project that uses them is not accepted. The Arduino IDE may be used to compile and upload, and for nothing else.</p>
  <p>The grade rewards the correctness and the completeness of the implementation, its technical difficulty and how well it fits the modality that was chosen, the quality of the code, of the documentation and of the design, and the clarity, the technical depth and the maturity shown in the discussion. The homework done during the course counts here too.</p>
  <p>Three things have to be delivered by the deadline: a report explaining the theoretical background and the implementation, a slide deck to support the presentation, and all the source code, including scripts, configuration files and anything else needed to run or test the system. Prof. Longo creates a shared OneDrive folder for the project on request, separate from the one used for the homework, and the materials go there and nowhere else: folders created by students are not accepted, and a project missing any of the three is not accepted either.</p>
</details>

<details class="faq-item" id="prep-oral">
  <summary><h2>What do I need to know before the oral examination?</h2></summary>
  <p>The project is presented with the slide deck that was submitted, and its architecture, implementation choices and results are discussed, together with the trade-offs and the limits of the solution. The questions then move to the theory behind it, from microcontroller architecture, peripherals, timing and interrupts to communication protocols and digital design, depending on the project.</p>
  <p>A single mark is given to the project and the discussion together.</p>
  <p>If the project is rejected during the discussion, it can be improved and presented again at a later session, or replaced by a different one agreed with Prof. Longo.</p>
</details>

{% include faq-toggle.html %}
