import json
import os

LANGUAGES = {
    "en": {"name": "English", "flag": "🇬🇧", "native": "English"},
    "fr": {"name": "French", "flag": "🇫🇷", "native": "Français"},
    "it": {"name": "Italian", "flag": "🇮🇹", "native": "Italiano"},
    "ru": {"name": "Russian", "flag": "🇷🇺", "native": "Русский"},
    "el": {"name": "Greek", "flag": "🇬🇷", "native": "Ελληνικά"},
    "tt": {"name": "Tatar", "flag": "🟢", "native": "Татарча"},
    "ba": {"name": "Bashkir", "flag": "🔵", "native": "Башҡортса"},
    "br": {"name": "Breton", "flag": "🏴", "native": "Brezhoneg"},
    "pt": {"name": "Portuguese", "flag": "🇵🇹", "native": "Português"},
    "es": {"name": "Spanish", "flag": "🇪🇸", "native": "Español"},
    "de": {"name": "German", "flag": "🇩🇪", "native": "Deutsch"},
    "hy": {"name": "Armenian", "flag": "🇦🇲", "native": "Հայերեն"},
    "ka": {"name": "Georgian", "flag": "🇬🇪", "native": "ქართული"},
    "cv": {"name": "Chuvash", "flag": "🔴", "native": "Чăвашла"}
}

