---
layout: page
lang: it
title: Fondamenti di Informatica
permalink: /teaching/courses/fondamenti-di-informatica/
course_id: fondamenti-di-informatica
---

{% assign c = site.data.teaching | where: "id", page.course_id | first %}
{% include course-header.html %}

<details class="faq-item" id="topics">
  <summary><h2>Di cosa parla il corso?</h2></summary>
  <p>Di come si rappresenta ed elabora l'informazione in un calcolatore e di come si programma in C. Il modulo A parte dal sistema binario, dall'architettura di Von Neumann e dagli algoritmi per arrivare ai costrutti del linguaggio C, agli array e ai puntatori; il modulo B affronta ricorsione, complessità computazionale, algoritmi di ricerca e ordinamento e le strutture dati elementari: liste, pile e code.</p>
  <p>Il programma ufficiale si trova sulla <a href="{{ c.links.catalogue }}">pagina del corso nel catalogo di Ateneo</a>, con una scheda per ciascuno dei due moduli.</p>
</details>

<details class="faq-item" id="material">
  <summary><h2>Dove trovo il materiale didattico?</h2></summary>
  <p>Il materiale più aggiornato si trova sul sistema di e-learning di Ateneo. Conviene fare sempre riferimento all'ultimo anno accademico, che in questo momento è il <a href="{{ c.links.elearning }}">2026/2027</a>. Per accedere ai file è necessario iscriversi al corso.</p>
  <p>Il collegamento porta a una pagina di Ingegneria Biomedica: non è un errore, l'insegnamento è incardinato su quel corso di laurea.</p>
</details>

<details class="faq-item" id="contact">
  <summary><h2>Come contatto il professore e dove trovo gli avvisi?</h2></summary>
  <p>Il Prof. Longo è raggiungibile all'indirizzo <a href="mailto:francesco.longo@unime.it">francesco.longo@unime.it</a>, su WhatsApp o su Teams in qualunque momento: gli studenti non disturbano mai.</p>
  <p>Il ricevimento in presenza è il martedì e il giovedì dalle 15.00 alle 16.00, al Dipartimento di Ingegneria, blocco B, settimo piano, stanza 743. È bene avvisare prima con una mail o un messaggio, per avere conferma che il Prof. Longo sia presente.</p>
  <p>Gli avvisi dell'ultimo minuto passano dalla chat WhatsApp di classe, usata dal Prof. Longo anche per condividere notizie dal Dipartimento e dall'Ateneo. Ne viene creata una nuova ogni anno accademico: il QR code per entrare si trova nel blocco di slide 0 del modulo A, sull'e-learning.</p>
</details>

<details class="faq-item" id="exam">
  <summary><h2>Com'è strutturato l'esame?</h2></summary>
  <p>Tre prove scritte e un orale.</p>
  <ul>
    <li><b>Prima prova scritta</b>, test a risposta multipla più un esercizio su carta. Argomenti: conoscere i principi di base dell'informatica, l'architettura dell'elaboratore, la rappresentazione digitale dell'informazione e i concetti di base dei linguaggi, ovvero tutto il programma fino all'introduzione al linguaggio C inclusa (modulo A, blocchi da 1 a 5).</li>
    <li><b>Seconda prova scritta</b>, prova di programmazione di base al calcolatore. Argomenti: conoscere i concetti di base del linguaggio C, variabili e I/O di base, espressioni e operatori, strutture di controllo, array e stringhe, puntatori, tipi strutturati, funzioni e file, ovvero tutta la parte sul C fino alla fine del primo semestre (modulo A, blocchi da 6 a 13).</li>
    <li><b>Terza prova scritta</b>, prova di programmazione avanzata al calcolatore. Argomenti: saper implementare, date le specifiche, un software che svolge un compito ben preciso usando algoritmi e strutture dati semplici, ovvero la parte sul C fino a liste, pile e code incluse (modulo B, blocchi da 1 a 2).</li>
    <li><b>Prova progettuale</b>, facoltativa e permessa solo ai più meritevoli. Argomenti: l'implementazione di un software complesso date le sue specifiche, con algoritmi e strutture dati avanzate, ovvero la parte sul C fino a liste di liste e strutture dati più complesse (modulo B, blocco 3).</li>
    <li><b>Prova orale</b>. Argomenti: conoscere le strutture dati e gli algoritmi trattati a lezione e saperli implementare in C, ovvero l'ultima parte del programma, dalla ricorsione fino agli alberi (modulo B, blocchi da 4 a 9). Si sostiene solo dopo aver superato tutte le prove scritte.</li>
  </ul>
  <p>Il voto dell'esame è la media dei voti delle tre prove scritte e della prova orale.</p>
  <p>La prova progettuale resta fuori da questa media. Chi la sostiene può ottenere un voto più alto di quello che la media da sola darebbe, e ha più probabilità di arrivare alla lode. Non può invece abbassare il voto.</p>
  <p>Durante il primo semestre si svolgono due prove in itinere, corrispondenti alla prima e alla seconda prova scritta. Valgono esattamente un anno, fino alla corrispondente prova in itinere dell'anno successivo: per gli studenti in corso, fino all'appello di novembre incluso.</p>
  <p>Se le prove in itinere non vengono sostenute o non vengono superate, a ogni appello è possibile ripetere la prima e la seconda prova scritta, sostenere la terza prova scritta e sostenere la prova orale, quest'ultima solo dopo aver superato tutte le prove scritte.</p>
  <p>I testi delle prove precedenti sono raccolti per prova: <a href="{{ c.links.archive_1 }}">prima</a>, <a href="{{ c.links.archive_2 }}">seconda</a> e <a href="{{ c.links.archive_3 }}">terza</a>.</p>
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

