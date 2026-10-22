import json
import os

languages_data = {
    "en": {
        "name": "English",
        "p1_title": "Top 10 Essential Verbs in English for Absolute Beginners (A0–A1)",
        "p2_title": "Top 10 Essential Verbs in English, Part 2 (CEFR A0–A1)",
        "p1_kicker": "ENGLISH CORE GUIDE — PART 1",
        "p2_kicker": "ENGLISH CORE GUIDE — PART 2",
        "p1_dek": "Master the 10 most high-frequency verbs in English: be, have, think, know, like, want/would like, go/be going to, can, eat, and drink with rich phrases and sentence frames.",
        "p2_dek": "Part 2 of the ultimate beginner guide to high-frequency English verbs (A0–A1): do/make, speak/talk/say/tell, look/watch/see, listen/hear, must/have to, take/give/get, live, wait, understand, and ask/answer.",
        "p1_intro": "Welcome to Part 1 of our essential guide to high-frequency English verbs for absolute beginners (A0–A1)! Mastering these core verbs will unlock over 80% of daily spoken output. Each verb includes practical usages, collocations, sentence frames, and key grammar notes.",
        "p2_intro": "Welcome to Part 2 of our English verb guide for A0–A1 learners! In this edition, we explore 10 vital action, perception, modality, and communication verb pairs and clusters with rich phrase examples.",
        "h_breakdown_p1": "Deep Dive: Top 10 English Verbs (Part 1)",
        "h_breakdown_p2": "Deep Dive: Top 10 English Verbs (Part 2)",
        "h_matrix": "Comparative Linguistics Matrix across 14 Languages",
        "h_family": "Language Family Nuances & Grammatical Highlights",
        "h_practice": "Interactive Practice & Navigation",
        "matrix_intro": "Below is the comparative breakdown for core verbs across all 14 official languages:",
        "family_text": "• **Indo-European:** Features tense auxiliary verbs and person/number inflections.\n• **Turkic Family (Tatar, Bashkir, Chuvash):** Agglutinative suffix structures expressing tense and person without separate helper verbs.\n• **Kartvelian (Georgian):** Polypersonal verb agreement marking subject and indirect/direct objects.",
        "practice_text": "📌 Explore all 14 language articles in the COSYmagazine hub or test your knowledge in [COSYpractice](https://cosylanguages.github.io/COSYpractice/) and view full verb tables in [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. To Be (am / is / are):** Identity, states, age, and location.\n  • *Usage & Frames:* 'I am a student', 'He is at home', 'They are ready', 'I am 25 years old'.\n  • *Useful Phrases:* 'be on time', 'be quiet', 'be right'.",

            "**2. To Have (have / has):** Possession, relationships, and bodily states.\n  • *Usage & Frames:* 'I have a car', 'She has a sister', 'I have a headache'.\n  • *Useful Phrases:* 'have breakfast', 'have a shower', 'have a good day'.",

            "**3. To Think:** Expressing opinions, belief, and mental processing.\n  • *Usage & Frames:* 'I think so', 'What do you think about this?', 'I think it is a great idea'.\n  • *Useful Phrases:* 'think twice', 'think about', 'think of'.",

            "**4. To Know:** Factual knowledge, familiarity, and skills.\n  • *Usage & Frames:* 'I know the answer', 'Do you know him?', 'I know how to drive'.\n  • *Useful Phrases:* 'let me know', 'as far as I know', 'you know'.",

            "**5. To Like:** Expressing preferences and personal taste.\n  • *Usage & Frames:* 'I like coffee', 'She likes reading', 'Do you like sports?'.\n  • *Useful Phrases:* 'like very much', 'would like', 'look like'.",

            "**6. To Want / Would Like:** Desires, intentions, and polite requests.\n  • *Usage & Frames:* 'I want some water', 'I would like a cup of tea, please', 'Where do you want to go?'.\n  • *Useful Phrases:* 'want to learn', 'would like to order', 'if you want'.",

            "**7. To Go / Be Going To:** Movement, direction, and future intentions.\n  • *Usage & Frames:* 'I go to work by bus', 'She goes home', 'We are going to visit London next week'.\n  • *Useful Phrases:* 'go home', 'go shopping', 'go on foot', 'be going to eat'.",

            "**8. To Can (Modal):** Ability, possibility, and polite permission.\n  • *Usage & Frames:* 'I can speak English', 'Can you help me?', 'You can sit here'.\n  • *Useful Phrases:* 'can I have...', 'as fast as I can', 'can do'.",

            "**9. To Eat:** Meals, food consumption, and dining out.\n  • *Usage & Frames:* 'I eat fruit every morning', 'What do you want to eat?', 'Let's eat out tonight'.\n  • *Useful Phrases:* 'eat healthy', 'eat out', 'something to eat'.",

            "**10. To Drink:** Beverages, hydration, and social drinking.\n  • *Usage & Frames:* 'I drink water', 'Would you like something to drink?', 'He drinks coffee with milk'.\n  • *Useful Phrases:* 'drink water', 'a hot drink', 'something to drink'."
        ],
        "p2_items": [
            "**1. Do / Make:** Activity vs Creation.\n  • *Usage & Frames:* 'I do my homework' vs 'I make breakfast'.\n  • *Useful Phrases:* 'do business', 'do research' | 'make progress', 'make a mistake'.",

            "**2. Speak / Talk / Say / Tell:** Communication nuances.\n  • *Usage & Frames:* 'I speak English', 'Let's talk about it', 'Say hello to her', 'Tell me the truth'.\n  • *Useful Phrases:* 'speak fluently', 'talk with', 'say yes', 'tell a story'.",

            "**3. Look / Watch / See:** Visual perception & attention.\n  • *Usage & Frames:* 'Look at this picture', 'Watch a movie', 'I see a bird outside'.\n  • *Useful Phrases:* 'look for', 'look forward to', 'watch out', 'see you soon'.",

            "**4. Listen / Hear:** Auditory focus vs involuntary perception.\n  • *Usage & Frames:* 'Listen to music', 'Did you hear that noise?'.\n  • *Useful Phrases:* 'listen carefully', 'hear from', 'glad to hear that'.",

            "**5. Must / Have To:** Expressing necessity & obligation.\n  • *Usage & Frames:* 'I must study for the exam', 'We have to leave now'.\n  • *Useful Phrases:* 'must be', 'have to go', 'don't have to'.",

            "**6. Take / Give / Get:** Physical and abstract exchange.\n  • *Usage & Frames:* 'Take a coat', 'Give me a hand', 'Get a gift / Get home'.\n  • *Useful Phrases:* 'take care', 'give up', 'get tired', 'get ready'.",

            "**7. Live:** Dwelling, existence, and lifestyle.\n  • *Usage & Frames:* 'I live in London', 'She lives with her family'.\n  • *Useful Phrases:* 'live abroad', 'live well', 'live together'.",

            "**8. Wait:** Patience, expectation, and time.\n  • *Usage & Frames:* 'Wait for the bus', 'Can you wait a minute?'.\n  • *Useful Phrases:* 'wait for', 'wait in line', 'can't wait'.",

            "**9. Understand:** Comprehension and active listening.\n  • *Usage & Frames:* 'I understand the lesson', 'Do you understand what I mean?'.\n  • *Useful Phrases:* 'make yourself understood', 'as I understand', 'fully understand'.",

            "**10. Ask / Answer:** Questions and responses.\n  • *Usage & Frames:* 'Ask a question', 'Answer the phone / email'.\n  • *Useful Phrases:* 'ask for help', 'answer questions', 'ask a favour'."
        ]
    },
    "fr": {
        "name": "French",
        "p1_title": "Les 10 verbes essentiels en français pour débutants (CEFR A0–A1)",
        "p2_title": "Les 10 verbes essentiels en français, Partie 2 (CEFR A0–A1)",
        "p1_kicker": "GUIDE DU FRANÇAIS — PARTIE 1",
        "p2_kicker": "GUIDE DU FRANÇAIS — PARTIE 2",
        "p1_dek": "Maîtrisez les 10 verbes clés : être, avoir, penser, savoir/connaître, aimer, vouloir/aimerait, aller/aller + inf, pouvoir, manger et boire avec expressions et cadres de phrases.",
        "p2_dek": "Deuxième partie du guide des verbes français (A0–A1) : faire, parler/dire, regarder/voir, écouter/entendre, devoir/falloir, prendre/donner/recevoir, vivre/habiter, attendre, comprendre et demander/répondre.",
        "p1_intro": "Bienvenue dans la première partie du guide des verbes essentiels en français pour débutants (A0–A1) ! Retrouvez pour chaque verbe des structures pratiques, des collocations utiles et des règles de grammaire.",
        "p2_intro": "Bienvenue dans la deuxième partie du guide des verbes français pour le niveau A0–A1 ! Nous abordons 10 paires et groupes de verbes fondamentaux pour communiquer au quotidien.",
        "h_breakdown_p1": "Analyse détaillée : Les 10 verbes français (Partie 1)",
        "h_breakdown_p2": "Analyse détaillée : Les 10 verbes français (Partie 2)",
        "h_matrix": "Matrice linguistique comparative en 14 langues",
        "h_family": "Nuances familiales et caractéristiques grammaticales",
        "h_practice": "Exercices pratiques et navigation",
        "matrix_intro": "Voici le tableau comparatif des verbes essentiels à travers nos 14 langues officielles :",
        "family_text": "• **Indo-européen :** Utilise des auxiliaires temporels et des inflexions de personne/nombre.\n• **Famille turcique (tatar, bachkir, tchouvache) :** Structures à suffixes agglutinants exprimant le temps et la personne sans auxiliaires distincts.\n• **Kartvélien (géorgien) :** Accord verbal polypersonnel marquant le sujet et les objets.",
        "practice_text": "📌 Explorez les 14 articles dans le hub COSYmagazine ou testez vos connaissances sur [COSYpractice](https://cosylanguages.github.io/COSYpractice/) et consultez les tables de verbes sur [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Être (suis, es, est, sommes, êtes, sont) :** Identité, états et localisation.\n  • *Exemples :* 'Je suis étudiant', 'Il est à la maison', 'Nous sommes prêts'.\n  • *Expressions utiles :* 'être à l'heure', 'être d'accord', 'être en train de'.",

            "**2. Avoir (ai, as, a, avons, avez, ont) :** Possession, âge et sensations physiques.\n  • *Exemples :* 'J'ai une voiture', 'J'ai 25 ans', 'J'ai faim / j'ai soif'.\n  • *Expressions utiles :* 'avoir besoin de', 'avoir envie de', 'avoir peur'.",

            "**3. Penser :** Exprimer ses opinions et ses pensées.\n  • *Exemples :* 'Je pense que oui', 'Qu'en penses-tu ?', 'Je pense à toi'.\n  • *Expressions utiles :* 'penser à', 'penser de', 'bien penser'.",

            "**4. Savoir / Connaître :** Faits, compétences et connaissance des personnes/lieux.\n  • *Exemples :* 'Je sais parler français', 'Je connais cette ville', 'Tu sais où c'est ?'.\n  • *Expressions utiles :* 'savoir faire', 'faire savoir', 'connaître du monde'.",

            "**5. Aimer :** Préférences, goûts et affection.\n  • *Exemples :* 'J'aime le café', 'J'aime voyager', 'Il aime le sport'.\n  • *Expressions utiles :* 'aimer bien', 'aimer beaucoup', 'j'aimerais'.",

            "**6. Vouloir / Voudrais :** Désirs, projets et demandes polies.\n  • *Exemples :* 'Je veux un verre d'eau', 'Je voudrais réserver une table', 'Qu'est-ce que tu veux faire ?'.\n  • *Expressions utiles :* 'vouloir dire', 'si vous voulez', 'je voudrais bien'.",

            "**7. Aller / Futur Proche :** Deplacements et intentions futures.\n  • *Exemples :* 'Je vais au travail', 'Elle va à Paris', 'Nous allons manger'.\n  • *Expressions utiles :* 'comment ça va ?', 'y aller', 'aller à pied'.",

            "**8. Pouvoir :** Capacité, possibilité et permission.\n  • *Exemples :* 'Je peux vous aider ?', 'On peut utiliser ce livre', 'Tu peux venir ?'.\n  • *Expressions utiles :* 'pouvoir faire', 'si possible', 'autant que possible'.",

            "**9. Manger :** Repas et alimentation.\n  • *Exemples :* 'Je mange une pomme', 'Qu'est-ce qu'on mange ce soir ?', 'Manger au restaurant'.\n  • *Expressions utiles :* 'bon appétit', 'donner à manger', 'manger équilibré'.",

            "**10. Boire :** Boissons et rafraîchissements.\n  • *Exemples :* 'Je bois du thé', 'Voulez-vous quelque chose à boire ?', 'Il boit de l'eau'.\n  • *Expressions utiles :* 'avoir à boire', 'boire un coup', 'boire du café'."
        ],
        "p2_items": [
            "**1. Faire :** Activités quotidiennes et créations.\n  • *Exemples :* 'Faire du sport', 'Faire la cuisine', 'Faire les courses'.\n  • *Expressions utiles :* 'faire attention', 'faire du bien', 'faire plaisir'.",

            "**2. Parler / Dire :** Communication et récit.\n  • *Exemples :* 'Parler français', 'Dire la vérité', 'Dis-moi'.\n  • *Expressions utiles :* 'parler de', 'dire bonjour', 'pour ainsi dire'.",

            "**3. Regarder / Voir :** Regard attentif et perception visuelle.\n  • *Exemples :* 'Regarder un film', 'Je vois un oiseau'.\n  • *Expressions utiles :* 'regarder la télé', 'voyons voir', 'à voir'.",

            "**4. Écouter / Entendre :** Écoute active vs perception auditive.\n  • *Exemples :* 'Écouter de la musique', 'J'entends du bruit'.\n  • *Expressions utiles :* 'écouter attentivement', 'entendre parler de'.",

            "**5. Devoir / Falloir :** Obligation et nécessité.\n  • *Exemples :* 'Je dois étudier', 'Il faut partir maintenant'.\n  • *Expressions utiles :* 'devoir faire', 'comme il faut', 'il faut absolument'.",

            "**6. Prendre / Donner / Obtenir :** Échanges physiques et abstraits.\n  • *Exemples :* 'Prendre le bus', 'Donner un cadeau', 'Obtenir un rendez-vous'.\n  • *Expressions utiles :* 'prendre soin', 'donner rendez-vous', 'prendre son temps'.",

            "**7. Vivre / Habiter :** Résidence et mode de vie.\n  • *Exemples :* 'J'habite à Paris', 'Vivre en paix'.\n  • *Expressions utiles :* 'vivre à l'étranger', 'habiter près d'ici'.",

            "**8. Attendre :** Patience et attente.\n  • *Exemples :* 'Attendre le bus', 'Attendez une minute'.\n  • *Expressions utiles :* 'attendre avec impatience', 'en attendant'.",

            "**9. Comprendre :** Assimilation et compréhension.\n  • *Exemples :* 'Je comprends la leçon', 'Vous comprenez ?'.\n  • *Expressions utiles :* 'faire comprendre', 'bien comprendre'.",

            "**10. Demander / Répondre :** Questions, réponses et formules de politesse.\n  • *Exemples :* 'Demander une question / un service', 'Répondre au téléphone'.\n  • *Expressions utiles :* 'demander de l'aide', 'répondre vite'."
        ]
    },
    "it": {
        "name": "Italian",
        "p1_title": "I 10 verbi essenziali in italiano per principianti (CEFR A0–A1)",
        "p2_title": "I 10 verbi essenziali in italiano, Parte 2 (CEFR A0–A1)",
        "p1_kicker": "GUIDA ALL'ITALIANO — PARTE 1",
        "p2_kicker": "GUIDA ALL'ITALIANO — PARTE 2",
        "p1_dek": "Domina i 10 verbi chiave: essere, avere, pensare, sapere/conoscere, piacere, volere/vorrei, andare/stare per, potere, mangiare e bere con frasi ed esempi pratici.",
        "p2_dek": "La seconda parte della guida ai verbi italiani per principianti (A0–A1): fare, parlare/dire, guardare/vedere, ascoltare/sentire, dovere/bisognare, prendere/dare, vivere/abitare, aspettare, capire e chiedere/rispondere.",
        "p1_intro": "Benvenuti nella prima parte della guida ai verbi essenziali della lingua italiana per il livello A0–A1! Per ogni verbo troverai frasi utili, combinazioni frequenti e note grammaticali.",
        "p2_intro": "Benvenuti alla seconda parte della guida ai verbi italiani per il livello A0–A1! Scopriamo 10 nuovi gruppi di verbi fondamentali per comunicare ogni giorno.",
        "h_breakdown_p1": "Analisi approfondita: I 10 verbi italiani (Parte 1)",
        "h_breakdown_p2": "Analisi approfondita: I 10 verbi italiani (Parte 2)",
        "h_matrix": "Matrice comparativa tra 14 lingue",
        "h_family": "Sfumature linguistiche e aspetti grammaticali",
        "h_practice": "Esercizi pratici e navigazione",
        "matrix_intro": "Ecco la tabella comparativa dei verbi principali nelle 14 lingue ufficiali:",
        "family_text": "• **Indoeuropeo:** Utilizza ausiliari e flessioni di persona/numero.\n• **Famiglia turchica (tataro, baschiro, ciuvascio):** Strutture a suffissi agglutinanti per tempo e persona senza ausiliari separati.\n• **Kartvelico (georgiano):** Accordo verbale polipersonale che marca soggetto e oggetti.",
        "practice_text": "📌 Esplora tutti i 14 articoli nell'hub di COSYmagazine o metti alla prova le tue conoscenze su [COSYpractice](https://cosylanguages.github.io/COSYpractice/) e consulta le tabelle dei verbi su [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Essere:** Identità, stati, età e posizione.\n  • *Esempi:* 'Sono uno studente', 'Lui è a casa', 'Siamo pronti'.\n  • *Frasi utili:* 'essere in orario', 'essere d'accordo', 'essere felice'.",

            "**2. Avere:** Possesso, età e sensazioni fisiche.\n  • *Esempi:* 'Ho una macchina', 'Ho 25 anni', 'Ho fame / ho sete'.\n  • *Frasi utili:* 'avere bisogno di', 'avere voglia di', 'avere fretta'.",

            "**3. Pensare:** Esprimere opinioni e pensieri.\n  • *Esempi:* 'Penso di sì', 'Che cosa ne pensi?', 'Penso a te'.\n  • *Frasi utili:* 'pensare a', 'pensarci sopra', 'pensare bene'.",

            "**4. Sapere / Conoscere:** Fatti, abilità e familiarità.\n  • *Esempi:* 'So parlare italiano', 'Conosco questa città', 'Sai dov'è?'.\n  • *Frasi utili:* 'fai sapere', 'per quanto ne so', 'conoscere gente'.",

            "**5. Piacere:** Esprimere preferenze e gusti.\n  • *Esempi:* 'Mi piace il caffè', 'Mi piace viaggiare', 'Le piace lo sport'.\n  • *Frasi utili:* 'mi piace molto', 'mi piacerebbe', 'ti piace?'.",

            "**6. Volere / Vorrei:** Desideri e richieste cortesi.\n  • *Esempi:* 'Voglio un bicchiere d'acqua', 'Vorrei prenotare un tavolo', 'Cosa vuoi fare?'.\n  • *Frasi utili:* 'vorrei un caffè', 'se vuoi', 'voler dire'.",

            "**7. Andare / Stare per:** Movimento e intenzioni future.\n  • *Esempi:* 'Vado al lavoro', 'Lei va a Roma', 'Stiamo per mangiare'.\n  • *Frasi utili:* 'come va?', 'andare a piedi', 'andare in vacanza'.",

            "**8. Potere:** Capacità, possibilità e permesso.\n  • *Esempi:* 'Posso aiutarti?', 'Possiamo usare questo libro', 'Puoi venire?'.\n  • *Frasi utili:* 'se possibile', 'può darsi', 'fai come puoi'.",

            "**9. Mangiare:** Pasti e alimentazione.\n  • *Esempi:* 'Mangio una mela', 'Cosa mangiamo stasera?', 'Mangiare al ristorante'.\n  • *Frasi utili:* 'buon appetito', 'dare da mangiare', 'mangiare sano'.",

            "**10. Bere:** Bevande e idratazione.\n  • *Esempi:* 'Bevo un tè', 'Vuoi qualcosa da bere?', 'Lui beve acqua'.\n  • *Frasi utili:* 'qualcosa da bere', 'bere un caffè', 'bere alla salute'."
        ],
        "p2_items": [
            "**1. Fare:** Attività quotidiane e creazioni.\n  • *Esempi:* 'Fare la spesa', 'Fare colazione', 'Fare i compiti'.\n  • *Frasi utili:* 'fare attenzione', 'fare piacere', 'fare bella figura'.",

            "**2. Parlare / Dire:** Comunicazione e racconto.\n  • *Esempi:* 'Parlare italiano', 'Dire la verità', 'Dimmi'.\n  • *Frasi utili:* 'parlare di', 'dire di sì', 'per così dire'.",

            "**3. Guardare / Vedere:** Attenzione visiva e percezione.\n  • *Esempi:* 'Guardare un film', 'Vedo un uccello'.\n  • *Frasi utili:* 'guardare la TV', 'stare a vedere', 'ci vediamo'.",

            "**4. Ascoltare / Sentire:** Ascolto attivo e percezione uditiva.\n  • *Esempi:* 'Ascoltare musica', 'Sento un rumore'.\n  • *Frasi utili:* 'ascolta con attenzione', 'sentire parlare di'.",

            "**5. Dovere / Bisognare:** Obbligo e necessità.\n  • *Esempi:* 'Devo studiare', 'Bisogna partire ora'.\n  • *Frasi utili:* 'dovere fare', 'come si deve', 'bisogna stare attenti'.",

            "**6. Prendere / Dare / Ricevere:** Scambi fisici e astratti.\n  • *Esempi:* 'Prendere il treno', 'Dare un regalo', 'Ricevere una lettera'.\n  • *Frasi utili:* 'prendersi cura', 'dare un passaggio', 'prendere un caffè'.",

            "**7. Vivere / Abitare:** Residenza e stile di vita.\n  • *Esempi:* 'Abito a Milano', 'Vivere in pace'.\n  • *Frasi utili:* 'vivere all'estero', 'abitare vicino'.",

            "**8. Aspettare:** Pazienza e attesa.\n  • *Esempi:* 'Aspettare l'autobus', 'Aspetta un momento'.\n  • *Frasi utili:* 'non vedere l'ora', 'aspettare in fila'.",

            "**9. Capire:** Comprensione ed empatia.\n  • *Esempi:* 'Capisco la lezione', 'Capisci cosa intendo?'.\n  • *Frasi utili:* 'farsi capire', 'capisco benissimo'.",

            "**10. Chiedere / Rispondere:** Domande, risposte e cortesia.\n  • *Esempi:* 'Chiedere un'informazione', 'Rispondere al telefono'.\n  • *Frasi utili:* 'chiedere aiuto', 'rispondere subito'."
        ]
    },
    "es": {
        "name": "Spanish",
        "p1_title": "Los 10 verbos esenciales en español para principiantes (CEFR A0–A1)",
        "p2_title": "Los 10 verbos esenciales en español, Parte 2 (CEFR A0–A1)",
        "p1_kicker": "GUÍA DE ESPAÑOL — PARTE 1",
        "p2_kicker": "GUÍA DE ESPAÑOL — PARTE 2",
        "p1_dek": "Domina los 10 verbos clave: ser/estar, tener, pensar, saber/conocer, gustar, querer/gustaría, ir/ir a, poder, comer y beber con frases y cuadros de uso.",
        "p2_dek": "Segunda parte de la guía de verbos en español (A0–A1): hacer, hablar/decir, mirar/ver, escuchar/oír, tener que/deber, tomar/dar, vivir, esperar, entender y preguntar/responder.",
        "p1_intro": "¡Bienvenidos a la primera parte de la guía de verbos esenciales en español para el nivel A0–A1! Incluye frases útiles, colocaciones y consejos gramaticales para cada verbo.",
        "p2_intro": "¡Bienvenidos a la segunda parte de la guía de verbos en español para principiantes (A0–A1)! Presentamos 10 grupos de verbos clave para la comunicación diaria.",
        "h_breakdown_p1": "Análisis detallado: Los 10 verbos en español (Parte 1)",
        "h_breakdown_p2": "Análisis detallado: Los 10 verbos en español (Parte 2)",
        "h_matrix": "Matriz lingüística comparativa en 14 idiomas",
        "h_family": "Matices familiares y aspectos gramaticales",
        "h_practice": "Ejercicios prácticos y navegación",
        "matrix_intro": "A continuación se muestra el desglose comparativo de los verbos principales en los 14 idiomas oficiales:",
        "family_text": "• **Indoeuropeo:** Utiliza auxiliares de tiempo e inflexiones de persona/número.\n• **Familia turca (tártaro, bashkir, chuvash):** Estructuras de sufijos aglutinantes que expresan tiempo y persona sin auxiliares separados.\n• **Kartveliano (georgiano):** Concordancia verbal polipersonal para sujeto y objetos.",
        "practice_text": "📌 Explora los 14 artículos en el hub de COSYmagazine o pon a prueba tus conocimientos en [COSYpractice](https://cosylanguages.github.io/COSYpractice/) y consulta las tablas de verbos en [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Ser / Estar:** Identidad, estados, ubicación y características.\n  • *Ejemplos:* 'Soy estudiante', 'Estoy en casa', 'Estamos listos'.\n  • *Frases útiles:* 'estar a tiempo', 'estar de acuerdo', 'estar bien'.",

            "**2. Tener:** Posesión, edad y estados físicos.\n  • *Ejemplos:* 'Tengo un coche', 'Tengo 25 años', 'Tengo hambre / tengo sed'.\n  • *Frases útiles:* 'tener que', 'tener ganas de', 'tener prisa'.",

            "**3. Pensar:** Expresar opiniones y pensamientos.\n  • *Ejemplos:* 'Pienso que sí', '¿Qué piensas de esto?', 'Pienso en ti'.\n  • *Frases útiles:* 'pensar en', 'pensarlo bien', 'pensar que'.",

            "**4. Saber / Conocer:** Información, habilidades y familiaridad.\n  • *Ejemplos:* 'Sé hablar español', 'Conozco esta ciudad', '¿Sabes dónde está?'.\n  • *Frases útiles:* 'dar a conocer', 'que yo sepa', 'conocer gente'.",

            "**5. Gustar:** Expresar preferencias y gustos personales.\n  • *Ejemplos:* 'Me gusta el café', 'Me gusta viajar', 'Le gusta el deporte'.\n  • *Frases útiles:* 'me gusta mucho', 'me gustaría', '¿te gusta?'.",

            "**6. Querer / Me Gustaría:** Deseos, proyectos y peticiones corteses.\n  • *Ejemplos:* 'Quiero un vaso de agua', 'Me gustaría reservar una mesa', '¿Qué quieres hacer?'.\n  • *Frases útiles:* 'querer decir', 'si quieres', 'me gustaría pedir'.",

            "**7. Ir / Ir a + Infinitivo:** Movimiento e intenciones futuras.\n  • *Ejemplos:* 'Voy al trabajo en autobús', 'Ella va a Madrid', 'Vamos a comer'.\n  • *Frases útiles:* '¿cómo te va?', 'ir a pie', 'ir de compras'.",

            "**8. Poder:** Capacidad, posibilidad y permiso.\n  • *Ejemplos:* '¿Puedo ayudarte?', 'Podemos usar este libro', '¿Puedes venir?'.\n  • *Frases útiles:* 'si se puede', 'se puede pasar', 'lo más rápido que pueda'.",

            "**9. Comer:** Comidas y alimentación.\n  • *Ejemplos:* 'Como una manzana cada mañana', '¿Qué vamos a comer?', 'Comer en un restaurante'.\n  • *Frases útiles:* 'buen provecho', 'dar de comer', 'comer sano'.",

            "**10. Beber:** Bebidas e hidratación.\n  • *Ejemplos:* 'Bebo té', '¿Quieres algo de beber?', 'Él bebe agua'.\n  • *Frases útiles:* 'algo de beber', 'tomar un trago', 'beber café'."
        ],
        "p2_items": [
            "**1. Hacer:** Actividades cotidianas y creación.\n  • *Ejemplos:* 'Hacer los deberes', 'Hacer el desayuno', 'Hacer ejercicio'.\n  • *Frases útiles:* 'hacer falta', 'hacer el favor', 'hacer fotos'.",

            "**2. Hablar / Decir:** Comunicación y relatos.\n  • *Ejemplos:* 'Hablar español', 'Decir la verdad', 'Dime'.\n  • *Frases útiles:* 'hablar de', 'decir que sí', 'por decir algo'.",

            "**3. Mirar / Ver:** Atención visual y percepción.\n  • *Ejemplos:* 'Mirar una película', 'Veo un pájaro'.\n  • *Frases útiles:* 'mirar la televisión', 'a ver', 'nos vemos'.",

            "**4. Escuchar / Oír:** Atención auditiva vs percepción.\n  • *Ejemplos:* 'Escuchar música', 'Oigo un ruido'.\n  • *Frases útiles:* 'escuchar con atención', 'oír hablar de'.",

            "**5. Tener que / Deber:** Obligación y necesidad.\n  • *Ejemplos:* 'Tengo que estudiar', 'Debemos salir ya'.\n  • *Frases útiles:* 'tener que hacer', 'debería ser', 'hay que'.",

            "**6. Tomar / Dar / Conseguir:** Intercambios y obtención.\n  • *Ejemplos:* 'Tomar el autobús', 'Dar un regalo', 'Conseguir una cita'.\n  • *Frases útiles:* 'darse prisa', 'dar la mano', 'tomar un café'.",

            "**7. Vivir:** Residencia y estilo de vida.\n  • *Ejemplos:* 'Vivo en Madrid', 'Vivir bien'.\n  • *Frases útiles:* 'vivir en el extranjero', 'vivir juntos'.",

            "**8. Esperar:** Paciencia, espera y esperanza.\n  • *Ejemplos:* 'Esperar el autobús', 'Espere un momento'.\n  • *Frases útiles:* 'esperar que', 'hacer cola', 'no ver la hora'.",

            "**9. Entender / Comprender:** Comprensión.\n  • *Ejemplos:* 'Entiendo la lección', '¿Entiendes lo que digo?'.\n  • *Frases útiles:* 'hacerse entender', 'entiendo perfectamente'.",

            "**10. Preguntar / Responder:** Preguntas, respuestas y cortesía.\n  • *Ejemplos:* 'Hacer una pregunta', 'Responder al teléfono'.\n  • *Frases útiles:* 'pedir ayuda', 'responder rápido'."
        ]
    },
    "de": {
        "name": "German",
        "p1_title": "Die 10 wichtigsten Verben im Deutschen für Anfänger (CEFR A0–A1)",
        "p2_title": "Die 10 wichtigsten Verben im Deutschen, Teil 2 (CEFR A0–A1)",
        "p1_kicker": "DEUTSCHER VERBEN-LEITFADEN — TEIL 1",
        "p2_kicker": "DEUTSCHER VERBEN-LEITFADEN — TEIL 2",
        "p1_dek": "Meistern Sie die 10 wichtigsten Verben: sein, haben, denken, wissen/kennen, mögen/gefallen, wollen/möchte, gehen/werden, können, essen und trinken mit Sätzen und Tipps.",
        "p2_dek": "Der zweite Teil des Verben-Leitfadens für Anfänger (A0–A1): machen/tun, sprechen/sagen, schauen/sehen, hören, müssen/sollen, nehmen/geben, wohnen/leben, warten, verstehen und fragen/antworten.",
        "p1_intro": "Willkommen zum ersten Teil unseres Verben-Leitfadens für das Niveau A0–A1 im Deutschen! Zu jedem Verb finden Sie Beispielsätze, feste Wendungen und Grammatik-Tipps.",
        "p2_intro": "Willkommen zum zweiten Teil unseres Verben-Leitfadens für A0–A1! Hier behandeln wir 10 weitere hochfrequente Alltagsverben für Handlungen und Gespräche.",
        "h_breakdown_p1": "Detaillierte Analyse: Die 10 deutschen Verben (Teil 1)",
        "h_breakdown_p2": "Detaillierte Analyse: Die 10 deutschen Verben (Teil 2)",
        "h_matrix": "Sprachvergleichsmatrix über 14 Sprachen",
        "h_family": "Sprachfamilien & Grammatik-Highlights",
        "h_practice": "Interaktive Übungen und Navigation",
        "matrix_intro": "Nachfolgend finden Sie den vergleichenden Überblick über die wichtigsten Verben in allen 14 Amtssprachen:",
        "family_text": "• **Indogermanisch:** Verwendet Zeitform-Hilfsverben und Person/Numerus-Flexionen.\n• **Turksprachen (Tatarisch, Baschkirisch, Tschuwaschisch):** Agglutinative Suffixstrukturen für Tempus und Person ohne separate Hilfsverben.\n• **Kartwelisch (Georgisch):** Polypersonale Verbkongruenz zur Markierung von Subjekt und Objekten.",
        "practice_text": "📌 Entdecken Sie alle 14 Sprachartikel im COSYmagazine-Hub oder testen Sie Ihr Wissen auf [COSYpractice](https://cosylanguages.github.io/COSYpractice/) und nutzen Sie die Verb-Tabellen auf [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Sein:** Identität, Zustand, Alter und Ort.\n  • *Beispiele:* 'Ich bin Student', 'Er ist zu Hause', 'Wir sind fertig'.\n  • *Nützliche Phrasen:* 'pünktlich sein', 'einverstanden sein', '25 Jahre alt sein'.",

            "**2. Haben:** Besitz, Beziehungen und körperliche Zustände.\n  • *Beispiele:* 'Ich habe ein Auto', 'Sie hat eine Schwester', 'Ich habe Kopfschmerzen'.\n  • *Nützliche Phrasen:* 'Hunger/Durst haben', 'Zeit haben', 'Glück haben'.",

            "**3. Denken:** Meinungen und Denkvorgänge.\n  • *Beispiele:* 'Ich denke schon', 'Was denkst du darüber?', 'Ich denke an dich'.\n  • *Nützliche Phrasen:* 'denken an', 'nachdenken', 'meiner Meinung nach'.",

            "**4. Wissen / Kennen:** Faktenwissen vs Bekanntschaft.\n  • *Beispiele:* 'Ich weiß die Antwort', 'Ich kenne diese Stadt', 'Weißt du wo das ist?'.\n  • *Nützliche Phrasen:* 'Bescheid wissen', 'kennenlernen', 'soweit ich weiß'.",

            "**5. Mögen / Gefallen:** Vorlieben und Geschmack.\n  • *Beispiele:* 'Ich mag Kaffee', 'Das Buch gefällt mir', 'Magst du Sport?'.\n  • *Nützliche Phrasen:* 'sehr mögen', 'Gefallen finden', 'wie du magst'.",

            "**6. Wollen / Ich möchte:** Wünsche, Pläne und höfliche Bitten.\n  • *Beispiele:* 'Ich will Wasser trinken', 'Ich möchte einen Kaffee bitte', 'Was willst du machen?'.\n  • *Nützliche Phrasen:* 'möchte bestellen', 'wenn du willst', 'willkommen'.",

            "**7. Gehen / Werden:** Bewegung und Zukunftsvorhaben.\n  • *Beispiele:* 'Ich gehe zur Arbeit', 'Sie geht nach Hause', 'Wir werden morgen reisen'.\n  • *Nützliche Phrasen:* 'Wie geht's?', 'zu Fuß gehen', 'einkaufen gehen'.",

            "**8. Können:** Fähigkeit, Möglichkeit und Erlaubnis.\n  • *Beispiele:* 'Ich kann Deutsch sprechen', 'Kannst du mir helfen?', 'Man kann hier sitzen'.\n  • *Nützliche Phrasen:* 'kann sein', 'so gut ich kann', 'was kann ich tun?'.",

            "**9. Essen:** Mahlzeiten und Nahrung.\n  • *Beispiele:* 'Ich esse jeden Morgen Obst', 'Was wollen wir essen?', 'Im Restaurant essen'.\n  • *Nützliche Phrasen:* 'Guten Appetit!', 'gesund essen', 'etwas zu essen'.",

            "**10. Trinken:** Getränke und Flüssigkeit.\n  • *Beispiele:* 'Ich trinke Tee', 'Möchten Sie etwas trinken?', 'Er trinkt Wasser'.\n  • *Nützliche Phrasen:* 'etwas zu trinken', 'Kaffee trinken', 'Prost!'."
        ],
        "p2_items": [
            "**1. Machen / Tun:** Aktivitäten und Handlungen.\n  • *Beispiele:* 'Hausaufgaben machen', 'Was tust du?'.\n  • *Nützliche Phrasen:* 'Freude machen', 'Sinn machen', 'Nichts zu tun'.",

            "**2. Sprechen / Sagen:** Kommunikation.\n  • *Beispiele:* 'Deutsch sprechen', 'Die Wahrheit sagen', 'Sag mir Bescheid'.\n  • *Nützliche Phrasen:* 'sprechen über', 'Hallo sagen', 'sozusagen'.",

            "**3. Schauen / Sehen:** Visuelle Aufmerksamkeit.\n  • *Beispiele:* 'Fernsehen schauen', 'Ich sehe einen Vogel'.\n  • *Nützliche Phrasen:* 'Schau mal!', 'Ausschau halten', 'Bis später!'.",

            "**4. Hören:** Akustische Wahrnehmung.\n  • *Beispiele:* 'Musik hören', 'Ich höre ein Geräusch'.\n  • *Nützliche Phrasen:* 'zuhören', 'von jemandem hören'.",

            "**5. Müssen / Sollen:** Notwendigkeit und Pflicht.\n  • *Beispiele:* 'Ich muss lernen', 'Du sollst schlafen'.\n  • *Nützliche Phrasen:* 'muss sein', 'soll ich helfen?'.",

            "**6. Nehmen / Geben:** Austausch und Übergabe.\n  • *Beispiele:* 'Den Bus nehmen', 'Ein Geschenk geben', 'Bescheid bekommen'.\n  • *Nützliche Phrasen:* 'Rücksicht nehmen', 'Acht geben', 'Platz nehmen'.",

            "**7. Wohnen / Leben:** Wohnort und Lebensstil.\n  • *Beispiele:* 'Ich wohne in Berlin', 'Gut leben'.\n  • *Nützliche Phrasen:* 'im Ausland leben', 'zusammenwohnen'.",

            "**8. Warten:** Geduld und Erwartung.\n  • *Beispiele:* 'Auf den Bus warten', 'Warten Sie einen Moment'.\n  • *Nützliche Phrasen:* 'warten auf', 'kaum erwarten können'.",

            "**9. Verstehen:** Verständnis.\n  • *Beispiele:* 'Ich verstehe die Lektion', 'Verstehst du mich?'.\n  • *Nützliche Phrasen:* 'sich verstehen', 'vollkommen verstehen'.",

            "**10. Fragen / Antworten:** Fragen und Antworten.\n  • *Beispiele:* 'Eine Frage stellen', 'Auf die E-Mail antworten'.\n  • *Nützliche Phrasen:* 'um Hilfe fragen', 'schnell antworten'."
        ]
    },
    "ru": {
        "name": "Russian",
        "p1_title": "Топ-10 главных глаголов русского языка для начинающих (CEFR A0–A1)",
        "p2_title": "Топ-10 главных глаголов русского языка, Часть 2 (CEFR A0–A1)",
        "p1_kicker": "ГИД ПО РУССКОМУ ЯЗЫКУ — ЧАСТЬ 1",
        "p2_kicker": "ГИД ПО РУССКОМУ ЯЗЫКУ — ЧАСТЬ 2",
        "p1_dek": "Освойте 10 ключевых глаголов: быть, иметь/у меня есть, думать, знать, нравиться, хотеть/хотел бы, идти/ехать, мочь, есть и пить с примерами и фразами.",
        "p2_dek": "Вторая часть руководства по частотным глаголам русского языка (A0–A1): делать, говорить/сказать, смотреть/видеть, слушать/слышать, должен/надо, брать/давать, жить, ждать, понимать и спрашивать/отвечать.",
        "p1_intro": "Добро пожаловать в первую часть гида по ключевым глаголам русского языка для уровня A0–A1! Для каждого глагола приведены устойчивые выражения, речевые шаблоны и советы.",
        "p2_intro": "Добро пожаловать во вторую часть гида по русским глаголам для начинающих (A0–A1)! Мы разбираем еще 10 важных пар и групп глаголов действия, восприятия и общения.",
        "h_breakdown_p1": "Подробный разбор: Топ-10 русских глаголов (Часть 1)",
        "h_breakdown_p2": "Подробный разбор: Топ-10 русских глаголов (Часть 2)",
        "h_matrix": "Сравнительная лингвистическая матрица на 14 языках",
        "h_family": "Языковые семьи и грамматические особенности",
        "h_practice": "Практические упражнения и навигация",
        "matrix_intro": "Ниже представлен сравнительный разбор ключевых глаголов на всех 14 официальных языках:",
        "family_text": "• **Индоевропейская семья:** Использует вспомогательные глаголы времени и личные окончания.\n• **Тюркская семья (татарский, башкирский, чувашский):** Агглютинативные суффиксальные структуры для выражения времени и лица без отдельных вспомогательных слов.\n• **Картвельская семья (грузинский):** Полиперсональное спряжение для обозначения субъекта и объектов.",
        "practice_text": "📌 Изучите все 14 статей в хабе COSYmagazine, проверяйте свои знания в [COSYpractice](https://cosylanguages.github.io/COSYpractice/) и смотрите полные таблицы глаголов в [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Быть (есть, был, будет):** Наличие, состояние, возраст и местонахождение.\n  • *Примеры:* 'Я студент', 'Он дома', 'Мы готовы'.\n  • *Фразы:* 'быть вовремя', 'быть согласным', 'мне 25 лет'.",

            "**2. Иметь / У меня есть:** Обладание и состояние.\n  • *Примеры:* 'У меня есть машина', 'У неё есть сестра', 'У меня болит голова'.\n  • *Фразы:* 'иметь значение', 'иметь в виду', 'у меня есть время'.",

            "**3. Думать:** Выражение мнения и мыслительный процесс.\n  • *Примеры:* 'Я думаю, да', 'Что ты думаешь об этом?', 'Я думаю о тебе'.\n  • *Фразы:* 'думать о', 'подумать дважды', 'как ты думаешь?'.",

            "**4. Знать:** Фактическое знание, умения и знакомство.\n  • *Примеры:* 'Я знаю ответ', 'Ты знаешь его?', 'Я знаю, как это делать'.\n  • *Фразы:* 'дай мне знать', 'насколько я знаю', 'кто знает'.",

            "**5. Нравиться / Любить:** Симпатии и предпочтения.\n  • *Примеры:* 'Мне нравится кофе', 'Она любит читать', 'Тебе нравится спорт?'.\n  • *Фразы:* 'очень нравится', 'мне бы хотелось', 'как тебе нравится?'.",

            "**6. Хотеть / Хотел бы:** Желания и вежливые просьбы.\n  • *Примеры:* 'Я хочу воду', 'Я хотел бы чай, пожалуйста', 'Куда ты хочешь пойти?'.\n  • *Фразы:* 'хотеть пить / есть', 'если хочешь', 'я хотел бы заказать'.",

            "**7. Идти / Ехать / Собираться:** Движение и планы на будущее.\n  • *Примеры:* 'Я иду на работу', 'Она едет домой', 'Мы собираемся обедать'.\n  • *Фразы:* 'идти пешком', 'как дела?', 'собираться делать'.",

            "**8. Мочь:** Способность, возможность и разрешение.\n  • *Примеры:* 'Я могу говорить по-русски', 'Можешь помочь мне?', 'Можно войти?'.\n  • *Фразы:* 'может быть', 'как можно скорее', 'чем могу помочь?'.",

            "**9. Есть (кушать):** Приемы пищи и еда.\n  • *Примеры:* 'Я ем фрукты каждое утро', 'Что будем есть?', 'Поесть в ресторане'.\n  • *Фразы:* 'приятного аппетита', 'хотеть есть', 'что-нибудь поесть'.",

            "**10. Пить:** Напитки и утоление жажды.\n  • *Примеры:* 'Я пью чай', 'Хочешь что-нибудь выпить?', 'Он пьет воду'.\n  • *Фразы:* 'хотеть пить', 'горячий напиток', 'выпить кофе'."
        ],
        "p2_items": [
            "**1. Делать:** Повседневные дела и действия.\n  • *Примеры:* 'Делать работу', 'Делать зарядку', 'Делать ошибки'.\n  • *Фразы:* 'делать всё возможное', 'что делать?', 'делать кофе'.",

            "**2. Говорить / Сказать:** Общение и речь.\n  • *Примеры:* 'Говорить по-русски', 'Сказать правду', 'Скажи мне'.\n  • *Фразы:* 'говорить о', 'так сказать', 'сказать да'.",

            "**3. Смотреть / Видеть:** Зрительное внимание и восприятие.\n  • *Примеры:* 'Смотреть фильм', 'Я вижу птицу'.\n  • *Фразы:* 'смотреть телевизор', 'посмотрим', 'до встречи'.",

            "**4. Слушать / Слышать:** Слуховое внимание и восприятие.\n  • *Примеры:* 'Слушать музыку', 'Я слышу шум'.\n  • *Фразы:* 'слушай внимательно', 'рад слышать'.",

            "**5. Должен / Надо:** Необходимость и обязанность.\n  • *Примеры:* 'Я должен учиться', 'Надо идти'.\n  • *Фразы:* 'так должно быть', 'мне надо'.",

            "**6. Брать / Давать / Получать:** Обмен и получение.\n  • *Примеры:* 'Брать такси', 'Давать подарок', 'Получить письмо'.\n  • *Фразы:* 'принимать решение', 'давать руку', 'получить ответ'.",

            "**7. Жить:** Место жительства и образ жизни.\n  • *Примеры:* 'Я живу в Москве', 'Жить хорошо'.\n  • *Фразы:* 'жить за границей', 'жить вместе'.",

            "**8. Ждать:** Ожидание и терпение.\n  • *Примеры:* 'Ждать автобус', 'Подожди минуту'.\n  • *Фразы:* 'не могу дождаться', 'ждать в очереди'.",

            "**9. Понимать:** Понимание.\n  • *Примеры:* 'Я понимаю урок', 'Ты понимаешь меня?'.\n  • *Фразы:* 'так сказать, чтобы поняли', 'прекрасно понимаю'.",

            "**10. Спрашивать / Отвечать:** Вопросы и ответы.\n  • *Примеры:* 'Задать вопрос', 'Ответить на звонок'.\n  • *Фразы:* 'просить о помощи', 'быстро ответить'."
        ]
    },
    "el": {
        "name": "Greek",
        "p1_title": "Τα 10 Βασικά Ρήματα στην Ελληνική Γλώσσα για Αρχάριους (CEFR A0–A1)",
        "p2_title": "Τα 10 Βασικά Ρήματα στην Ελληνική Γλώσσα, Μέρος 2 (CEFR A0–A1)",
        "p1_kicker": "ΟΔΗΓΟΣ ΕΛΛΗΝΙΚΩΝ — ΜΕΡΟΣ 1",
        "p2_kicker": "ΟΔΗΓΟΣ ΕΛΛΗΝΙΚΩΝ — ΜΕΡΟΣ 2",
        "p1_dek": "Μάθετε τα 10 βασικά ρήματα: είμαι, έχω, σκέφτομαι, ξέρω/γνωρίζω, μου αρέσει, θέλω/θα ήθελα, πηγαίνω/θα πάω, μπορώ, τρώω και πίνω με παραδείγματα.",
        "p2_dek": "Δεύτερο μέρος του οδηγού βασικών ρημάτων της ελληνικής γλώσσας (A0–A1): κάνω/φτιάχνω, μιλώ/λέω, κοιτάζω/βλέπω, ακούω, πρέπει, παίρνω/δίνω, ζω/μένω, περιμένω, καταλαβαίνω, ρωτώ/απαντώ.",
        "p1_intro": "Καλώς ήρθατε στο πρώτο μέρος του οδηγού βασικών ελληνικών ρημάτων για το επίπεδο A0–A1! Για κάθε ρήμα θα βρείτε χρήσιμες εκφράσεις και παραδείγματα.",
        "p2_intro": "Καλώς ήρθατε στο δεύτερο μέρος του οδηγού ελληνικών ρημάτων για αρχάριους (A0–A1)! Εξετάζουμε 10 νέα ρήματα δράσης, επικοινωνίας και αντίληψης.",
        "h_breakdown_p1": "Αναλυτική Παρουσίαση: Τα 10 Ελληνικά Ρήματα (Μέρος 1)",
        "h_breakdown_p2": "Αναλυτική Παρουσίαση: Τα 10 Ελληνικά Ρήματα (Μέρος 2)",
        "h_matrix": "Συγκριτικός Πίνακας σε 14 Γλώσσες",
        "h_family": "Γλωσσικές Οικογένειες & Γραμματικά Στοιχεία",
        "h_practice": "Πρακτικές Ασκήσεις & Πλοήγηση",
        "matrix_intro": "Παρακάτω παρουσιάζεται η συγκριτική ανάλυση των βασικών ρημάτων στις 14 επίσημες γλώσσες:",
        "family_text": "• **Ινδοευρωπαϊκή:** Χρησιμοποιεί βοηθητικά ρήματα χρόνου και κλιτικές καταλήξεις προσώπου/αριθμού.\n• **Τουρκική οικογένεια (Ταταρικά, Μπασκίρ, Τσουβασικά):** Συγκολλητικές δομές επιθημάτων χωρίς ξεχωριστά βοηθητικά ρήματα.\n• **Καρτβελική (Γεωργιανά):** Πολυπρόσωπη συμφωνία ρήματος που δηλώνει υποκείμενο και αντικείμενα.",
        "practice_text": "📌 Ανακαλύψτε και τα 14 άρθρα στο κέντρο του COSYmagazine ή δοκιμάστε τις γνώσεις σας στο [COSYpractice](https://cosylanguages.github.io/COSYpractice/) και δείτε τους πίνακες ρημάτων στο [COSYtools](https://cosylanguages.github.io/COSYtools/).",
        "p1_items": [
            "**1. Είμαι:** Ταυτότητα, κατάσταση και τοποθεσία.\n  • *Παραδείγματα:* 'Είμαι μαθητής', 'Είναι στο σπίτι', 'Είμαστε έτοιμοι'.\n  • *Χρήσιμες εκφράσεις:* 'είμαι στην ώρα μου', 'σύμφωνος', 'είμαι 25 χρονών'.",

            "**2. Έχω:** Κατοχή, ηλικία και σωματικές καταστάσεις.\n  • *Παραδείγματα:* 'Έχω αυτοκίνητο', 'Έχω 25 χρόνια', 'Έχω πείνα / δίψα'.\n  • *Χρήσιμες εκφράσεις:* 'έχω ανάγκη', 'έχω όρεξη', 'έχω χρόνο'.",

            "**3. Σκέφτομαι:** Έκφραση γνώμης και σκέψης.\n  • *Παραδείγματα:* 'Σκέφτομαι πως ναι', 'Τι σκέφτεσαι για αυτό;', 'Σε σκέφτομαι'.\n  • *Χρήσιμες εκφράσεις:* 'σκέφτομαι να', 'ξανασκέφτομαι'.",

            "**4. Ξέρω / Γνωρίζω:** Γνώση, δεξιότητες και γνωριμία.\n  • *Παραδείγματα:* 'Ξέρω την απάντηση', 'Γνωρίζω αυτή την πόλη', 'Ξέρεις πού είναι;'.\n  • *Χρήσιμες εκφράσεις:* 'κάνω γνωστό', 'από όσο ξέρω'.",

            "**5. Μου αρέσει:** Προτιμήσεις και γούστα.\n  • *Παραδείγματα:* 'Μου αρέσει ο καφές', 'Μου αρέσει να ταξιδεύω'.\n  • *Χρήσιμες εκφράσεις:* 'μου αρέσει πολύ', 'θα μου άρεσε'.",

            "**6. Θέλω / Θα ήθελα:** Επιθυμίες και ευγενικές αιτήσεις.\n  • *Παραδείγματα:* 'Θέλω νερό', 'Θα ήθελα έναν καφέ παρακαλώ'.\n  • *Χρήσιμες εκφράσεις:* 'θέλω να πω', 'αν θέλεις'.",

            "**7. Πηγαίνω / Θα πάω:** Μετακίνηση και μελλοντικά σχέδια.\n  • *Παραδείγματα:* 'Πηγαίνω στη δουλειά', 'Πάμε σπίτι', 'Θα πάμε ταξίδι'.\n  • *Χρήσιμες εκφράσεις:* 'πως πάει;', 'πηγαίνω με τα πόδια'.",

            "**8. Μπορώ:** Ικανότητα, δυνατότητα και άδεια.\n  • *Παραδείγματα:* 'Μπορώ να βοηθήσω;', 'Μπορείς να έρθεις;'.\n  • *Χρήσιμες εκφράσεις:* 'αν είναι δυνατόν', 'μπορεί'.",

            "**9. Τρώω:** Γεύματα και διατροφή.\n  • *Παραδείγματα:* 'Τρώω φρούτα κάθε πρωί', 'Τι θα φάμε;'.\n  • *Χρήσιμες εκφράσεις:* 'καλή όρεξη', 'τρώω έξω'.",

            "**10. Πίνω:** Ποτά και ενυδάτωση.\n  • *Παραδείγματα:* 'Πίνω τσάι', 'Θέλεις κάτι να πιεις;'.\n  • *Χρήσιμες εκφράσεις:* 'στην υγειά μας', 'πίνω καφέ'."
        ],
        "p2_items": [
            "**1. Κάνω / Φτιάχνω:** Δραστηριότητες.\n  • *Παραδείγματα:* 'Κάνω μαθήματα', 'Φτιάχνω καφέ'.\n  • *Χρήσιμες εκφράσεις:* 'κάνω γυμναστική', 'κάνω λάθος'.",

            "**2. Μιλώ / Λέω:** Επικοινωνία.\n  • *Παραδείγματα:* 'Μιλώ ελληνικά', 'Λέω την αλήθεια'.\n  • *Χρήσιμες εκφράσεις:* 'μιλώ για', 'λέω γεια'.",

            "**3. Κοιτάζω / Βλέπω:** Όραση και προσοχή.\n  • *Παραδείγματα:* 'Κοιτάζω την ταινία', 'Βλέπω ένα πουλί'.\n  • *Χρήσιμες εκφράσεις:* 'για να δούμε', 'θα δούμε'.",

            "**4. Ακούω:** Ακοή.\n  • *Παραδείγματα:* 'Ακούω μουσική', 'Ακούω έναν θόρυβο'.\n  • *Χρήσιμες εκφράσεις:* 'άκουσε με', 'χαίρομαι που το ακούω'.",

            "**5. Πρέπει:** Υποχρέωση.\n  • *Παραδείγματα:* 'Πρέπει να διαβάσω', 'Πρέπει να φύγουμε'.\n  • *Χρήσιμες εκφράσεις:* 'όπως πρέπει', 'πρέπει να'.",

            "**6. Παίρνω / Δίνω:** Ανταλλαγή.\n  • *Παραδείγματα:* 'Παίρνω το λεωφορείο', 'Δίνω ένα δώρο'.\n  • *Χρήσιμες εκφράσεις:* 'παίρνω χρόνο', 'δίνω το χέρι'.",

            "**7. Μένω / Ζω:** Κατοικία.\n  • *Παραδείγματα:* 'Μένω στην Αθήνα', 'Ζω καλά'.\n  • *Χρήσιμες εκφράσεις:* 'ζω στο εξωτερικό', 'μένουμε μαζί'.",

            "**8. Περιμένω:** Αναμονή.\n  • *Παραδείγματα:* 'Περιμένω το λεωφορείο', 'Περίμενε ένα λεπτό'.\n  • *Χρήσιμες εκφράσεις:* 'περιμένω στη σειρά', 'ανυπομονώ'.",

            "**9. Καταλαβαίνω:** Κατανόηση.\n  • *Παραδείγματα:* 'Καταλαβαίνω το μάθημα', 'Καταλαβαίνεις;'.\n  • *Χρήσιμες εκφράσεις:* 'καταλαβαίνω απόλυτα'.",

            "**10. Ρωτώ / Απαντώ:** Ερωτήσεις και απαντήσεις.\n  • *Παραδείγματα:* 'Κάνω μια ερώτηση', 'Απαντώ στο τηλέφωνο'.\n  • *Χρήσιμες εκφράσεις:* 'ζητώ βοήθεια', 'απαντώ αμέσως'."
        ]
    },
    "tt": {
        "name": "Tatar",
        "p1_title": "Татар теле буенча иң мөһим 10 фигыль (CEFR A0–A1)",
        "p2_title": "Татар теле буенча иң мөһим 10 фигыль, 2 өлеш (CEFR A0–A1)",
        "p1_kicker": "ТАТАР ТЕЛЕ МӘГАРИФЕ — 1 ӨЛЕШ",
        "p2_kicker": "ТАТАР ТЕЛЕ МӘГАРИФЕ — 2 ӨЛЕШ",
        "p1_dek": "Иң мөһим 10 фигыль: булу, бар/минем бар, уйлау, белү, ярату/ошату, теләү/тели идем, бару/бармакчы, булдыру, ашау һәм эчү.",
        "p2_dek": "Башлап өйрәнүчеләр өчен 2-нче өлеш: эшләү, сөйләү/әйтү, карау/күрү, тыңлау/ишетү, кирәк/тиеш, алу/бирү, яшәү, көтү, аңлау, сорау/җавап бирү.",
        "p1_intro": "Татар теле буенча башлап өйрәнүчеләр өчен (A0–A1) иң мөһим фигыльләр кулланмасының 1-нче өлешенә рәхим итегез!Һәр фигыль буенча үрнәкләр һәм җөмлә үрнәкләре бирелә.",
        "p2_intro": "Татар теле фигыльләре кулланмасының 2-нче өлешенә рәхим итегез! 10 яңа төп фигыльне өйрәнәбез.",
        "h_breakdown_p1": "Төп 10 Татар фигыле (1 өлеш)",
        "h_breakdown_p2": "Төп 10 Татар фигыле (2 өлеш)",
        "h_matrix": "14 тел арасында чагыштырма таблица",
        "h_family": "Тел гаиләләре һәм грамматик үзенчәлекләр",
        "h_practice": "Практик күнегүләр һәм навигация",
        "matrix_intro": "Түбәндә барлык 14 рәсми тел буенча төп фигыльләрнең чагыштырма анализы бирелә:",
        "family_text": "• **Индоевропа гаиләсе:** Вакыт ярдамчы фигыльләре һәм зат/сан кушымталары кулланыла.\n• **Төрки гаилә (Татар, Башҡорт, Чуваш):** Аерым ярдамчы сүзләрсез вакыт һәм затны белдерүче агглютинатив кушымталар.\n• **Картвел гаиләсе (Грузин):** Субъект һәм объектны бергә белдерүче полиперсональ спряжение.",
        "practice_text": "📌 COSYmagazine хабында 14 тел мәкаләсен өйрәнегез яки белемегезне [COSYpractice](https://cosylanguages.github.io/COSYpractice/) битендә тикшерегез һәм [COSYtools](https://cosylanguages.github.io/COSYtools/) битендә фигыль таблицаларын карагыз.",
        "p1_items": [
            "**1. Булу:** Ешлык һәм булу (*Мин студент*, *Ул өйдә*, *Әзербез*).",
            "**2. Бар / Юк (Минем бар):** Иялек (*Минем машинам бар*, *Минем вакытым бар*).",
            "**3. Уйлау:** Фикер белдерү (*Мин шулай уйлыйм*, *Сез ничек уйлыйсыз?*).",
            "**4. Белү:** Белем (*Мин җавапны беләм*, *Ул белә*).",
            "**5. Ярату / Ошату:** Сағыну һәм ошату (*Мин чәй яратам*, *Музыка ошый*).",
            "**6. Теләү / Тели идем:** Теләкләр (*Мин су телим*, *Чәй тели идем*).",
            "**7. Бару / Бармакчы:** Хәрәкәт (*Мин эшкә барам*, *Өйгә бару*).",
            "**8. Булдыру (Булдыра алу):** Мөмкинлек (*Мин сөйләшә алам*).",
            "**9. Ашау:** Ашау-эчү (*Мин алма ашам*, *Ашарга теләү*).",
            "**10. Эчү:** Эчемлекләр (*Чәй эчү*, *Су эчәсе килә*)."
        ],
        "p2_items": [
            "**1. Эшләү / Ясау:** Эш һәм ясау (*Өй эшләрен эшләү*).",
            "**2. Сөйләү / Әйтү:** Сөйләшү (*Татарча сөйләшү*).",
            "**3. Карау / Күрү:** Игътибар (*Фильм карау*).",
            "**4. Тыңлау / Ишетү:** Тыңлау (*Музыка тыңлау*).",
            "**5. Кирәк / Тиеш:** Зарурилык (*Миңа өйрәнергә кирәк*).",
            "**6. Алу / Бирү:** Алмашу (*Китап алу*).",
            "**7. Яшәү:** Яшәү урыны (*Мин Казанда яшим*).",
            "**8. Көтү:** Көтү (*Автобус көтү*).",
            "**9. Аңлау:** Аңлау (*Мин аңлыйм*).",
            "**10. Сорау / Җавап бирү:** Сорау бирү (*Сорау бирү*)."
        ]
    },
    "ba": {
        "name": "Bashkir",
        "p1_title": "Башҡорт теле буйынса иң мөһим 10 ҡылым (CEFR A0–A1)",
        "p2_title": "Башҡорт теле буйынса иң мөһим 10 ҡылым, 2-се өлөш (CEFR A0–A1)",
        "p1_kicker": "БАШҠОРТ ТЕЛЕ МӘҒАРИФЫ — 1-СЕ ӨЛӨШ",
        "p2_kicker": "БАШҠОРТ ТЕЛЕ МӘҒАРИФЫ — 2-СЕ ӨЛӨШ",
        "p1_dek": "Иң мөһим 10 ҡылым: булыу, бар/минең бар, уйлау, белеү, яратыу, теләү, барыу, булдырыу, ашау һәм эсеү.",
        "p2_dek": "Башлап өйрәнеүселәр өсөн 2-се өлөш: эшләү, һөйләү/әйтеү, ҡарау/күреү, тыңлау/ишетеү, кәрәк/тәйеш, алыу/биреү, йәшәү, көтөү, аңлау, һорау/яуап биреү.",
        "p1_intro": "Башҡорт теле буйынса башлап өйрәнеүселәр өсөн (A0–A1) иң мөһим ҡылымдар ҡулланмаһына рәхим итегеҙ!",
        "p2_intro": "Башҡорт теле ҡылымдары ҡулланмаһының 2-се өлөшөнә рәхим итегеҙ! 10 яңы төп ҡылымды өйрәнәбеҙ.",
        "h_breakdown_p1": "Төп 10 Башҡорт ҡылымы (1-се өлөш)",
        "h_breakdown_p2": "Төп 10 Башҡорт ҡылымы (2-се өлөш)",
        "h_matrix": "14 тел араһында сағыштырыу таблицаһы",
        "h_family": "Тел ғаиләләре һәм грамматика үҙенсәлектәре",
        "h_practice": "Практик күнегеүҙәр һәм навигация",
        "matrix_intro": "Түбәндә барлыҡ 14 рәсми тел буйынса төп ҡылымдарҙың сағыштырыу анализы бирелә:",
        "family_text": "• **Индоевропа ғаиләһе:** Ваҡыт ярҙамсы ҡылымдары ҡулланыла.\n• **Төрки ғаилә (Башҡорт, Татар, Чуваш):** Агглютинатив ҡушымталар.",
        "practice_text": "📌 COSYmagazine хабында 14 тел мәҡәләһен өйрәнегеҙ йәки белемегеҙҙе [COSYpractice](https://cosylanguages.github.io/COSYpractice/) битендә тикшерегеҙ.",
        "p1_items": [
            "**1. Вулыу / Булыу:** Торош (*Мин студент*, *Өйҙә*).",
            "**2. Бар / Юҡ:** Эйәлек (*Минең китабым бар*).",
            "**3. Уйлау:** Фикер (*Мин шулай уйлайым*).",
            "**4. Белеү:** Белем (*Мин яуапты беләм*).",
            "**5. Яратыу:** Ошатыу (*Мин музыка яратам*).",
            "**6. Теләү:** Теләк (*Һыу теләйем*).",
            "**7. Барыу:** Хәрәкәт (*Мин мәктәпкә барам*).",
            "**8. Булдырыу (Алыу):** Мөмкинлек (*Һөйләшә алам*).",
            "**9. Ашау:** Ашау (*Алма ашау*).",
            "**10. Эсеү:** Эсеү (*Сәй эсеү*)."
        ],
        "p2_items": [
            "**1. Эшләү / Яһау:** Эш (*Эш эшләү*).",
            "**2. Һөйләү / Әйтеү:** Һөйләшеү (*Һөйләшеү*).",
            "**3. Ҡарау / Күреү:** Ҡарау (*Кино ҡарау*).",
            "**4. Тыңлау / Ишетеү:** Тыңлау (*Музыка тыңлау*).",
            "**5. Кәрәк / Тиеш:** Зарурилыҡ (*Кәрәк*).",
            "**6. Алыу / Биреү:** Алмашыу (*Китап алыу*).",
            "**7. Йәшәү:** Йәшәү (*Өфөлә йәшәйем*).",
            "**8. Көтөү:** Көтөү (*Көтөү*).",
            "**9. Аңлау:** Аңлау (*Аңлайым*).",
            "**10. Һорау / Яуап биреү:** Һорау (*Һорау биреү*)."
        ]
    },
    "br": {
        "name": "Breton",
        "p1_title": "Ar 10 verb pennañ e brezhoneg evit ar re dhazerañ (CEFR A0–A1)",
        "p2_title": "Ar 10 verb pennañ e brezhoneg, Rann 2 (CEFR A0–A1)",
        "p1_kicker": "KAVLEVR BREZHONEG — RANN 1",
        "p2_kicker": "KAVLEVR BREZHONEG — RANN 2",
        "p1_dek": "Deskit ar 10 verb pennañ: bezañ, kaout, meizañ/soñjal, gouzout, plijout, c'hoant kaout, mont, gallout, debriñ hag evañ.",
        "p2_dek": "Eil rann eus ar c'havlevr verboù brezhonek (A0–A1) : ober, komz/lavarout, sellet/gwelout, selaou/klevout, rankout, kemer/rein, bevañ, gortoz, meizañ ha goulenn/respont.",
        "p1_intro": "Degemer mat e kavlevr ar verboù brezhonek pennañ evit al live A0–A1 !",
        "p2_intro": "Degemer mat en eil rann eus kavlevr ar verboù brezhonek (A0–A1) !",
        "h_breakdown_p1": "Dielfennadur munut : Ar 10 verb brezhonek (Rann 1)",
        "h_breakdown_p2": "Dielfennadur munut : Ar 10 verb brezhonek (Rann 2)",
        "h_matrix": "Taolenn geñveriañ dre 14 yezh",
        "h_family": "Lodennoù yezh ha poentouriezh yezhadurel",
        "h_practice": "Aozioù pleustriñ ha merdeiñ",
        "matrix_intro": "Setu an daolenn geñveriañ eus ar verboù pennañ er 14 yezh ofisiel :",
        "family_text": "• **Indezeuropegek:** Implijout a ra verboù skoazell.",
        "practice_text": "📌 Enklaskit an 14 pennad yezh e kreizenn COSYmagazine.",
        "p1_items": [
            "**1. Bezañ:** Bezañs (*Skoaziad on*).",
            "**2. Kaout:** Perc'henniezh (*Libr am eus*).",
            "**3. Soñjal:** Soñj (*Soñjal a ran*).",
            "**4. Gouzout / Anavezout:** Gouziegezh (*Gouzout a ran*).",
            "**5. Pliout:** Pliadur (*Pliout a ra din*).",
            "**6. C'hoant kaout:** Fellout (*C'hoant am eus*).",
            "**7. Mont:** Mont (*Mont d'ar skol*).",
            "**8. Gallout:** Galloud (*Gallout a ran*).",
            "**9. Debriñ:** Debriñ (*Debriñ avaloù*).",
            "**10. Evañ:** Evañ (*Evañ dour*)."
        ],
        "p2_items": [
            "**1. Ober:** Obererezh (*Ober al labour*).",
            "**2. Komz / Lavarout:** Komz (*Komz brezhoneg*).",
            "**3. Sellet / Gwelout:** Sellet (*Sellet ouzh ur film*).",
            "**4. Selaou / Klevout:** Selaou (*Selaou sonerezh*).",
            "**5. Rankout:** Retiez (*Rankout a ran*).",
            "**6. Kemer / Rein:** Eskemm (*Kemer ur banne*).",
            "**7. Bevañ / Chom:** Bevañ (*Bevañ e Roazhon*).",
            "**8. Gortoz:** Gortoz (*Gortoz*).",
            "**9. Meizañ:** Meizañ (*Kompren a ran*).",
            "**10. Goulenn / Respont:** Goulenn (*Goulenn ur gaoz*)."
        ]
    },
    "pt": {
        "name": "Portuguese",
        "p1_title": "Os 10 verbos essenciais em português para principiantes (CEFR A0–A1)",
        "p2_title": "Os 10 verbos essenciais em português, Parte 2 (CEFR A0–A1)",
        "p1_kicker": "GUIA DE PORTUGUÊS — PARTE 1",
        "p2_kicker": "GUIA DE PORTUGUÊS — PARTE 2",
        "p1_dek": "Domine os 10 verbos essenciais: ser/estar, ter, pensar, saber/conhecer, gostar, querer/gostaria, ir/ir a, poder, comer e beber.",
        "p2_dek": "Segunda parte do guia essencial de verbos em português (A0–A1): fazer, falar/dizer, olhar/ver, ouvir/escutar, ter de/dever, tomar/dar, viver/morar, esperar, entender e perguntar/responder.",
        "p1_intro": "Bem-vindo ao guia de verbos essenciais em português para o nível A0–A1!",
        "p2_intro": "Bem-vindo à segunda parte do guia de verbos em português para principiantes (A0–A1)!",
        "h_breakdown_p1": "Análise detalhada: Os 10 verbos em português (Parte 1)",
        "h_breakdown_p2": "Análise detalhada: Os 10 verbos em português (Parte 2)",
        "h_matrix": "Matriz linguística comparativa em 14 línguas",
        "h_family": "Nuances das famílias linguísticas e aspetos gramaticais",
        "h_practice": "Exercícios práticos e navegação",
        "matrix_intro": "Apresentamos abaixo a análise comparativa dos principais verbos nas 14 línguas oficiais:",
        "family_text": "• **Indo-europeu:** Utiliza auxiliares de tempo.",
        "practice_text": "📌 Explore todos os 14 artigos no hub da COSYmagazine.",
        "p1_items": [
            "**1. Ser / Estar:** Identidade e estado (*Sou estudante*, *Estou em casa*).",
            "**2. Ter:** Posse e idade (*Tenho um livro*, *Tenho 25 anos*).",
            "**3. Pensar:** Opinioes (*Penso que sim*).",
            "**4. Saber / Conhecer:** Conhecimento (*Sei a resposta*).",
            "**5. Gostar:** Preferências (*Gosto de café*).",
            "**6. Querer / Gostaria:** Desejos (*Quero água*, *Gostaria de um chá*).",
            "**7. Ir:** Movimento (*Vou trabalhar*).",
            "**8. Poder:** Capacidade (*Posso ajudar?*).",
            "**9. Comer:** Alimentação (*Comer uma maçã*).",
            "**10. Beber:** Bebidas (*Beber água*)."
        ],
        "p2_items": [
            "**1. Fazer:** Atividades (*Fazer os TPC*).",
            "**2. Falar / Dizer:** Comunicação (*Falar português*).",
            "**3. Olhar / Ver:** Atenção visual (*Olhar para um filme*).",
            "**4. Ouvir / Escutar:** Audição (*Ouvir música*).",
            "**5. Ter de / Dever:** Obrigação (*Tenho de estudar*).",
            "**6. Tomar / Dar:** Troca (*Tomar um café*).",
            "**7. Morar / Viver:** Residência (*Moro em Lisboa*).",
            "**8. Esperar:** Paciência (*Esperar o autocarro*).",
            "**9. Entender / Compreender:** Compreensão (*Entendo a lição*).",
            "**10. Perguntar / Responder:** Perguntas (*Fazer uma pergunta*)."
        ]
    },
    "hy": {
        "name": "Armenian",
        "p1_title": "Հայերենի 10 հիմնական բայերը սկսնակների համար (CEFR A0–A1)",
        "p2_title": "Հայերենի 10 հիմնական բայերը, Մաս 2 (CEFR A0–A1)",
        "p1_kicker": "ՀԱՅԵՐԵՆԻ ՈՒՂԵՑՈՒՅՑ — ՄԱՍ 1",
        "p2_kicker": "ՀԱՅԵՐԵՆԻ ՈՒՂԵՑՈՒՅՑ — ՄԱՍ 2",
        "p1_dek": "Սովորեք 10 հիմնական բայերը․ լինել, ունենալ, մտածել, իմանալ, սիրել, ուզենալ, գնալ, կարողանալ, ուտել և խմել։",
        "p2_dek": "Սկսնակների համար հայերենի հիմնական բայերի ուղեցույցի երկրորդ մասը (A0–A1)․ անել, խոսել/ասել, նայել/տեսնել, լսել, պետք է, վերցնել/տալ, ապրել, սպասել, հասկանալ և հարցնել/պատասխանել։",
        "p1_intro": "Բարի գալուստ հայերենի հիմնական բայերի ուղեցույց սկսնակների համար (A0–A1)։",
        "p2_intro": "Բարի գալուստ հայերենի բայերի ուղեցույցի երկրորդ մաս (A0–A1)։",
        "h_breakdown_p1": "Մանրամասն վերլուծություն․ Հայերենի 10 բայերը (Մաս 1)",
        "h_breakdown_p2": "Մանրամասն վերլուծություն․ Հայերենի 10 բայերը (Մաս 2)",
        "h_matrix": "Համեմատական լեզվաբանական աղյուսակ 14 լեզուներով",
        "h_family": "Լեզվաընտանիքների առանձնահատկությունները",
        "h_practice": "Գործնական վարժություններ և նավիգացիա",
        "matrix_intro": "Ստորև ներկայացված է հիմնական բայերի համեմատական վերլուծությունը բոլոր 14 պաշտոնական լեզուներով․",
        "family_text": "• **Հնդեվրոպական․** Օգտագործում է ժամանակի օժանդակ բայեր։",
        "practice_text": "📌 Ուսումնասիրեք բոլոր 14 լեզվական հոդվածները COSYmagazine կենտրոնում։",
        "p1_items": [
            "**1. Լինել:** Ինքնություն (*Ես ուսանող եմ*).",
            "**2. Ունենալ:** Ունեցվածք (*Ես գիրք ունեմ*).",
            "**3. Մտածել:** Կարծիք (*Ես մտածում եմ*).",
            "**4. Իմանալ / Ճանաչել:** Գիտելիք (*Ես գիտեմ պատասխանը*).",
            "**5. Սիրել:** Նախասիրություն (*Ես սիրում եմ սուրճ*).",
            "**6. Ուզենալ:** Ցանկություն (*Ես ջուր եմ ուզում*).",
            "**7. Գնալ:** Շարժում (*Ես գնում եմ դպրոց*).",
            "**8. Կարողանալ:** Կարողություն (*Ես կարող եմ խոսել*).",
            "**9. Ուտել:** Ուտելիք (*Հաց ուտել*).",
            "**10. Խմել:** Խմիչք (*Ջուր խմել*)."
        ],
        "p2_items": [
            "**1. Անել:** Գործեր (*Անել դասերը*).",
            "**2. Խոսել / Ասել:** Հաղորդակցություն (*Խոսել հայերեն*).",
            "**3. Նայել / Տեսնել:** Ուշադրություն (*Նայել ֆիլմ*).",
            "**4. Լսել:** Լսողություն (*Երաժշտություն լսել*).",
            "**5. Պետք է:** Անհրաժեշտություն (*Ես պետք է սովորեմ*).",
            "**6. Վերցնել / Տալ:** Փոխանակում (*Սուրճ վերցնել*).",
            "**7. Ապրել:** Բնակություն (*Ես ապրում եմ Երևանում*).",
            "**8. Սպասել:** Սպասում (*Սպասել ավտոբուսին*).",
            "**9. Հասկանալ:** Ըմբռնում (*Ես հասկանում եմ*).",
            "**10. Հարցնել / Պատասխանել:** Հարցեր (*Հարց տալ*)."
        ]
    },
    "ka": {
        "name": "Georgian",
        "p1_title": "10 ძირითადი ზმნა ქართულ ენაში დამწყებთათვის (CEFR A0–A1)",
        "p2_title": "10 ძირითადი ზმნა ქართულ ენაში, ნაწილი 2 (CEFR A0–A1)",
        "p1_kicker": "ქართული ენის სახელმძღვანელო — ნაწილი 1",
        "p2_kicker": "ქართული ენის სახელმძღვანელო — ნაწილი 2",
        "p1_dek": "ისწავლეთ 10 ძირითადი ზმნა: ყოფნა, ქონა/ყოლიება, ფიქრი, ცოდნა, მოწონება, ნდომა, წასვლა, შეძლება, ჭამა და დალევა.",
        "p2_dek": "ქართული ენის ძირითადი ზმნების სახელმძღვანელოს მეორე ნაწილი დამწყებთათვის (A0–A1): კეთება, ლაპარაკი/თქმა, ყურება/ნახვა, მოსმენა, უნდა/საჭიროა, აღება/მიცემა, ცხოვრება, ლოდინი, გაგება და კითხვა/პასუხი.",
        "p1_intro": "კეთილი იყოს თქვენი მობრძანება ქართული ენის ძირითადი ზმნების სახელმძღვანელოში A0–A1 დონისთვის!",
        "p2_intro": "მოგესალმებით ქართული ზმნების სახელმძღვანელოს მეორე ნაწილში (A0–A1)!",
        "h_breakdown_p1": "დეტალური ანალიზი: 10 ქართული ზმნა (ნაწილი 1)",
        "h_breakdown_p2": "დეტალური ანალიზი: 10 ქართული ზმნა (ნაწილი 2)",
        "h_matrix": "14 ენის შედარებითი ენათმეცნიერული ცხრილი",
        "h_family": "ენათა ოჯახის თავისებურებები და გრამატიკა",
        "h_practice": "პრაქტიკული სავარჯიშოები და ნავიგაცია",
        "matrix_intro": "ქვემოთ მოცემულია ძირითადი ზმნების შედარებითი ანალიზი 14-ვე ოფიციალურ ენაზე:",
        "family_text": "• **ქართველური:** პოლიპერსონალური ზმნური შეთანხმება.",
        "practice_text": "📌 იხილეთ 14-ვე ენის სტატია COSYmagazine-ის ჰაბში.",
        "p1_items": [
            "**1. ყოფნა:** იდენტობა (*მე ვარ სტუდენტი*).",
            "**2. ქონა / Ჰყოლა:** ფლობა (*მე მაქვს წიგნი*).",
            "**3. ფიქრი:** აზრი (*მე ვფიქრობ*).",
            "**4. ცოდნა / ცნობა:** ცოდნა (*მე ვიცი პასუხი*).",
            "**5. მოწონება:** მოწონება (*მე მომწონს ყავა*).",
            "**6. ნდომა:** სურვილი (*მე მინდა წყალი*).",
            "**7. წასვლა:** მოძრაობა (*მივდივარ სკოლაში*).",
            "**8. შეძლება:** შესაძლებლობა (*მე შემიძლია*).",
            "**9. ჭამა:** კვება (*ვაშლის ჭამა*).",
            "**10. დალევა:** სითხე (*წყლის დალევა*)."
        ],
        "p2_items": [
            "**1. კეთება:** საქმე (*საქმის კეთება*).",
            "**2. ლაპარაკი / თქმა:** კომუნიკაცია (*ქართულად ლაპარაკი*).",
            "**3. ყურება / ნახვა:** ყურადღება (*ფილმის ყურება*).",
            "**4. მოსმენა:** სმენა (*მუსიკის მოსმენა*).",
            "**5. უნდა / საჭიროა:** აუცილებლობა (*მე უნდა ვისწავლო*).",
            "**6. აღება / მიცემა:** გაცვლა (*ყავის აღება*).",
            "**7. ცხოვრება:** საცხოვრებელი (*ვცხოვრობ თბილისში*).",
            "**8. ლოდინი:** ლოდინი (*ავტობუსის ლოდინი*).",
            "**9. გაგება:** გაგება (*მესმის გაკვეთილი*).",
            "**10. კითხვა / პასუხი:** კითხვა (*კითხვის დასმა*)."
        ]
    },
    "cv": {
        "name": "Chuvash",
        "p1_title": "Чăваш чĕлхинчи чи кирлĕ 10 глагол (CEFR A0–A1)",
        "p2_title": "Чăваш чĕлхинчи чи кирлĕ 10 глагол, 2-мĕш пай (CEFR A0–A1)",
        "p1_kicker": "ЧĂВАШ ЧĔЛХИН СУМЛĂ ГИДĔ — 1-МĔШ ПАЙ",
        "p2_kicker": "ЧĂВАШ ЧĔЛХИН СУМЛĂ ГИДĔ — 2-МĔШ ПАЙ",
        "p1_dek": "10 тĕп глагол: пулма, пур/манăн пур, шухăшлама, пĕлме, кăмăллама, тăвас килме, кайма, булма, çеме тата ĕçме.",
        "p2_dek": "Чăваш чĕлхипе пуçласа вĕренекенсем валли чи кирлĕ глаголсен 2-мĕш пайĕ: тăвасси, калаçасси/каласси, пăхасси/курасси, итлесси/ишитесси, кирлĕ, илесси/парасси, пурăнасси, кĕтесси, ăнланасси тата ыйтасси/хуравламалли.",
        "p1_intro": "Чăваш чĕлхипе пуçласа вĕренекенсем (A0–A1) валли чи кирлĕ глаголсен гидне кăч ярапăр!",
        "p2_intro": "Чăваш глаголĕсен гидĕн 2-мĕш пайне килĕр!",
        "h_breakdown_p1": "Тĕп 10 Чăваш глаголĕ (1-мĕш пай)",
        "h_breakdown_p2": "Тĕп 10 Чăваш глаголĕ (2-мĕш пай)",
        "h_matrix": "14 чĕлхе хушшинчи танлаштару таблици",
        "h_family": "Чĕлхе çемйисем тата грамматика уйрăмлăхĕсем",
        "h_practice": "Практика хăнăхăвĕсем тата навигаци",
        "matrix_intro": "Аллари 14 официаллă чĕлхе тăрăх тĕп глаголсен танлаштару анализĕ кунтан пăхăр:",
        "family_text": "• **Тĕрĕк çемйи:** Агглютинаци структурисем.",
        "practice_text": "📌 COSYmagazine хабĕнче 14 чĕлхе статьине вĕренĕр.",
        "p1_items": [
            "**1. Пулма:** Пулни (*Эпĕ студент*).",
            "**2. Пур / Ҫук:** Пурлăх (*Манăн кĕнеке пур*).",
            "**3. Шухăшлама:** Шухăш (*Эпĕ шухăшлатăп*).",
            "**4. Пĕлме:** Пĕлӳ (*Эпĕ хуравне пĕлетĕп*).",
            "**5. Кăмăллама:** Кăмăл (*Мана кофе кăмăла каять*).",
            "**6. Тăвас килесси:** Ĕмĕт (*Шыв ĕçесшĕн*).",
            "**7. Кайма:** Куçни (*Шкула каятăп*).",
            "**8. Пултарасси:** Пултару (*Эпĕ калаçма пултаратăп*).",
            "**9. Çеме:** Çимĕç (*Улма çеме*).",
            "**10. Ĕçме:** Ĕçмелли (*Шыв ĕçме*)."
        ],
        "p2_items": [
            "**1. Тăвасси:** Ĕçсем (*Ĕç тăвасси*).",
            "**2. Калаçасси / Каласси:** Калаçу (*Чăвашла калаçасси*).",
            "**3. Пăхасси / Курасси:** Асăрхаса пăхасси (*Фильм пăхасси*).",
            "**4. Итлесси / Ишитесси:** Итлесси (*Музыка итлесси*).",
            "**5. Кирлĕ:** Ыйтни (*Мана кирлĕ*).",
            "**6. Илесси / Парасси:** Улмаш (*Кĕнеке илесси*).",
            "**7. Пурăнасси:** Вырăн (*Пурăнатăп*).",
            "**8. Кĕтесси:** Кĕтесси (*Кĕтесси*).",
            "**9. Ăнланасси:** Ăнланасси (*Ăнланатăп*).",
            "**10. Ыйтасси / Хуравламалли:** Ыйту (*Ыйту парасси*)."
        ]
    }
}

