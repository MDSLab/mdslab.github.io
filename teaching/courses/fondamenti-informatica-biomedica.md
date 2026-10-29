---
layout: page
lang: it
title: Fondamenti di Informatica (modulo A)
permalink: /teaching/courses/fondamenti-informatica-biomedica/
course_id: fondamenti-informatica-biomedica
---

{% assign c = site.data.teaching | where: "id", page.course_id | first %}
{% include course-header.html %}

<details class="faq-item" id="structure">
  <summary><h2>Com'è organizzato il corso?</h2></summary>
  <p>Il corso è diviso in due moduli, A e B, tenuti da docenti diversi. Il modulo A è tenuto dal Prof. Longo, il modulo B in questo momento dal Prof. Luca D'Agati.</p>
  <p>Tutte le informazioni di questa pagina riguardano il modulo A. Per quelle sul modulo B occorre rivolgersi al Prof. D'Agati.</p>
</details>

<details class="faq-item" id="topics">
  <summary><h2>Di cosa parla il modulo A?</h2></summary>
  <p>Di come si rappresenta ed elabora l'informazione in un calcolatore e di come si programma in C: dal sistema binario, dall'architettura di Von Neumann e dagli algoritmi fino ai costrutti del linguaggio C, agli array e ai puntatori.</p>
  <p>Il programma ufficiale si trova sulla <a href="{{ c.links.catalogue }}">pagina del modulo A nel catalogo di Ateneo</a>.</p>
</details>

<details class="faq-item" id="material">
  <summary><h2>Dove trovo il materiale didattico del modulo A?</h2></summary>
  <p>Il materiale più aggiornato si trova sul sistema di e-learning di Ateneo. Conviene fare sempre riferimento all'ultimo anno accademico, che in questo momento è il <a href="{{ c.links.elearning }}">2026/2027</a>. Per accedere ai file è necessario iscriversi al corso.</p>
</details>

<details class="faq-item" id="contact">
  <summary><h2>Come contatto il professore e dove trovo gli avvisi?</h2></summary>
  <p>Il Prof. Longo è raggiungibile all'indirizzo <a href="mailto:francesco.longo@unime.it">francesco.longo@unime.it</a>, su WhatsApp o su Teams in qualunque momento: gli studenti non disturbano mai.</p>
  <p>Il ricevimento in presenza è il martedì e il giovedì dalle 15.00 alle 16.00, al Dipartimento di Ingegneria, blocco B, settimo piano, stanza 743. È bene avvisare prima con una mail o un messaggio, per avere conferma che il Prof. Longo sia presente.</p>
  <p>Gli avvisi dell'ultimo minuto passano dalla chat WhatsApp di classe, usata dal Prof. Longo anche per condividere notizie dal Dipartimento e dall'Ateneo. Ne viene creata una nuova ogni anno accademico: il QR code per entrare si trova nel blocco di slide 0 del modulo A, sull'e-learning.</p>
</details>

<details class="faq-item" id="exam">
  <summary><h2>Com'è strutturato l'esame del modulo A?</h2></summary>
  <p>Due prove scritte.</p>
  <ul>
    <li><b>Prima prova scritta</b>, test a risposta multipla più un esercizio su carta. Argomenti: conoscere i principi di base dell'informatica, l'architettura dell'elaboratore, la rappresentazione digitale dell'informazione e i concetti di base dei linguaggi, ovvero tutto il programma fino all'introduzione al linguaggio C inclusa (blocchi da 1 a 5).</li>
    <li><b>Seconda prova scritta</b>, prova di programmazione di base al calcolatore. Argomenti: conoscere i concetti di base del linguaggio C, variabili e I/O di base, espressioni e operatori, strutture di controllo, array e stringhe, puntatori, tipi strutturati, funzioni e file, ovvero tutta la parte sul C (blocchi da 6 a 13).</li>
  </ul>
  <p>I voti delle due prove del modulo A fanno media con i voti del modulo B nel voto del corso integrato.</p>
  <p>Durante il primo semestre si svolgono due prove in itinere, corrispondenti alla prima e alla seconda prova scritta. Valgono esattamente un anno, fino alla corrispondente prova in itinere dell'anno successivo: per gli studenti in corso, fino all'appello di novembre incluso.</p>
  <p>Se le prove in itinere non vengono sostenute o non vengono superate, a ogni appello è possibile ripetere la prima e la seconda prova scritta.</p>
  <p>I testi delle prove precedenti sono raccolti per prova: <a href="{{ c.links.archive_1 }}">prima</a> e <a href="{{ c.links.archive_2 }}">seconda</a>.</p>
</details>