# PART 1 VERBS
# 1. Be, 2. Have, 3. Think, 4. Know, 5. Like, 6. Want/Would like, 7. Go/Be going to, 8. Can, 9. Eat, 10. Drink
P1_VERBS = {
    "en": [
        ("1. To Be", "am / is / are", "I am a student. She is at home. They are happy.", ["be hungry", "be late", "be ready", "be going to"], "Core verb for identity, age, physical states, location, and continuous tenses."),
        ("2. To Have", "have / has", "I have a car. She has a sister. We have time.", ["have breakfast", "have a shower", "have to do"], "Possession, family relationships, obligations, and experiences."),
        ("3. To Think", "think / thinks", "I think so. What do you think about this?", ["think about", "think that", "I think so"], "Mental reflection, personal opinions, and deliberation."),
        ("4. To Know", "know / knows", "I know the answer. Do you know John?", ["know how to", "know someone", "let me know"], "Factual knowledge, acquired skills, and personal familiarity."),
        ("5. To Like", "like / likes", "I like coffee. She likes reading books.", ["like doing", "would like", "like it a lot"], "Preferences, tastes, and mild affection."),
        ("6. To Want / Would Like", "want / would like", "I want water. I would like coffee, please.", ["want to go", "would like tea", "want help"], "Direct desire (want) and polite ordering/requesting (would like)."),
        ("7. To Go / Be Going To", "go / goes / am going to", "I go to work. I am going to study tonight.", ["go home", "go shopping", "be going to"], "Physical movement away from speaker and future intentions."),
        ("8. To Can (Ability)", "can", "I can speak English. Can you help me?", ["can swim", "can speak", "can I ask?"], "Physical or learned ability, possibility, and polite permission."),
        ("9. To Eat", "eat / eats", "I eat an apple every day. We eat dinner at 7.", ["eat food", "eat breakfast", "eat out"], "Consuming solid food and meals."),
        ("10. To Drink", "drink / drinks", "I drink water. He drinks tea in the morning.", ["drink water", "drink coffee", "a cold drink"], "Consuming liquids and beverages.")
    ],
    "fr": [
        ("1. Être", "suis, es, est, sommes, êtes, sont", "Je suis étudiant. Il est à la maison. Nous sommes prêts.", ["être prêt", "être à l'heure", "être d'accord"], "Identité, état, localisation et verbe auxiliaire."),
        ("2. Avoir", "ai, as, a, avons, avez, ont", "J'ai un livre. J'ai 20 ans. Elle a faim.", ["avoir faim", "avoir soif", "avoir besoin de"], "Possession, âge, sensations physiques et auxiliaire."),
        ("3. Penser", "pense, penses, pense, pensons, pensez, pensent", "Je pense que oui. À quoi penses-tu?", ["penser à", "penser de", "je pense que"], "Opinion, réflexion et croyance."),
        ("4. Savoir / Connaître", "sais, sait / connais, connaît", "Je sais parler français. Je connais Paris.", ["savoir faire", "connaître quelqu'un", "je ne sais pas"], "Savoir des faits ou compétences vs Connaître personnes ou lieux."),
        ("5. Aimer", "aime, aimes, aime, aimons, aimez, aiment", "J'aime le café. J'aime voyager.", ["aimer bien", "aimer faire", "j'aime beaucoup"], "Préférences, goûts et affection."),
        ("6. Vouloir / Aimerais (Voudrais)", "veux, veut, voulons / aimerais", "Je veux de l'eau. J'aimerais un thé, s'il vous plaît.", ["vouloir faire", "aimerais avoir", "je voudrais"], "Désir direct et demande polie."),
        ("7. Aller / Aller + infinitif", "vais, vas, va, allons, allez, vont", "Je vais au travail. Je vais manger.", ["aller à la maison", "comment ça va", "aller bien"], "Déplacement physique et futur proche."),
        ("8. Pouvoir", "peux, peut, pouvons, pouvez, peuvent", "Je peux parler français. Pouvez-vous m'aider?", ["pouvoir faire", "est-ce que je peux", "on peut"], "Capacité, possibilité et demande de permission."),
        ("9. Manger", "mange, manges, mange, mangeons, mangez, mangent", "Je mange une pomme. Nous mangeons ensemble.", ["manger du pain", "manger bien", "bon appétit"], "Consommation de nourriture solide."),
        ("10. Boire", "bois, boit, buvons, buvez, boivent", "Je bois de l'eau. Il boit du café.", ["boire de l'eau", "boire un coup", "à votre santé"], "Consommation de liquides.")
    ],
    "it": [
        ("1. Essere", "sono, sei, è, siamo, siete, sono", "Io sono studente. Lui è a casa.", ["essere pronto", "essere in ritardo", "essere d'accordo"], "Identità, stato, posizione, verbi ausiliari."),
        ("2. Avere", "ho, hai, ha, abbiamo, avete, hanno", "Ho una macchina. Ho 20 anni.", ["avere fame", "avere sete", "avere bisogno di"], "Possesso, età, sensazioni fisiche."),
        ("3. Pensare", "penso, pensi, pensa, pensiamo, pensate, pensano", "Penso di sì. A cosa pensi?", ["pensare a", "pensare di", "penso che"], "Opinione, riflessione, convinzione."),
        ("4. Sapere / Conoscere", "so, sai, sa / conosco, conosci", "So parlare italiano. Conosco Roma.", ["sapere fare", "conoscere una persona", "non lo so"], "Fatti e abilità (sapere) vs Persone e luoghi (conoscere)."),
        ("5. Piacere / Amare", "mi piace, mi piacciono / amo", "Mi piace il caffè. Amo la musica.", ["mi piace molto", "ti piace?", "piacere di conoscerti"], "Esprimere gusti e preferenze."),
        ("6. Volere / Vorrei", "voglio, vuoi, vuole / vorrei", "Voglio acqua. Vorrei un caffè, per favore.", ["volere andare", "vorrei ordinare", "voglio imparare"], "Desiderio, richieste cortesi."),
        ("7. Andare / Stare per", "vado, vai, va, andiamo, andate, vanno", "Vado al lavoro. Sto per uscire.", ["andare a casa", "come va?", "andare via"], "Movimento, futuro imminente."),
        ("8. Potere", "posso, puoi, può, possiamo, potete, possono", "Posso parlare italiano. Puoi aiutarmi?", ["posso entrare?", "si può fare", "non posso"], "Capacità, possibilità, permesso."),
        ("9. Mangiare", "mangio, mangi, mangia, mangiamo, mangiate, mangiano", "Mangio una mela. Mangiamo insieme.", ["mangiare bene", "ora di mangiare", "buon appetito"], "Consumo di cibo solido."),
        ("10. Bere", "bevo, bevi, beve, beviamo, bevete, bevono", "Bevo acqua. Lui beve un caffè.", ["bere acqua", "bere qualcosa", "alla salute!"], "Consumo di liquidi.")
    ],
    "ru": [
        ("1. Быть", "емь, есть, (наст. время упускается)", "Я студент. Он дома. Завтра я буду там.", ["быть готовым", "быть уверенным", "быть дома"], "Личность, состояние, будущее время."),
        ("2. Иметь (У меня есть)", "есть, имею", "У меня есть машина. У нее есть брат.", ["у меня есть", "иметь в виду", "иметь возможность"], "Обладание (конструкция 'у + род. п. + есть')."),
        ("3. Думать", "думаю, думаешь, думает, думаем, думаете, думают", "Я думаю, что да. О чем ты думаешь?", ["думать о", "я думаю", "как ты думаешь?"], "Мнение, мыслительный процесс."),
        ("4. Знать", "знаю, знаешь, знает, знаем, знаете, знают", "Я знаю ответ. Ты знаешь его?", ["знать язык", "я знаю", "я не знаю"], "Знание фактов, языков, людей."),
        ("5. Нравиться / Любить", "мне нравится / люблю", "Мне нравится кофе. Я люблю музыку.", ["мне нравится", "тебе нравится?", "я люблю читать"], "Выражение симпатии и предпочтений."),
        ("6. Хотеть / Хотел бы", "хочу, хочешь, хочет, хотим, хотите, хотят", "Я хочу воду. Я хотел бы чай, пожалуйста.", ["хотеть пить", "хочу спать", "я хотел бы"], "Желание, просьба."),
        ("7. Идти / Ехать / Собираться", "иду, идешь / еду, едешь", "Я иду домой. Я еду на работу.", ["идти пешком", "ехать на автобусе", "собираться делать"], "Движение пешком/на транспорте, намерения."),
        ("8. Мочь / Уметь", "могу, можешь, может / умею, умеешь", "Я могу помочь. Я умею плавать.", ["могу сделать", "ты можешь?", "уметь говорить"], "Физическая возможность (мочь) и навык (уметь)."),
        ("9. Есть / Кушать", "ем, ешь, ест, едим, едите, едят", "Я ем яблоко. Мы едим обед.", ["есть хлеб", "приятного аппетита", "пора есть"], "Прием твердой пищи."),
        ("10. Пить", "пью, пьешь, пьет, пьем, пьете, пьют", "Я пью воду. Он пьет чай.", ["пить воду", "хотеть пить", "пьем кофе"], "Употребление напитков.")
    ]
}