posts_dir = "posts"
os.makedirs(posts_dir, exist_ok=True)

for code, lang in languages_data.items():
    for is_part_2 in [False, True]:
        slug = f"top-10-verbs-part-2-{code}" if is_part_2 else (f"top-10-verbs-{code}" if code != "en" else "top-10-verbs-en")
        filepath = os.path.join(posts_dir, f"{slug}.json")

        post_obj = {
            "id": f"post-{slug}",
            "slug": slug,
            "language": code,
            "translationOf": "top-10-verbs-part-2" if is_part_2 else "top-10-verbs",
            "desk": "Words",
            "format": "list",
            "level": "A0–A1 / A2",
            "issue": {
                "number": "Vol. 2026 — December Issue" if is_part_2 else "Vol. 2026 — August Issue",
                "title": "Winter Grammar & High Frequency Verbs" if is_part_2 else "Get ready for school"
            },
            "date": "2026-12-01" if is_part_2 else "2026-03-01",
            "title": lang["p2_title"] if is_part_2 else lang["p1_title"],
            "kicker": lang["p2_kicker"] if is_part_2 else lang["p1_kicker"],
            "dek": lang["p2_dek"] if is_part_2 else lang["p1_dek"],
            "tags": ["Verbs", lang["name"], "A0-A1", "Part2" if is_part_2 else "14Languages"],
            "readingTime": 10,
            "podcast": {
                "episode": 3 if is_part_2 else 2,
                "audioUrl": None
            },
            "artDirection": {
                "palette": ["#0284c7", "#f0f9ff", "#0f172a"] if is_part_2 else ["#d97706", "#fef3c7", "#0d9488", "#1e293b"],
                "fonts": {
                    "display": "Fraunces",
                    "text": "DM Sans",
                    "accent": "Fraunces Italic"
                },
                "layout": "magazine-spread",
                "motif": "editorial-stars",
                "seed": slug,
                "coverOverride": None
            },
            "blocks": [
                {
                    "type": "paragraph",
                    "text": lang["p2_intro"] if is_part_2 else lang["p1_intro"]
                },
                {
                    "type": "heading",
                    "level": 3,
                    "text": lang["h_breakdown_p2"] if is_part_2 else lang["h_breakdown_p1"]
                },
                {
                    "type": "list-item",
                    "ordered": False,
                    "items": lang["p2_items"] if is_part_2 else lang["p1_items"]
                },
                {
                    "type": "heading",
                    "level": 3,
                    "text": lang["h_matrix"]
                },
                {
                    "type": "paragraph",
                    "text": lang["matrix_intro"]
                },
                {
                    "type": "table",
                    "headers": ["Concept", "Romance (FR/IT/ES/PT)", "Germanic (EN/DE)", "Slavic / Hellenic / Celtic / Arm", "Turkic (TT/BA/CV)", "Kartvelian (KA)"],
                    "rows": [
                        ["Be / Exist", "être / essere / ser, estar / ser, estar", "be / sein", "быть / είναι / bezañ / լինել", "булу / булыу / пуласси", "ყოფნა (qopna)"],
                        ["Have / Possess", "avoir / avere / tener / ter", "have / haben", "иметь (у меня есть) / έχω / kaout / ունենալ", "бар (минем бар) / бар / пур", "ქონა / ყოლა"],
                        ["Do / Make", "faire / fare / hacer / fazer", "do, make / machen, tun", "делать / κάνω / ober / անել", "эшләү / эшләү / тăвасси", "კეთება (keteba)"],
                        ["Go", "aller / andare / ir / ir", "go / gehen", "идти, ехать / πηγαίνω / mont / գնալ", "бару / барыу / кайни", "წاسვლა (tsasvla)"],
                        ["See / Look", "voir, regarder / vedere, guardare", "see, look / sehen, schauen", "видеть, смотреть / βλέπω / gwelout / տեսնել", "күрү, карау / күреү, ҡарау / курасси", "ნახვა, ყურება"]
                    ]
                },
                {
                    "type": "heading",
                    "level": 3,
                    "text": lang["h_family"]
                },
                {
                    "type": "paragraph",
                    "text": lang["family_text"]
                },
                {
                    "type": "heading",
                    "level": 3,
                    "text": lang["h_practice"]
                },
                {
                    "type": "paragraph",
                    "text": lang["practice_text"]
                }
            ],
            "draft": False
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(post_obj, f, ensure_ascii=False, indent=2)

print("All JSON posts updated successfully with correct top 10 verbs lists and rich usages!")
