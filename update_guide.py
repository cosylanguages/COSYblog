import json

with open("posts/demystifying-english-tenses-timeline-guide.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Re-structure blocks to move meat up, add signature timeline, 12 tense timelines, comparisons, common mistakes, practice
blocks = []

# 0. Culture Bite (Founder's Letter)
blocks.append(data["blocks"][0])

# 1. Headline & Immediate Master Timeline
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "The Signature COSY Master Timeline: All 12 Tenses at a Glance",
    "say": "Here is our signature master timeline showing how all twelve English tenses exist simultaneously on a single temporal spectrum."
})

blocks.append({
    "type": "paragraph",
    "text": """<div class="cosy-master-timeline">
    <h3 class="master-timeline-title">🗺️ Signature COSY Master Timeline: Visualizing All 12 Tenses</h3>
    <div class="master-timeline-rows">
        <div class="master-timeline-row">
            <span class="master-row-label">Past Perfect Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:2%; width:26%; background:#f97316;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Past Perfect</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:6%; width:20%; background:#f97316;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Past Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:14%; width:16%; background:#f97316;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Past Simple</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:18%; width:5%; background:#f97316;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Present Perfect Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:28%; width:24%; background:#3B82F6;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Present Perfect</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:34%; width:18%; background:#3B82F6;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Present Simple</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:48%; width:4%; background:#3B82F6;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Present Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:49%; width:12%; background:#3B82F6;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Future Simple</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:55%; width:6%; background:#10b981;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Future Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:55%; width:18%; background:#10b981;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Future Perfect</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:55%; width:26%; background:#10b981;"></div>
            </div>
        </div>
        <div class="master-timeline-row">
            <span class="master-row-label">Future Perfect Continuous</span>
            <div class="master-row-track">
                <div class="master-row-now"></div>
                <div class="master-row-bar" style="left:55%; width:34%; background:#10b981;"></div>
            </div>
        </div>
    </div>
</div>"""
})

# Helper function to generate a timeline HTML block
def timeline_html(title, desc, left, width, event_class=""):
    return f"""<div class="cosy-timeline">
    <div class="timeline-labels">
        <span class="timeline-past-label">Past 🕰️</span>
        <span class="timeline-now-label">● NOW</span>
        <span class="timeline-future-label">Future 🚀</span>
    </div>
    <div class="timeline-line">
        <div class="timeline-event {event_class}" style="left:{left}; width:{width};">
            <div class="timeline-bar"></div>
            <div class="timeline-card">
                <strong>{title}</strong>
                <p>{desc}</p>
            </div>
        </div>
        <div class="timeline-now"></div>
    </div>
</div>"""

# 2. Section 1: The Present Tenses
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "1. The Present Cluster (Anchored At or Surrounding NOW)",
    "say": "Let's examine the four Present tenses. Notice how each tense positions itself relative to the central NOW marker."
})

# Present Simple
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Present Simple (Habit / Routine / Permanent Truth)",
    "say": "Present Simple represents timeless truths, regular habits, or permanent states."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Present Simple", "Habitual state or general truth<br><em>'The team completed the audit daily.'</em>", "48%", "4%")
})
blocks.append({
    "type": "example",
    "targetText": "Engineers debug systems every morning.",
    "gloss": "Regular daily routine / general fact",
    "context": "Professional habit"
})

# Present Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Present Continuous (Live Action in Progress)",
    "say": "Present Continuous represents an ongoing action active right now around the present moment."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Present Continuous", "Ongoing action happening right now<br><em>'Engineers are debugging the system.'</em>", "49%", "12%")
})
blocks.append({
    "type": "example",
    "targetText": "She is presenting the quarterly report right now.",
    "gloss": "Active live duration unfolding NOW",
    "context": "Meeting in progress"
})

# Present Perfect
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Present Perfect (Started Before Now, Relevant NOW)",
    "say": "Present Perfect creates a bridge: an action occurred in the past, but its result or relevance is active right now."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Present Perfect", "Started before now<br>Still relevant or active result NOW", "34%", "18%")
})
blocks.append({
    "type": "example",
    "targetText": "We have updated the server security protocol.",
    "gloss": "Past action with active present status (the server is safe NOW)",
    "context": "Project update"
})