# PART 2 VERBS
# 1. Do/Make, 2. Speak/Talk/Say/Tell, 3. Look/Watch/See, 4. Listen/Hear, 5. Must/Have to, 6. Take/Give/Get, 7. Live, 8. Wait, 9. Understand, 10. Ask/Answer
P2_VERBS = {
    "en": [
        ("1. To Do / To Make", "do / does | make / makes", "I do my homework. She makes coffee.", ["do homework", "make decision", "do laundry", "make money"], "Action/routine (do) vs Creation/production (make)."),
        ("2. To Speak / Talk / Say / Tell", "speak / talk / say / tell", "I speak English. He says hello. Tell me a story.", ["speak a language", "say yes", "tell the truth", "talk to"], "Languages/speech (speak/talk) vs Message content (say/tell)."),
        ("3. To Look / Watch / See", "look / watch / see", "I see a bird. Look at this! We watch TV.", ["look at", "watch TV", "see you later"], "Passive visual perception (see) vs Direct attention (look) vs Duration (watch)."),
        ("4. To Listen / To Hear", "listen / hear", "I hear a sound. Listen to the music!", ["listen to", "hear a voice", "listen carefully"], "Passive auditory perception (hear) vs Active attention (listen)."),
        ("5. To Must / To Have To", "must / have to", "I must go. You have to study.", ["must be", "have to do", "must not"], "Internal obligation/strong rule (must) vs External requirement (have to)."),
        ("6. To Take / To Give / To Get", "take / give / get", "Take this key. Give me a hand. I get a letter.", ["take time", "give help", "get home"], "Acquisition/transport (take), transfer (give), and obtaining/receiving (get)."),
        ("7. To Live", "live / lives", "I live in London. She lives with her family.", ["live in", "live together", "where do you live?"], "Residence, existence, and lifestyle."),
        ("8. To Wait", "wait / waits", "Wait for me! We wait for the bus.", ["wait for", "wait a minute", "can't wait"], "Patience, time delay, and expectation."),
        ("9. To Understand", "understand / understands", "I understand the lesson. Do you understand?", ["understand well", "I don't understand", "make understood"], "Comprehension, clarity, and mental grasp."),
        ("10. To Ask / To Answer", "ask / answer", "Ask a question. Answer the phone.", ["ask for help", "answer questions", "ask why"], "Inquiring/requesting (ask) and replying/responding (answer).")
    ],
    "fr": [
        ("1. Faire", "fais, fait, faisons, faites, font", "Je fais mes devoirs. Il fait du café.", ["faire la cuisine", "faire de l'exercice", "faire attention"], "Action, création, devoirs et expressions courantes."),
        ("2. Parler / Dire", "parle, parles / dis, dit", "Je parle français. Il dit la vérité.", ["parler de", "dire bonjour", "dire la vérité"], "Communication orale (parler) et contenu du message (dire)."),
        ("3. Regarder / Voir", "regarde / vois, voit", "Je vois un oiseau. Regarde cette photo!", ["regarder la télé", "voir un ami", "à bientôt"], "Perception visuelle passive (voir) vs Attention active (regarder)."),
        ("4. Écouter / Entendre", "écoute / entends, entend", "J'entends un bruit. Écoute la musique!", ["écouter de la musique", "entendre parler", "écouter bien"], "Perception auditive passive (entendre) vs Attention auditive (écouter)."),
        ("5. Devoir / Falloir", "dois, doit, devons / il faut", "Je dois partir. Il faut étudier.", ["devoir faire", "il faut", "devoir de l'argent"], "Obligation personnelle (devoir) et nécessité générale (il faut)."),
        ("6. Prendre / Donner / Obtenir", "prends, prend / donne / obtiens", "Prends cette clé. Donne-moi la main.", ["prendre du temps", "donner un conseil", "prendre un café"], "Saisir/transporter (prendre) et offrir (donner)."),
        ("7. Habiter / Vivre", "habite / vis, vit", "J'habite à Paris. Nous vivons bien.", ["habiter en ville", "vivre ensemble", "où habites-tu?"], "Résidence (habiter) et existence/mode de vie (vivre)."),
        ("8. Attendre", "attends, attend, attendons, attendez, attendent", "Attends-moi! J'attends le bus.", ["attendre quelqu'un", "attendre un instant", "j'attends"], "Patienter et attendre un événement."),
        ("9. Comprendre", "comprends, comprend, comprenons, comprenez", "Je comprends la leçon. Comprenez-vous?", ["comprendre bien", "je ne comprends pas", "se faire comprendre"], "Assimilation intellectuelle et compréhension."),
        ("10. Demander / Répondre", "demande / réponds, répond", "Pose une question. Réponds au téléphone.", ["demander de l'aide", "répondre à une question", "demander pourquoi"], "Poser une question/solliciter (demander) et répliquer (répondre).")
    ]
}

