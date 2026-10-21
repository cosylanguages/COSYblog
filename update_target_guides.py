import json
import os

target_files = [
    ("posts/demystifying-french-tenses-timeline-guide-fr.json", "fr", "Système des Temps Français", "Passé", "PRÉSENT", "Futur"),
    ("posts/demystifying-italian-tenses-timeline-guide-it.json", "it", "Sistema dei Tempi Italiani", "Passato", "PRESENTE", "Futuro"),
    ("posts/demystifying-russian-tenses-timeline-guide-ru.json", "ru", "Система Времен и Аспектов Русского Языка", "Прошлое", "НАСТОЯЩЕЕ", "Будущее"),
    ("posts/demystifying-greek-tenses-timeline-guide-el.json", "el", "Σύστημα Χρόνων της Ελληνικής Γλώσσας", "Παρελθόν", "ΤΩΡΑ", "Μέλλον")
]

for filepath, lang, title_label, past_lbl, now_lbl, fut_lbl in target_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Check if cosy-timeline is already embedded
    has_timeline = any("cosy-timeline" in json.dumps(b) for b in data.get("blocks", []))
    if not has_timeline:
        # Add visual timeline block after introduction
        timeline_block = {
            "type": "paragraph",
            "text": f"""<div class="cosy-timeline">
    <div class="timeline-labels">
        <span class="timeline-past-label">{past_lbl} 🕰️</span>
        <span class="timeline-now-label">● {now_lbl}</span>
        <span class="timeline-future-label">{fut_lbl} 🚀</span>
    </div>
    <div class="timeline-line">
        <div class="timeline-event" style="left:35%; width:30%;">
            <div class="timeline-bar"></div>
            <div class="timeline-card">
                <strong>{title_label}</strong>
                <p>Visual Chronological Spectrum & Aspect Progression</p>
            </div>
        </div>
        <div class="timeline-now"></div>
    </div>
</div>"""
        }
        data["blocks"].insert(2, timeline_block)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {filepath} with timeline block.")
