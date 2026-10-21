import json
import os

LANGUAGES = {
    "en": {"name": "English", "flag": "🇬🇧", "native": "English"},
    "fr": {"name": "French", "flag": "🇫🇷", "native": "Français"},
    "it": {"name": "Italian", "flag": "🇮🇹", "native": "Italiano"},
    "ru": {"name": "Russian", "flag": "🇷🇺", "native": "Русский"},
    "el": {"name": "Greek", "flag": "🇬🇷", "native": "Ελληνικά"},
    "tt": {"name": "Tatar", "flag": " Татарстан / 🇷🇺", "native": "Татарча"},
    "ba": {"name": "Bashkir", "flag": " Башкортостан / 🇷🇺", "native": "Башҡортса"},
    "br": {"name": "Breton", "flag": "🏴", "native": "Brezhoneg"},
    "pt": {"name": "Portuguese", "flag": "🇵🇹", "native": "Português"},
    "es": {"name": "Spanish", "flag": "🇪🇸", "native": "Español"},
    "de": {"name": "German", "flag": "🇩🇪", "native": "Deutsch"},
    "hy": {"name": "Armenian", "flag": "🇦🇲", "native": "Հայերեն"},
    "ka": {"name": "Georgian", "flag": "🇬🇪", "native": "ქართული"},
    "cv": {"name": "Chuvash", "flag": " Чăвашла / 🇷🇺", "native": "Чăвашла"}
}

# Clean flag string for JSON
LANG_FLAGS = {
    "en": "🇬🇧", "fr": "🇫🇷", "it": "🇮🇹", "ru": "🇷🇺", "el": "🇬🇷",
    "tt": "🟢", "ba": "🔵", "br": "🏴", "pt": "🇵🇹", "es": "🇪🇸",
    "de": "🇩🇪", "hy": "🇦🇲", "ka": "🇬🇪", "cv": "🔴"
}

# Target Verbs definitions per language for Part 1
# 1. Be, 2. Have, 3. Think, 4. Know, 5. Like, 6. Want/Would like, 7. Go/Be going to, 8. Can (ability), 9. Eat, 10. Drink
PART1_VERBS = {
    "en": [
        {"verb": "To Be", "forms": "am / is / are", "meaning": "identity, state, location", "examples": ["I am happy.", "She is at home."], "collocations": ["be hungry", "be late", "be ready"]},
        {"verb": "To Have", "forms": "have / has", "meaning": "possession, experience", "examples": ["I have a car.", "He has a dog."], "collocations": ["have breakfast", "have time", "have a shower"]},
        {"verb": "To Think", "forms": "think / thinks", "meaning": "opinion, mental process", "examples": ["I think so.", "What do you think?"], "collocations": ["think about", "think that", "I think so"]},
        {"verb": "To Know", "forms": "know / knows", "meaning": "facts, familiarity", "examples": ["I know the answer.", "Do you know him?"], "collocations": ["know how to", "know a place", "I don't know"]},
        {"verb": "To Like", "forms": "like / likes", "meaning": "preference, enjoyment", "examples": ["I like coffee.", "She likes reading."], "collocations": ["like music", "would like to", "like it a lot"]},
        {"verb": "To Want / Would Like", "forms": "want / would like", "meaning": "desire, request", "examples": ["I want water.", "I would like tea, please."], "collocations": ["want to go", "would like a cup", "want help"]},
        {"verb": "To Go / Be Going To", "forms": "go / goes / am going to", "meaning": "movement, future plans", "examples": ["I go to work.", "I am going to sleep."], "collocations": ["go home", "go to bed", "be going to do"]},
        {"verb": "To Can (Ability)", "forms": "can", "meaning": "ability, possibility, permission", "examples": ["I can speak English.", "Can you help me?"], "collocations": ["can swim", "can speak", "can I ask?"]},
        {"verb": "To Eat", "forms": "eat / eats", "meaning": "consuming solid food", "examples": ["I eat an apple every day.", "We eat dinner at 7."], "collocations": ["eat food", "eat breakfast", "eat out"]},
        {"verb": "To Drink", "forms": "drink / drinks", "meaning": "consuming liquids", "examples": ["I drink water.", "He drinks tea."], "collocations": ["drink water", "drink coffee", "a cold drink"]}
    ],
    "fr": [
        {"verb": "Être", "forms": "suis, es, est, sommes, êtes, sont", "meaning": "identité, état, localisation", "examples": ["Je suis étudante.", "Il est à la maison."], "collocations": ["être prêt", "être à l'heure", "être d'accord"]},
        {"verb": "Avoir", "forms": "ai, as, a, avons, avez, ont", "meaning": "possession, âge, faim/soif", "examples": ["J'ai un livre.", "J'ai 20 ans."], "collocations": ["avoir faim", "avoir soif", "avoir besoin de"]},
        {"verb": "Penser", "forms": "pense, penses, pense, pensons, pensez, pensent", "meaning": "opinion, réflexion", "examples": ["Je pense que oui.", "À quoi penses-tu?"], "collocations": ["penser à", "penser de", "je pense que"]},
        {"verb": "Savoir / Connaître", "forms": "sais, sait / connais, connaît", "meaning": "faits (savoir), personnes/lieux (connaître)", "examples": ["Je sais parler français.", "Je connais Paris."], "collocations": ["savoir faire", "connaître quelqu'un", "je ne sais pas"]},
        {"verb": "Aimer", "forms": "aime, aimes, aime, aimons, aimez, aiment", "meaning": "préférence, affection", "examples": ["J'aime le café.", "J'aime voyager."], "collocations": ["aimer bien", "aimer faire", "j'aime beaucoup"]},
        {"verb": "Vouloir / Aimerais", "forms": "veux, veut, voulons / aimerais", "meaning": "désir, politesse", "examples": ["Je veux de l'eau.", "J'aimerais un thé, s'il vous plaît."], "collocations": ["vouloir faire", "aimerais avoir", "je voudrais"]},
        {"verb": "Aller", "forms": "vais, vas, va, allons, allez, vont", "meaning": "déplacement, futur proche", "examples": ["Je vais au travail.", "Je vais manger."], "collocations": ["aller à la maison", "comment ça va", "aller bien"]},
        {"verb": "Pouvoir", "forms": "peux, peut, pouvons, pouvez, peuvent", "meaning": "capacité, possibilité", "examples": ["Je peux parler français.", "Pouvez-vous m'aider?"], "collocations": ["pouvoir faire", "est-ce que je peux", "on peut"]},
        {"verb": "Manger", "forms": "mange, manges, mange, mangeons, mangez, mangent", "meaning": "consommer de la nourriture", "examples": ["Je mange une pomme.", "Nous mangeons ensemble."], "collocations": ["manger du pain", "manger bien", "donner à manger"]},
        {"verb": "Boire", "forms": "bois, boit, buvons, buvez, boivent", "meaning": "consommer des liquides", "examples": ["Je bois de l'eau.", "Il boit du thé."], "collocations": ["boire un café", "boire de l'eau", "donner à boire"]}
    ]
}

print("Script template ready")