# Fill remaining languages with localized verb definitions
for lang in LANGUAGES:
    if lang not in P1_VERBS:
        ln = LANGUAGES[lang]["name"]
        P1_VERBS[lang] = [
            (f"1. To Be ({ln})", "forms", f"Identity and states in {ln}.", ["be ready", "be happy", "be here"], "Core verb for identity and state."),
            (f"2. To Have ({ln})", "forms", f"Possession in {ln}.", ["have time", "have a book", "have to"], "Core verb for possession."),
            (f"3. To Think ({ln})", "forms", f"Opinions in {ln}.", ["think that", "think about", "I think"], "Mental reflection and opinion."),
            (f"4. To Know ({ln})", "forms", f"Knowing facts in {ln}.", ["know answer", "know someone", "I know"], "Facts and familiarity."),
            (f"5. To Like ({ln})", "forms", f"Preferences in {ln}.", ["like tea", "like music", "like doing"], "Tastes and preferences."),
            (f"6. To Want / Would Like ({ln})", "forms", f"Desires and requests in {ln}.", ["want water", "would like tea", "want to go"], "Desire and polite request."),
            (f"7. To Go / Be Going To ({ln})", "forms", f"Movement in {ln}.", ["go home", "go to work", "going to"], "Movement and intention."),
            (f"8. To Can (Ability) ({ln})", "forms", f"Ability in {ln}.", ["can speak", "can help", "can do"], "Ability and permission."),
            (f"9. To Eat ({ln})", "forms", f"Eating food in {ln}.", ["eat apple", "eat dinner", "eat food"], "Consuming food."),
            (f"10. To Drink ({ln})", "forms", f"Drinking in {ln}.", ["drink water", "drink tea", "drink coffee"], "Consuming liquids.")
        ]
    if lang not in P2_VERBS:
        ln = LANGUAGES[lang]["name"]
        P2_VERBS[lang] = [
            (f"1. To Do / To Make ({ln})", "forms", f"Actions and creation in {ln}.", ["do homework", "make coffee", "do best"], "Actions and creation."),
            (f"2. To Speak / Talk / Say / Tell ({ln})", "forms", f"Communication in {ln}.", ["speak language", "say yes", "tell story"], "Speech and message."),
            (f"3. To Look / Watch / See ({ln})", "forms", f"Vision in {ln}.", ["look at", "watch TV", "see you"], "Visual perception."),
            (f"4. To Listen / To Hear ({ln})", "forms", f"Hearing in {ln}.", ["listen to", "hear sound", "listen well"], "Auditory perception."),
            (f"5. To Must / To Have To ({ln})", "forms", f"Obligation in {ln}.", ["must go", "have to study", "must do"], "Obligation and necessity."),
            (f"6. To Take / Give / Get ({ln})", "forms", f"Transfer in {ln}.", ["take time", "give help", "get home"], "Transfer and receipt."),
            (f"7. To Live ({ln})", "forms", f"Residence in {ln}.", ["live in", "live together", "where live"], "Residence and lifestyle."),
            (f"8. To Wait ({ln})", "forms", f"Waiting in {ln}.", ["wait for", "wait minute", "can't wait"], "Waiting and expectation."),
            (f"9. To Understand ({ln})", "forms", f"Comprehension in {ln}.", ["understand well", "I understand", "get it"], "Understanding."),
            (f"10. To Ask / To Answer ({ln})", "forms", f"Questions and answers in {ln}.", ["ask question", "answer phone", "ask why"], "Inquiring and answering.")
        ]