# Present Perfect Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Present Perfect Continuous (Unbroken Duration Up To NOW)",
    "say": "Present Perfect Continuous emphasizes unbroken time and energy spent leading directly into the present."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Present Perfect Continuous", "Continuous duration leading directly up to NOW<br><em>'I have been writing for 3 hours.'</em>", "28%", "24%")
})
blocks.append({
    "type": "example",
    "targetText": "The archivist has been compiling manuscripts since 9 AM.",
    "gloss": "Emphasizes duration and effort up to current moment",
    "context": "Work in progress"
})

# 3. Section 2: The Past Tenses
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "2. The Past Cluster (Completed Before NOW)",
    "say": "Now let's explore the four Past tenses. All four reside to the left of the NOW anchor line."
})

# Past Simple
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Past Simple (Closed Historical Fact)",
    "say": "Past Simple is a single completed dot or interval in finished past time."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Past Simple", "Completed action in finished time<br><em>'She submitted the application yesterday.'</em>", "18%", "5%", "event-past")
})
blocks.append({
    "type": "example",
    "targetText": "The board approved the budget last Tuesday.",
    "gloss": "Single completed event in closed past time",
    "context": "Finished event"
})

# Past Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Past Continuous (Background Scene / Interrupted Action)",
    "say": "Past Continuous paints a continuous background action in progress at a specific past moment."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Past Continuous", "Ongoing past action interrupted by an event<br><em>'We were reviewing data when the light failed.'</em>", "14%", "16%", "event-past")
})
blocks.append({
    "type": "example",
    "targetText": "Analysts were evaluating market trends during Q3.",
    "gloss": "Continuous duration in past background",
    "context": "Scene setting"
})

# Past Perfect
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Past Perfect (The 'Past Before Past')",
    "say": "Past Perfect establishes sequence: Event A happened BEFORE Event B in the past."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Past Perfect", "Action completed BEFORE another past event<br><em>'The team had finished the draft before deadline.'</em>", "6%", "20%", "event-past")
})
blocks.append({
    "type": "example",
    "targetText": "The researchers had gathered all data prior to publication.",
    "gloss": "First past action completed prior to second past milestone",
    "context": "Temporal ordering"
})

# Past Perfect Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Past Perfect Continuous (Extended Duration Leading Up to a Past Point)",
    "say": "Past Perfect Continuous measures duration and effort accumulated before a past moment."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Past Perfect Continuous", "Unbroken duration leading up to a past milestone<br><em>'They had been negotiating for weeks.'</em>", "2%", "26%", "event-past")
})

# 4. Section 3: The Future Tenses
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "3. The Future Cluster (Projected After NOW)",
    "say": "Finally, let's explore the four Future tenses, residing to the right of the NOW anchor line."
})

# Future Simple
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Future Simple (Prediction / Instant Decision)",
    "say": "Future Simple projects a decision, promise, or prediction after NOW."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Future Simple", "Decision or prediction after NOW<br><em>'We will launch the campaign tomorrow.'</em>", "55%", "6%", "event-future")
})

# Future Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Future Continuous (Action In Progress at a Specific Future Moment)",
    "say": "Future Continuous places our camera frame at a specific moment in the future."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Future Continuous", "Ongoing action at a future timestamp<br><em>'This time tomorrow, I will be flying.'</em>", "55%", "18%", "event-future")
})

# Future Perfect
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Future Perfect (Completion Prior to a Future Deadline)",
    "say": "Future Perfect looks back from a future deadline to confirm completion."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Future Perfect", "Action completed BEFORE a future deadline<br><em>'By 5 PM, we will have signed the contract.'</em>", "55%", "26%", "event-future")
})

# Future Perfect Continuous
blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Future Perfect Continuous (Duration Accumulated Up to a Future Milestone)",
    "say": "Future Perfect Continuous measures total duration accumulated up to a future milestone."
})
blocks.append({
    "type": "paragraph",
    "text": timeline_html("Future Perfect Continuous", "Duration accumulated up to a future milestone<br><em>'By December, I will have been working 10 years.'</em>", "55%", "34%", "event-future")
})

# 5. Crucial Tense Comparisons
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "Crucial Tense Comparisons: Solving Common Learner Dilemmas",
    "say": "The biggest struggle for intermediate learners isn't individual tense formulas—it's choosing between similar tenses. Let's compare them directly."
})

blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Comparison 1: Present Perfect vs. Past Simple",
    "say": "Present Perfect keeps the door open to NOW, whereas Past Simple closes the door in finished past time."
})
blocks.append({
    "type": "table",
    "headers": ["Aspect / Feature", "Present Perfect ('I have lived in London')", "Past Simple ('I lived in London')"],
    "rows": [
        ["Connection to NOW", "Active link to present (I still live there OR experience matters NOW)", "No connection to NOW (I no longer live there / finished time)"],
        ["Time Markers Used", "Unfinished time: 'so far', 'already', 'this week', 'ever'", "Finished time: 'yesterday', 'in 2018', '2 years ago', 'last night'"],
        ["Timeline Shape", "Bridge extending from past to NOW marker", "Closed dot or isolated interval in the past"]
    ],
    "caption": "Direct Comparison: Present Perfect vs. Past Simple"
})

blocks.append({
    "type": "heading",
    "level": 3,
    "text": "Comparison 2: Past Continuous vs. Past Simple",
    "say": "Past Continuous provides the continuous background canvas, while Past Simple provides the interrupting foreground event."
})
blocks.append({
    "type": "example",
    "targetText": "While engineers were debugging the system, power failed.",
    "gloss": "Past Continuous = ongoing background wave; Past Simple = sudden single interruption point",
    "context": "Narrative structure"
})

# 6. Common Learner Mistakes & How Timelines Fix Them
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "Common Learner Mistakes: Timeline Diagnostics",
    "say": "Let's diagnose and fix classic non-native errors using visual timeline logic."
})

blocks.append({
    "type": "paragraph",
    "text": """<div class="phrase-upgrade-grid">
    <div class="phrase-upgrade-card">
        <span class="flow-step-bad">❌ "I am living here since 2019."</span> → <span class="flow-step-good">✅ "I have been living here since 2019."</span>
        <br><small><strong>Why?</strong> Present Continuous cannot connect past starting points ('since 2019') to now. Only Present Perfect Continuous bridges duration from a past date to NOW.</small>
    </div>
    <div class="phrase-upgrade-card">
        <span class="flow-step-bad">❌ "Yesterday I have submitted the report."</span> → <span class="flow-step-good">✅ "Yesterday I submitted the report."</span>
        <br><small><strong>Why?</strong> 'Yesterday' is a closed finished past time marker. Closed past time requires Past Simple, never Present Perfect.</small>
    </div>
    <div class="phrase-upgrade-card">
        <span class="flow-step-bad">❌ "When I arrived, the meeting already started."</span> → <span class="flow-step-good">✅ "When I arrived, the meeting had already started."</span>
        <br><small><strong>Why?</strong> Since the meeting started prior to my arrival, Past Perfect ('had started') is needed to show the 'past before past' sequence.</small>
    </div>
</div>"""
})

# 7. Practice Micro-Exercises
blocks.append({
    "type": "heading",
    "level": 2,
    "text": "Immediate Practice Micro-Quiz",
    "say": "Test your mental timeline model with this immediate micro-quiz."
})

blocks.append({
    "type": "quiz",
    "question": "Which tense best describes an action that started in the past, continued for 3 hours, and is still actively continuing right NOW?",
    "options": [
        "Past Continuous ('I was writing')",
        "Present Perfect Continuous ('I have been writing')",
        "Past Perfect Continuous ('I had been writing')",
        "Future Continuous ('I will be writing')"
    ],
    "correctIndex": 1,
    "explanation": "Present Perfect Continuous ('I have been writing') connects past duration directly up to and including the present moment.",
    "say": "Which tense connects past duration directly to the present moment?"
})

# Add remaining overview sections from original guide
blocks.append(data["blocks"][-3]) # Spoken vs Academic table
blocks.append(data["blocks"][-2]) # Quiz
blocks.append(data["blocks"][-1]) # Summary Action Plan

data["blocks"] = blocks

with open("posts/demystifying-english-tenses-timeline-guide.json", "w", encoding="utf-8") as f:
    json.load_file = json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated posts/demystifying-english-tenses-timeline-guide.json successfully.")
