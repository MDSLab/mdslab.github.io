# Testi dei due modelli. L'italiano serve alla triennale, l'inglese alla magistrale.

IT = dict(
    lingua="it",
    nome_frontespizio="tesi-triennale-frontespizio",
    nome_modello="tesi-triennale-modello",
    cartella_latex="latex-triennale",
    ateneo="UNIVERSITÀ DEGLI STUDI DI MESSINA", dipartimento="DIPARTIMENTO DI INGEGNERIA",
    corso="Corso di Laurea in ……………………………………………",
    titolo="Titolo della tesi",
    tesi_di="Tesi di Laurea di:",
    relatore="Relatore:", correlatore="",
    prof="Chiar.mo Prof. Francesco Longo", prof2="",
    candidato="Nome Cognome", anno="ANNO ACCADEMICO 20…/20…",
    indice="Indice", elenco_fig="Elenco delle figure", elenco_tab="Elenco delle tabelle",
    abstract="Abstract", bibliografia="Bibliografia",
    parola_capitolo="Capitolo",
    cap=["Introduzione", "Background", "Il lavoro svolto", "Conclusioni"],
    sugg_cap=["", "(modifica il titolo come ti piace di più)",
              "(modifica il titolo come reputi più descrittivo del tuo lavoro specifico)", ""],
    sez=["Il contesto", "Obiettivo della tesi", "Struttura della tesi",
         "Titolo della prima sezione", "Titolo della seconda sezione",
         "Architettura del sistema", "Sviluppo software", "Misure e risultati"],
    sottosez="Titolo della sottosezione",
    sottosottosez="Titolo della sotto-sottosezione",

    g_ai="Nota valida per tutta la tesi: puoi usare gli strumenti di intelligenza artificiale per "
         "migliorare la forma, la chiarezza e la correttezza della lingua, non per generare "
         "contenuti, risultati o argomentazioni che non sapresti spiegare e difendere.",
    g_grigi="Nota valida per tutta la tesi: elimina tutti i suggerimenti in grigio nella versione "
            "finale della tua tesi.",
    g_indice="Clic destro sull'indice e «Aggiorna campo» per ricostruirlo. Perché funzioni, i titoli "
             "dei capitoli devono usare gli stili Titolo 1, 2, 3 e 4: la numerazione viene da sé.",
    g_abstract="L'abstract deve essere lungo una pagina e descrivere brevemente il problema, che cosa "
               "è stato fatto e il risultato principale. Si scrive per ultimo, quando si sa che cosa "
               "si è ottenuto.",

    g_apertura="Ogni capitolo si apre con un paragrafo che ne annuncia il contenuto, fuori da "
               "qualunque sezione. Per esempio:",
    e_intro="In questo capitolo si introduce il contesto in cui il lavoro si colloca, si enuncia "
            "l'obiettivo della tesi e si descrive l'organizzazione dei capitoli che seguono.",
    g_contesto="Di cosa si parla in questa tesi e perché il problema esiste. Scrivilo pensando a "
               "qualcuno che conosce l'informatica ma non è esperto dell'argomento della tua tesi.",
    g_obiettivo="Che cosa ti sei proposto di fare. E soprattutto qual è il tuo contributo, cioè che "
                "cosa c'era prima e che cosa c'è adesso grazie al tuo lavoro. È la prima cosa che una "
                "commissione cerca ed è quella che gli studenti dimenticano più spesso.",
    g_struttura="La mappa: un paragrafo che dice cosa si trova in ciascun capitolo, così chi legge sa "
                "dove andare.",

    g_back1="Uno o più capitoli. Il criterio per decidere cosa mettere in questi capitoli è questo: "
            "immagina che un collega debba continuare il tuo lavoro e debba leggere la tua tesi per "
            "farlo. Che cosa deve conoscere e studiare per capire a fondo quello che hai fatto e come "
            "proseguirlo? Ecco quello che va in questi capitoli.",
    e_back="In questo capitolo si richiamano le nozioni necessarie a seguire il resto del lavoro: la "
           "tecnologia X, il protocollo Y e le tecniche con cui in letteratura si affronta il problema Z.",
    g_organizzazione="Ogni capitolo può essere organizzato in più sezioni, con più sottosezioni e "
                     "sotto-sottosezioni ciascuna.",
    g_sez="Anche le sezioni si aprono annunciando il proprio contenuto, con una frase sola. Per esempio:",
    e_sez="Questa sezione descrive la tecnologia X, a partire dal modello di esecuzione per arrivare ai "
          "limiti che ne derivano.",
    g_cite="Questo è anche il capitolo in cui compaiono quasi tutte le fonti. Si citano con il numero "
           "fra parentesi quadre, a fine periodo prima del punto. Un possibile esempio è il seguente:",
    e_cite="La migrazione di container nel fog computing è stata studiata confrontando le tecniche "
           "cold, pre-copy e post-copy [1]. Una trattazione sistematica degli algoritmi impiegati si "
           "trova in [2], mentre la documentazione ufficiale del runtime descrive l'interfaccia "
           "utilizzata [3].",
    g_sottosez="Si scende di livello quando una sezione contiene due o più argomenti che meritano un "
               "titolo proprio. Se ce n'è uno solo, la sottosezione non serve.",
    g_sottosottosez="Terzo e ultimo livello. Più in basso di così la numerazione diventa illeggibile: "
                    "se serve, conviene ripensare l'organizzazione del capitolo.",
    g_fig="Ogni figura va richiamata nel testo: una figura che non viene mai citata è decorazione. La "
          "didascalia sta sotto la figura. Un possibile esempio è il seguente:",

    e_fig="L'architettura complessiva del sistema è rappresentata in Figura 1.",
    g_lst="Anche i listati vanno richiamati nel testo: un listato che non viene mai citato è "
          "decorazione. La didascalia sta sotto il listato. Un possibile esempio è il seguente:",
    e_lst="La funzione che calcola la somma è riportata nel Listato 1.",
    g_tab="Anche le tabelle vanno richiamate nel testo: una tabella che non viene mai citata è "
          "decorazione. La didascalia sta sopra la tabella. Un possibile esempio è il seguente:",
    e_tab="I tempi misurati nelle due configurazioni sono riportati in Tabella 1.",
    g_ic="Quando i risultati vengono da misure ripetibili, fai un numero adeguato di repliche e "
         "riporta anche la variabilità, per esempio la deviazione standard o gli intervalli di "
         "confidenza. Una media senza un'indicazione della variabilità non dice quanto ci si possa "
         "fidare del confronto.",
    g_graf="Un grafico è una figura a tutti gli effetti, quindi anche lui va richiamato nel testo e "
           "ha la didascalia sotto. Un possibile esempio è il seguente:",
    e_graf="L'andamento del tempo di risposta al crescere del carico è riportato in Figura 2, dove "
           "le barre verticali sono gli intervalli di confidenza al 95%.",
    cap_graf=": Tempo medio di risposta al crescere del carico, con intervalli di confidenza al 95%.",
    g_lav1="Uno o più capitoli, il cuore della tesi. Spiega il tuo lavoro nel dettaglio: l'architettura "
           "del sistema, del software o dell'algoritmo su cui hai lavorato, e le scelte che hai fatto "
           "con le loro ragioni.",
    e_lav="In questo capitolo si presenta l'architettura del sistema realizzato, se ne discutono le "
          "scelte implementative e si riportano le misure sperimentali raccolte.",
    g_lav2="Inserisci solo i listati significativi e spiegane le parti che contano, quelle in cui si "
           "vede una scelta implementativa. Non incollare lunghe porzioni di codice: scegli quelle "
           "che aiutano a capire il lavoro svolto.",
    g_lav3="Metti molte figure: pensa fin d'ora a come farai la presentazione il giorno della laurea, e disegna quello che "
           "spiegherai a voce. Per l'architettura e il comportamento sono utili i diagrammi UML più "
           "comuni, activity diagram, sequence diagram, class diagram.",
    g_misure="Riporta tutte le misure sperimentali che sei riuscito a fare e le osservazioni che se "
             "ne possono trarre sull'efficienza e sulle prestazioni.",

    g_apertura_ultimo="Anche l'ultimo capitolo si apre annunciando il proprio contenuto.",
    e_concl="In questo capitolo si riassumono i risultati ottenuti, se ne discutono i limiti e si "
            "indicano le direzioni in cui il lavoro può proseguire.",
    g_concl="Le conclusioni non introducono nuovi risultati né nuove informazioni tecniche: "
            "interpretano e sintetizzano quello che i capitoli precedenti hanno già presentato. "
            "Riassumi brevemente i risultati ottenuti. Dichiara anche i limiti del lavoro: una tesi "
            "che li riconosce è più credibile, non meno. Chiudi con i possibili sviluppi futuri, cioè "
            "da dove ripartirebbe quel collega.",
    g_bib="I riferimenti si elencano nell'ordine in cui compaiono nel testo e si numerano: il numero "
          "è quello con cui li hai citati fra parentesi quadre. Lo stile è IEEE, quello degli esempi "
          "che seguono — un articolo, un libro e una pagina web — e vale per tutti i riferimenti, "
          "senza eccezioni. Per raccogliere i dati il modo più rapido è il pulsante «Cita» di Google "
          "Scholar, che però propone solo MLA, APA, Chicago, Harvard e Vancouver: da lì prendi i "
          "dati, la forma la dai tu seguendo gli esempi.",

    g_dedica="Questa pagina è per la dedica. Se non la vuoi, cancellala.",
    appendice="Appendice", titolo_appendice="Titolo dell'appendice",
    g_app1="Le appendici servono a togliere dal corpo della tesi quello che lo appesantirebbe senza "
           "aggiungere niente al discorso: la procedura di installazione di un ambiente, la "
           "configurazione di una scheda, le tabelle complete dei dati di cui nel capitolo hai "
           "mostrato solo il riassunto, il codice che serve a riprodurre il lavoro ma che non "
           "contiene nessuna decisione interessante.",
    g_app2="Il criterio è lo stesso di un listato: se una cosa serve a chi vuole rifare quello che "
           "hai fatto, ma a chi legge per capire il lavoro fa solo perdere il filo, va in appendice.",
    g_app3="Si numerano con le lettere e compaiono nell'indice. Come le figure, vanno richiamate nel "
           "testo: un'appendice che nessuno cita non la legge nessuno. Un possibile esempio è il "
           "seguente:",
    e_app="La procedura completa di installazione dell'ambiente di sviluppo è riportata in Appendice A.",
    g_app4="Se non hai niente da metterci, cancella questa parte.",
    fig="Figura", tab="Tabella", lst="Listato",
    cap_fig=": Didascalia della figura.", cap_tab=": Didascalia della tabella.",
    cap_lst=": Didascalia del listato.",
    tabella=[["Configurazione", "Tempo medio (ms)", "Deviazione standard"],
             ["A", "12,4", "0,8"], ["B", "31,7", "2,1"]],
    bib=["[1] A. Autore, B. Coautore, «Titolo dell'articolo», Nome della rivista o della conferenza, "
         "vol. 12, n. 3, pp. 45-58, 2024.",
         "[2] C. Autore, Titolo del libro, 2ª ed. Città: Editore, 2023.",
         "[3] D. Organizzazione, «Titolo della pagina o della documentazione», "
         "https://esempio.org/pagina (consultato il 4 ottobre 2026)."],
)