<details class="faq-item" id="prep-1">
  <summary><h2>Cosa devo sapere prima di sostenere la prima prova?</h2></summary>
  <p>La prova consiste in un quiz a risposta multipla e in un diagramma di flusso da disegnare su carta. Dura un'ora e mezza.</p>
  <p>Il quiz è composto da 30 domande con quattro opzioni ciascuna, per un'ora di tempo, senza penalità per le risposte errate: alcune domande sono teoriche, altre richiedono semplici calcoli, e quelle sulla rappresentazione digitale dell'informazione chiedono di applicare le tecniche viste a lezione e nelle esercitazioni facoltative. Si svolge sull'e-learning, dai computer dell'aula: non si possono usare computer propri. Per ovvie ragioni non è possibile avere l'elenco delle domande prima o dopo la prova, ma è possibile richiedere un ricevimento per conoscere gli argomenti sui quali si sono fatti più errori. Per la parte di calcolo c'è un <a href="{{ '/teaching/courses/fondamenti-di-informatica/esercizi/' | relative_url }}">generatore di esercizi sulla rappresentazione digitale dell'informazione</a>, che propone quesiti sempre nuovi.</p>
  <p>Il diagramma di flusso si disegna in trenta minuti sul foglio della traccia e deve descrivere un algoritmo che risolve il problema proposto. Per esercitarsi ci sono le <a href="{{ c.links.archive_1 }}">tracce dei diagrammi di flusso assegnati in passato</a>.</p>
  <p>Il voto del quiz è il numero di risposte esatte, e siccome le domande sono trenta e gli errori non tolgono punti il conteggio è già un voto in trentesimi. Anche il diagramma di flusso è valutato in trentesimi. Il voto della prova è la media dei due, e la prova è superata con almeno 18.</p>
  <p>La consegna del quiz è automatica allo scadere del tempo, ma conviene attivare la consegna manualmente, qualche minuto prima, per evitare che un problema tecnico dell'ultimo momento comprometta la prova. Il diagramma di flusso va consegnato sul foglio della traccia. Qualunque altro foglio usato per la brutta copia non va consegnato: se lo si consegna, non viene valutato.</p>
  <p>Prima del giorno della prova occorre verificare il proprio accesso all'e-learning. Chi non riesce a fare il login deve risolvere il problema prima, non in aula.</p>
  <p>Si possono portare solo una penna, una matita, una gomma e un righello. Appunti, libri, dispositivi elettronici e calcolatrici non sono ammessi. Il cellulare si può usare solo per l'autenticazione a due fattori al momento del login; subito dopo va appoggiato sopra il computer e non si può più toccare fino alla fine della prova. Smartwatch e altri dispositivi smart indossabili sono vietati in aula: chi li ha con sé li appoggia sopra il computer insieme al cellulare.</p>
  <p class="faq-warning">Durante la prova è vietato parlare o comunicare con altri studenti e, durante il quiz, aprire qualunque pagina web che non sia quella dell'e-learning necessaria a svolgere il test. Chi non rispetta le regole viene escluso dalla prova; chi viene sorpreso ad aprire altre pagine o a usare strumenti di intelligenza artificiale vede la prova annullata e non può sostenerla la volta successiva in cui viene svolta.</p>
  <p>L'iscrizione alla prova è obbligatoria e si fa con un modulo Google pubblicato sulla chat dell'anno accademico in corso, entro la scadenza indicata: chi non si iscrive entro quel termine non può sostenere la prova. La prova si svolge in più turni e la suddivisione precisa viene comunicata un paio di giorni prima. Chi ha bisogno di cambiare turno deve accordarsi per uno scambio con un altro studente: la comunicazione al Prof. Longo va fatta da entrambi, sulla chat WhatsApp. Fuori da questa procedura i cambi non vengono concessi. Conviene arrivare almeno dieci minuti prima del proprio turno.</p>
  <p>Gli studenti che hanno una certificazione che prevede misure compensative o dispensative possono scrivere al Prof. Longo prima della prova: si concorda insieme cosa serve, dal tempo aggiuntivo agli strumenti di supporto. Quanto viene comunicato resta tra lo studente e il Prof. Longo.</p>
</details>

<details class="faq-item" id="prep-2">
  <summary><h2>Cosa devo sapere prima di sostenere la seconda prova?</h2></summary>
  <p>La prova consiste in una serie di problemi da risolvere progettando e implementando in C dei semplici algoritmi. Dura due ore e si svolge al calcolatore.</p>
  <p>Gli esercizi sono sei, ognuno in un file <code>.c</code> a sé. Ogni file contiene il testo del problema, un esempio con i dati in ingresso e il risultato atteso, e lo scheletro del programma già scritto: le direttive, il <code>main</code> e a volte le variabili con il loro commento. Si completa solo la parte delimitata dai commenti che la segnalano; il resto del codice non va modificato. I file si scaricano dall'e-learning all'inizio della prova e vanno ricaricati lì alla fine.</p>
  <p>Gli argomenti seguono l'ordine del programma: selezione e cicli, cicli con array, array di strutture, e poi le funzioni, con il passaggio per valore, il passaggio di un array e il passaggio per riferimento.</p>
  <p>Il voto della prova dipende da quanti dei sei esercizi vengono risolti e dalla qualità delle soluzioni. La prova è superata con almeno 18.</p>
  <p>Per esercitarsi ci sono le <a href="{{ c.links.archive_2 }}">prove e le esercitazioni assegnate in passato</a>.</p>
  <p>Per tutto il resto valgono le <a href="#prep-1">stesse regole della prima prova</a>: iscrizione, turni, prerequisiti tecnici, materiale consentito, divieti e misure compensative.</p>
</details>

{% include faq-toggle.html %}