<details class="faq-item" id="prep-3">
  <summary><h2>Cosa devo sapere prima di sostenere la terza prova?</h2></summary>
  <p>La prova consiste in un sistema software da completare in linguaggio C. Dura tre ore e si svolge al calcolatore.</p>
  <p>Il sistema è realizzato con il paradigma dei Tipi di Dato Astratto ed è composto da diversi file <code>.h</code> e <code>.c</code>, più un <code>main.c</code>. Quanto è già pronto cambia da un appello all'altro: a volte il sistema compila e funziona, e va esteso o corretto, a volte alcune funzioni sono stub da riempire, a volte un intero ADT è da scrivere partendo dalla sua sola interfaccia. I file dichiarati completi non si modificano e le interfacce nei file <code>.h</code> restano come sono. I file si scaricano dall'e-learning all'inizio della prova e vanno ricaricati lì alla fine.</p>
  <p>Il codice deve rispettare alcuni vincoli, gli stessi a ogni appello: il paradigma a puntatore opaco, con la definizione della struct nel file <code>.c</code> e, nel <code>.h</code>, il tipo e i prototipi; i file <code>.h</code> non si modificano; niente variabili globali; niente array, se non per le stringhe; nessuna operazione di ingresso o uscita nelle funzioni di interfaccia di un ADT, a parte quelle di stampa; tutta la memoria allocata dinamicamente va liberata. Le funzioni che restituiscono un <code>int</code> tornano 0 in caso di successo e 1 in caso di errore, salvo le eccezioni indicate nel testo della prova.</p>
  <p>Il voto della prova dipende da quanti punti della traccia vengono svolti e dalla qualità dello svolgimento. La prova è superata con almeno 18.</p>
  <p>Per esercitarsi ci sono le <a href="{{ c.links.archive_3 }}">prove assegnate in passato</a>, con i loro file di partenza.</p>
  <p>Per tutto il resto valgono le <a href="#prep-1">stesse regole della prima prova</a>: iscrizione, turni, prerequisiti tecnici, materiale consentito, divieti e misure compensative.</p>
</details>

<details class="faq-item" id="prep-oral">
  <summary><h2>Cosa devo sapere prima di sostenere la prova orale?</h2></summary>
  <p>La prova orale consiste in una serie di domande sugli algoritmi e sulle strutture dati trattati durante la seconda parte del modulo B: ricorsione, calcolo della complessità, algoritmi di ricerca e di ordinamento, grafi, alberi.</p>
  <p>Allo studente si chiede di conoscere i principi su cui quegli algoritmi e quelle strutture dati si fondano, di saperne spiegare il funzionamento, di saperne descrivere la complessità computazionale e di fornirne un'implementazione in linguaggio C, scritta su carta durante il colloquio.</p>
  <p>La prova orale si sostiene soltanto dopo aver superato tutte le prove scritte.</p>
</details>

{% include faq-toggle.html %}