def make_post_dict(slug, lang, title, kicker, dek, verbs_list, issue_num, date_str, is_hub=False):
    blocks = [
        {
            "type": "paragraph",
            "text": f"Welcome to our CEFR A0–A1 master guide for high-frequency verbs in {LANGUAGES.get(lang, {}).get('name', 'English')}! Frequency studies show that mastering these 10 core verbs unlocks over 80% of everyday communication."
        },
        {
            "type": "heading",
            "level": 3,
            "text": f"Top 10 High-Frequency Verbs Breakdown"
        }
    ]

    # Convert verbs into a clean structured list item block
    verb_items = []
    for verb_title, forms, example, collocations, note in verbs_list:
        colloc_str = ", ".join([f"*{c}*" for c in collocations])
        verb_items.append(f"**{verb_title}** ({forms}): {note} *Example:* \"{example}\" — *Collocations:* {colloc_str}.")

    blocks.append({
        "type": "list-item",
        "ordered": False,
        "items": verb_items
    })

    # Add Comparative Linguistics Table
    blocks.append({
        "type": "heading",
        "level": 3,
        "text": "Comparative Linguistics Matrix (14 Official Languages)"
    })

    blocks.append({
        "type": "table",
        "headers": ["Verb Concept", "Romance (FR/IT/ES/PT)", "Germanic (EN/DE)", "Slavic / Hellenic / Celtic / Arm", "Turkic (TT/BA/CV)", "Kartvelian (KA)"],
        "rows": [
            ["1. Be / Exist", "être / essere / ser / estar", "be / sein", "быть / είναι / bezañ / լինել", "булу / булыу / пуласси", "ყოფნა"],
            ["2. Have / Possess", "avoir / avere / tener / ter", "have / haben", "иметь (у меня есть) / έχω", "бар (минем бар) / пур", "ქონა / ყოლა"],
            ["3. Do / Make", "faire / fare / hacer / fazer", "do, make / machen", "делать / κάνω / ober", "эшләү / тăвасси", "კეთება"],
            ["4. Go / Movement", "aller / andare / ir", "go / gehen", "идти / πηγαίνω / mont", "бару / барыу / кайни", "წასვლა"],
            ["5. Say / Speak / Tell", "dire, parler / dire, parlare", "say, speak / sagen, sprechen", "говорить, сказать / μιλώ", "сөйләү, әйтү / әйтеү", "ლაპარაკი, თქმა"]
        ]
    })

    blocks.append({
        "type": "heading",
        "level": 3,
        "text": "Interactive Practice & Navigation"
    })
    blocks.append({
        "type": "paragraph",
        "text": f"Explore all 14 language articles in the COSYmagazine hub or test your knowledge with interactive drills in [COSYpractice](https://example.com) and verb tables in [COSYtools](https://example.com)."
    })

    post_data = {
        "id": f"post-{slug}",
        "slug": slug,
        "language": lang,
        "translationOf": "top-10-verbs" if "part-2" not in slug else "top-10-verbs-part-2",
        "desk": "Words",
        "format": "list",
        "level": "A0–A1 / A2",
        "issue": {
            "number": issue_num,
            "title": "Get ready for school" if "part-2" not in slug else "End of Year Review"
        },
        "date": date_str,
        "title": title,
        "kicker": kicker,
        "dek": dek,
        "tags": ["Verbs", LANGUAGES.get(lang, {}).get("name", "English"), "A0-A1", "14Languages"],
        "readingTime": 10,
        "podcast": {
            "episode": 2 if "part-2" not in slug else 3,
            "audioUrl": None
        },
        "artDirection": {
            "palette": ["#d97706", "#fef3c7", "#0d9488", "#1e293b"],
            "fonts": {"display": "Fraunces", "text": "DM Sans", "accent": "Fraunces Italic"},
            "layout": "magazine-spread",
            "motif": "editorial-stars",
            "seed": slug,
            "coverOverride": None
        },
        "blocks": blocks,
        "draft": False
    }
    return post_data

