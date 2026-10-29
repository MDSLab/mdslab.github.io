---
layout: page
title: CyberSecurity
permalink: /teaching/courses/cybersecurity/
course_id: cybersecurity
---

{% assign c = site.data.teaching | where: "id", page.course_id | first %}
{% include course-header.html %}

<details class="faq-item" id="topics">
  <summary><h2>What is the course about?</h2></summary>
  <p>Attacking and defending information systems, and the cryptography that makes defence possible. Four areas: software and memory security, from buffer overflows and stack smashing to return-oriented programming; cryptography, from symmetric ciphers and hash functions to public-key cryptography, digital signatures and PKI; web security, from the same-origin policy to XSS, CSRF and SQL injection; and network security, from TLS and DNSSEC to man-in-the-middle and denial-of-service attacks.</p>
  <p>The official programme is on the <a href="{{ c.links.catalogue }}">course page in the University catalogue</a>.</p>
</details>

<details class="faq-item" id="material">
  <summary><h2>Where do I find the course material?</h2></summary>
  <p>The most up-to-date material is on the University e-learning platform. Always refer to the latest academic year, which at the moment is <a href="{{ c.links.elearning }}">2025/2026</a>. Enrolment in the course is needed to reach the files.</p>
</details>

<details class="faq-item" id="contact">
  <summary><h2>How do I contact the professor and where do I find announcements?</h2></summary>
  <p>Prof. Longo can be reached at <a href="mailto:francesco.longo@unime.it">francesco.longo@unime.it</a>, on WhatsApp or on Teams at any time: students are never an interruption. The names and contacts of the course tutors are in the course slides.</p>
  <p>Office hours are on Tuesdays and Thursdays from 15.00 to 16.00, at the Department of Engineering, block B, seventh floor, room 743. It is best to send an email or a message beforehand, to make sure Prof. Longo is there.</p>
  <p>Official announcements go through the class WhatsApp chat, which is joined by scanning the QR code in the course slides. The same chat serves <a href="{{ '/teaching/courses/embedded-systems/' | relative_url }}">Embedded Systems</a>.</p>
</details>

<details class="faq-item" id="exam">
  <summary><h2>How is the exam structured?</h2></summary>
  <p>Three parts, each with its own weight on the final grade.</p>
  <ul>
    <li><b>Homework</b>, done during the course on a dedicated platform. 10%.</li>
    <li><b>The project and its interview</b>, which takes place before the oral examination. 40%.</li>
    <li><b>The oral examination</b>, on everything the course has covered. 50%.</li>
  </ul>
  <p>Registration for an exam session is on Esse3. Before each session Prof. Longo announces the deadline for submitting the project and the date and time of the project interview.</p>
</details>

<details class="faq-item" id="homework">
  <summary><h2>What do I need to know about the homework?</h2></summary>
  <p>There are four assignments, one per unit of the course, and they weigh the same as each other. They are done individually, on a platform that is reachable only through the University VPN. The e-learning page has its address and a guide to connecting through the VPN.</p>
  <p>The score depends on how many challenges are solved and on how quickly. An assignment that is not delivered counts as zero and enters the average all the same, so a missing one weighs on the whole 10%.</p>
  <p class="faq-warning">Registration on the platform must use the student's full name, first name and family name. Work submitted under any other name is not marked, and counts as zero.</p>
</details>

<details class="faq-item" id="prep-project">
  <summary><h2>What do I need to know before submitting the project?</h2></summary>
  <p>The project is a piece of cybersecurity work with a practical implementation, developed individually. Once the topic is agreed, a chat dedicated to the project is created on Teams, and that is where the project is discussed, for whatever comes up along the way.</p>
  <p class="faq-warning">The topic must be agreed with Prof. Longo and explicitly approved in advance. A student whose topic has not been approved beforehand is not admitted to the project interview.</p>
  <p>There are three modalities, each with its own maximum grade.</p>
  <ul>
    <li><b>A practical project on the course topics</b>: reproducing, analysing and extending an attack or a technique seen in the lectures or the tutorials — buffer overflow and binary exploitation, CSRF, XSS and SQL injection, TLS and cryptographic protocols, ARP spoofing and basic network attacks. Maximum grade 22/30.</li>
    <li><b>An advanced project</b>, on topics not covered in the lectures, calling for technical autonomy and a substantial original implementation: malware analysis, reverse engineering, intrusion detection systems, custom security tools or frameworks. Maximum grade 26/30.</li>
    <li><b>A research-oriented project</b>, on innovative topics, where originality, technical complexity, experimental evaluation and significant software development carry the most weight: novel attack or defence techniques, firmware and hardware security, AI-based security systems, experimental security architectures. Maximum grade 30/30, with honours.</li>
  </ul>
  <p>Three things have to be delivered by the deadline: a report explaining the theoretical background and the implementation, a slide deck to support the presentation, and all the source code, including scripts, configuration files, datasets and anything else needed to run or test the implementation. Prof. Longo creates a shared OneDrive folder on request, and the materials go there and nowhere else: folders created by students are not accepted, and a project missing any of the three is not accepted either.</p>
  <p>The grade rewards the originality and the relevance of the topic, the completeness of the analysis, the quality and correctness of the implementation, the practical demonstration of vulnerabilities and defences, and the clarity of the presentation. What counts most is how much code the student wrote personally and how far the work goes beyond wiring together existing libraries, frameworks and tools: a project that rests almost entirely on ready-made tools, with little original contribution, is marked down. Advanced technical solutions, reverse engineering, complex attack and defence scenarios, substantial original development and creative approaches can earn bonus points.</p>
</details>

<details class="faq-item" id="prep-interview">
  <summary><h2>What do I need to know before the project interview?</h2></summary>
  <p>The interview takes place before the oral examination, on the date announced for that exam session. The project is presented with the slide deck that was submitted, its technical aspects are explained, and the implementation and design choices are justified. The questions can reach any part of the submitted material, including the source code, and full command of what was handed in is expected.</p>
  <p>At the end of the discussion the project grade is assigned. Together with the project it is worth 40% of the final grade.</p>
</details>

<details class="faq-item" id="prep-oral">
  <summary><h2>What do I need to know before the oral examination?</h2></summary>
  <p>The oral examination covers everything the course has gone through: the lectures, the tutorials, the homework and the project. It is worth 50% of the final grade, the largest share of the three.</p>
  <p>What is expected is an understanding of cybersecurity concepts and methods, knowledge of attacks, vulnerabilities and countermeasures, the ability to reason about practical scenarios, and familiarity with the work submitted during the course. The questions range from theoretical discussion to practical reasoning, and can also concern the homework, to confirm that it was done personally.</p>
</details>

<details class="faq-item" id="integrity">
  <summary><h2>What are the rules on original work?</h2></summary>
  <p>Everything submitted must be the student's own work, and the student must be able to explain it: the implementation choices, the structure and the behaviour of the source code, the methods and technologies used, the attacks and countermeasures implemented, and the homework solutions.</p>
  <p>This is checked by asking. During the project interview and at the oral examination the questions can go into detail on any part of what was submitted, and a student who cannot show a sufficient grasp of their own work is marked down for it.</p>
</details>

{% include faq-toggle.html %}