EN = dict(
    lingua="en",
    nome_frontespizio="masters-thesis-title-page",
    nome_modello="masters-thesis-template",
    cartella_latex="latex-magistrale",
    ateneo="UNIVERSITY OF MESSINA", dipartimento="DEPARTMENT OF ENGINEERING",
    corso="Master's Degree in ……………………………………………",
    titolo="Title of the thesis",
    tesi_di="Candidate:",
    relatore="Supervisor:", correlatore="Co-supervisor:",
    prof="Prof. Francesco Longo", prof2="Prof. Name Surname",
    candidato="Name Surname", anno="ACADEMIC YEAR 20…/20…",
    indice="Contents", elenco_fig="List of Figures", elenco_tab="List of Tables",
    abstract="Abstract", bibliografia="References",
    parola_capitolo="Chapter",
    cap=["Introduction", "Background", "The work carried out", "Conclusions"],
    sugg_cap=["", "(change the title as you prefer)",
              "(change the title to whatever best describes your own work)", ""],
    sez=["Context", "Goal of the thesis", "Structure of the thesis",
         "Title of the first section", "Title of the second section",
         "System architecture", "Software development", "Measurements and results"],
    sottosez="Title of the subsection",
    sottosottosez="Title of the sub-subsection",

    g_ai="Note for the whole thesis: you may use artificial intelligence tools to improve the form, "
         "the clarity and the correctness of the language, not to generate content, results or "
         "arguments that you would not be able to explain and defend.",
    g_grigi="Note for the whole thesis: delete all the grey guidance from the final version of your "
            "thesis.",
    g_indice="Right-click the table of contents and choose «Update field» to rebuild it. For this to "
             "work, chapter titles must use the Heading 1, 2, 3 and 4 styles: the numbering follows.",
    g_abstract="The abstract must be one page long and briefly describe the problem, what was done "
               "and the main result. Write it last, when you know what you obtained. It is also the "
               "summary to be deposited at the Segreteria didattica, which forwards it to the members "
               "of the examination board.",

    g_apertura="Every chapter opens with a paragraph announcing its content, outside any section. "
               "A possible example is the following:",
    e_intro="This chapter introduces the context in which the work is placed, states the goal of the "
            "thesis and describes how the remaining chapters are organised.",
    g_contesto="What this thesis is about and why the problem exists. Write it thinking of someone "
               "who knows computer engineering but is not an expert in the subject of your thesis.",
    g_obiettivo="What you set out to do. And above all what your contribution is, that is, what existed "
                "before and what exists now thanks to your work. It is the first thing an examination "
                "board looks for and the one students most often leave out.",
    g_struttura="The map: a paragraph saying what each chapter contains, so the reader knows where to go.",

    g_back1="One or more chapters. The criterion for deciding what belongs in these chapters is this: "
            "imagine a colleague has to continue your work and must read your thesis to do so. What "
            "do they need to know and study in order to understand what you did and how to carry it "
            "on? That is what goes in these chapters.",
    e_back="This chapter recalls the notions needed to follow the rest of the work: technology X, "
           "protocol Y and the techniques with which the literature addresses problem Z.",
    g_organizzazione="Each chapter can be organised into several sections, each with several "
                     "subsections and sub-subsections.",
    g_sez="Sections, too, open by announcing their own content, in a single sentence. A possible example is the following:",
    e_sez="This section describes technology X, from its execution model to the limitations that "
          "follow from it.",
    g_cite="This is also the chapter where almost all the sources appear. They are cited with a number "
           "in square brackets, at the end of the sentence before the full stop. A possible example is "
           "the following:",
    e_cite="Container migration in fog computing has been studied by comparing the cold, pre-copy and "
           "post-copy techniques [1]. A systematic treatment of the algorithms involved can be found "
           "in [2], while the official runtime documentation describes the interface used here [3].",
    g_sottosez="You go one level down when a section contains two or more topics that deserve a heading "
               "of their own. If there is only one, the subsection is not needed.",
    g_sottosottosez="Third and last level. Any deeper and the numbering becomes unreadable: if you need "
                    "it, it is better to rethink how the chapter is organised.",
    g_fig="Every figure must be referred to in the text: a figure that is never cited is decoration. "
          "The caption goes below the figure. A possible example is the following:",

    e_fig="The overall architecture of the system is shown in Figure 1.",
    g_lst="Listings, too, must be referred to in the text: a listing that is never cited is "
          "decoration. The caption goes below the listing. A possible example is the following:",
    e_lst="The function that computes the sum is shown in Listing 1.",
    g_tab="Tables, too, must be referred to in the text: a table that is never cited is decoration. "
          "The caption goes above the table. A possible example is the following:",
    e_tab="The times measured in the two configurations are reported in Table 1.",
    g_ic="When the results come from repeatable measurements, run an adequate number of repetitions "
         "and report the variability as well, for instance the standard deviation or the confidence "
         "intervals. A mean with no indication of its variability says nothing about how far the "
         "comparison can be trusted.",
    g_graf="A chart is a figure to all intents and purposes, so it too must be referred to in the "
           "text and has its caption below. A possible example is the following:",
    e_graf="The behaviour of the response time as the load grows is shown in Figure 2, where the "
           "vertical bars are the 95% confidence intervals.",
    cap_graf=": Mean response time as the load grows, with 95% confidence intervals.",
    g_lav1="One or more chapters, the core of the thesis. Explain your work in detail: the architecture "
           "of the system, software or algorithm you worked on, and the choices you made with their "
           "reasons.",
    e_lav="This chapter presents the architecture of the system that was built, discusses its "
          "implementation choices and reports the experimental measurements that were collected.",
    g_lav2="Include only the listings that matter and explain the parts that count, the ones where an "
           "implementation choice is visible. Do not paste long portions of code: pick the ones that "
           "help the reader understand the work.",
    g_lav3="Use many figures: think now about how you will give the presentation on the day of your graduation, and draw what you "
           "will explain out loud. For architecture and behaviour the most common UML diagrams are "
           "useful: activity, sequence and class diagrams.",
    g_misure="Report every experimental measurement you managed to take and the observations that can "
             "be drawn from them about the efficiency and the performance.",

    g_apertura_ultimo="The last chapter, too, opens by announcing its own content.",
    e_concl="This chapter summarises the results obtained, discusses their limitations and indicates "
            "the directions in which the work can be continued.",
    g_concl="The conclusions introduce no new results and no new technical information: they "
            "interpret and summarise what the previous chapters have already presented. Summarise "
            "your results briefly. State the limits of the work as well: a thesis that acknowledges "
            "them is more credible, not less. Close with possible future developments, that is, where "
            "that colleague would start from.",
    g_bib="References are listed in the order in which they appear in the text and numbered: the "
          "number is the one you used to cite them in square brackets. The style is IEEE, the one of "
          "the examples that follow — an article, a book and a web page — and it applies to every "
          "reference, with no exceptions. The quickest way to collect the data is the «Cite» button "
          "on Google Scholar, which however only offers MLA, APA, Chicago, Harvard and Vancouver: "
          "take the data from there, the form is up to you, following the examples.",

    g_dedica="This page is for the dedication. If you do not want one, delete it.",
    appendice="Appendix", titolo_appendice="Title of the appendix",
    g_app1="Appendices take out of the body of the thesis what would weigh it down without adding "
           "anything to the argument: the procedure for installing an environment, the "
           "configuration of a board, the complete data tables of which the chapter showed only the "
           "summary, the code needed to reproduce the work but holding no interesting decision.",
    g_app2="The criterion is the same as for a listing: if something is needed by whoever wants to "
           "redo what you did, but only makes the reader lose the thread, it belongs in an appendix.",
    g_app3="Appendices are lettered and appear in the table of contents. Like figures, they must be "
           "referred to in the text: an appendix nobody cites is an appendix nobody reads. A "
           "possible example is the following:",
    e_app="The complete procedure for installing the development environment is given in Appendix A.",
    g_app4="If you have nothing to put there, delete this part.",
    fig="Figure", tab="Table", lst="Listing",
    cap_fig=": Caption of the figure.", cap_tab=": Caption of the table.",
    cap_lst=": Caption of the listing.",
    tabella=[["Configuration", "Average time (ms)", "Standard deviation"],
             ["A", "12.4", "0.8"], ["B", "31.7", "2.1"]],
    bib=["[1] A. Author, B. Coauthor, \"Title of the article,\" Name of the journal or conference, "
         "vol. 12, no. 3, pp. 45-58, 2024.",
         "[2] C. Author, Title of the book, 2nd ed. City: Publisher, 2023.",
         "[3] D. Organisation, \"Title of the page or of the documentation,\" "
         "https://example.org/page (accessed 4 October 2026)."],
)