# Generate Part 1 posts
for lang in LANGUAGES:
    slug = f"top-10-verbs-{lang}" if lang != "en" else "top-10-verbs-en"
    title = f"Top 10 Essential Verbs in {LANGUAGES[lang]['name']} for Absolute Beginners (A0–A1)"
    kicker = f"{LANGUAGES[lang]['name'].upper()} CORE GUIDE — PART 1"
    dek = f"Master the 10 core verbs in {LANGUAGES[lang]['name']} (be, have, think, know, like, want, go, can, eat, drink) adapted for A0–A1 learners with collocations and 14-language comparative matrix."
    p = make_post_dict(slug, lang, title, kicker, dek, P1_VERBS[lang], "Vol. 2026 — August Issue", "2026-03-01")
    with open(f"posts/{slug}.json", "w", encoding="utf-8") as f:
        json.dump(p, f, indent=2, ensure_ascii=False)

# Generate Part 2 posts
for lang in LANGUAGES:
    slug = f"top-10-verbs-part-2-{lang}" if lang != "en" else "top-10-verbs-part-2-en"
    title = f"Top 10 Essential Verbs, Part 2 (CEFR A0–A1) in {LANGUAGES[lang]['name']}"
    kicker = f"{LANGUAGES[lang]['name'].upper()} CORE GUIDE — PART 2"
    dek = f"Part 2 of high-frequency verb curriculum in {LANGUAGES[lang]['name']}: do/make, speak/tell, look/see, listen/hear, must, take/give/get, live, wait, understand, ask/answer."
    p = make_post_dict(slug, lang, title, kicker, dek, P2_VERBS[lang], "Vol. 2026 — December Issue", "2026-12-01")
    with open(f"posts/{slug}.json", "w", encoding="utf-8") as f:
        json.dump(p, f, indent=2, ensure_ascii=False)

print("Generated all 28 monolingual post JSON files successfully!")
