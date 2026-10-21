import json

with open('posts/top-10-verbs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

html = data['blocks'][0]['text']

# 1. Construct Verb Map Component HTML
verb_map_html = """
<div class="verb-map-container">
    <h3 class="verb-map-title">🗺️ The COSY Interactive Verb Map & Network</h3>
    <p style="margin-bottom:1rem; color:var(--ink-secondary);">Frequency research shows that these 10 core verbs carry up to 80% of daily spoken output. Click any verb below to jump directly to its grammar traps, usage contexts, and building block collocations.</p>

    <div class="verb-map-grid">
        <a href="#v-be" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">1. To Be</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">🗣 Daily</span>
                    <span class="usage-badge">🎓 Grammar</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">be hungry</span>
                <span class="block-chip">be 25 years old</span>
                <span class="block-chip">be going to</span>
            </div>
        </a>

        <a href="#v-have" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">2. To Have</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">🗣 Daily</span>
                    <span class="usage-badge">💼 Business</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">have breakfast</span>
                <span class="block-chip">have a shower</span>
                <span class="block-chip">have to do</span>
            </div>
        </a>

        <a href="#v-do" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">3. To Do</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">🗣 Daily</span>
                    <span class="usage-badge">💼 Work</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">do homework</span>
                <span class="block-chip">do research</span>
                <span class="block-chip">do business</span>
            </div>
        </a>

        <a href="#v-make" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">4. To Make</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">🗣 Daily</span>
                    <span class="usage-badge">💬 Social</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">make a decision</span>
                <span class="block-chip">make progress</span>
                <span class="block-chip">make money</span>
            </div>
        </a>

        <a href="#v-go" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">5. To Go</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">✈ Travel</span>
                    <span class="usage-badge">🗣 Daily</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">go home</span>
                <span class="block-chip">go abroad</span>
                <span class="block-chip">go shopping</span>
            </div>
        </a>

        <a href="#v-come" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">6. To Come</span>
                    <span class="frequency-stars">★★★★☆</span>
                </div>
                <div>
                    <span class="usage-badge">✈ Travel</span>
                    <span class="usage-badge">💬 Social</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">come back</span>
                <span class="block-chip">come from</span>
                <span class="block-chip">come true</span>
            </div>
        </a>

        <a href="#v-say" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">7. To Say / Tell</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">💬 Social</span>
                    <span class="usage-badge">🗣 Daily</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">say hello</span>
                <span class="block-chip">tell a story</span>
                <span class="block-chip">tell the truth</span>
            </div>
        </a>

        <a href="#v-get" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">8. To Get</span>
                    <span class="frequency-stars">★★★★★</span>
                </div>
                <div>
                    <span class="usage-badge">🗣 Daily</span>
                    <span class="usage-badge">💼 Work</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">get tired</span>
                <span class="block-chip">get a job</span>
                <span class="block-chip">get home</span>
            </div>
        </a>

        <a href="#v-see" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">9. To See / Look</span>
                    <span class="frequency-stars">★★★★☆</span>
                </div>
                <div>
                    <span class="usage-badge">💬 Social</span>
                    <span class="usage-badge">🎓 Media</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">see you later</span>
                <span class="block-chip">look at</span>
                <span class="block-chip">watch TV</span>
            </div>
        </a>

        <a href="#v-know" class="verb-node-card">
            <div>
                <div class="verb-node-head">
                    <span class="verb-node-title">10. To Know</span>
                    <span class="frequency-stars">★★★★☆</span>
                </div>
                <div>
                    <span class="usage-badge">🎓 Mind</span>
                    <span class="usage-badge">🗣 Daily</span>
                </div>
            </div>
            <div class="building-block-chips">
                <span class="block-chip">know how to</span>
                <span class="block-chip">know someone</span>
                <span class="block-chip">let me know</span>
            </div>
        </a>
    </div>
</div>
"""

# 2. Construct CEFR Roadmap Table HTML
cefr_roadmap_html = """
<div style="margin:2rem 0;">
    <h3 class="editorial-heading">📈 CEFR Verb Progression Roadmap</h3>
    <p style="color:var(--ink-secondary); margin-bottom:1rem;">Targeting your verb study according to CEFR difficulty ensures you build a natural communicative foundation before tackling abstract vocabulary.</p>

    <table class="cefr-roadmap-table">
        <thead>
            <tr>
                <th>Level</th>
                <th>Core Verb Focus</th>
                <th>Communicative Capability</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="cefr-badge cefr-a0">A0</span></td>
                <td><strong>be, have, go, want</strong></td>
                <td>Survival needs, basic identity, age, physical states, immediate movement.</td>
            </tr>
            <tr>
                <td><span class="cefr-badge cefr-a1">A1</span></td>
                <td><strong>come, do, make, see, say, get</strong></td>
                <td>Daily routines, simple descriptions, origin, asking questions, basic transactions.</td>
            </tr>
            <tr>
                <td><span class="cefr-badge cefr-a2">A2</span></td>
                <td><strong>take, give, know, think, feel, work</strong></td>
                <td>Expressing preferences, past experiences, plans, workplace tasks, opinions.</td>
            </tr>
            <tr>
                <td><span class="cefr-badge cefr-b1">B1</span></td>
                <td><strong>achieve, improve, discuss, provide, allow</strong></td>
                <td>Storytelling, workplace discussions, explaining reasons, resolving simple issues.</td>
            </tr>
            <tr>
                <td><span class="cefr-badge cefr-b2">B2</span></td>
                <td><strong>acquire, maintain, facilitate, demonstrate, resolve</strong></td>
                <td>Professional negotiations, precise nuanced writing, academic debate, diplomacy.</td>
            </tr>
            <tr>
                <td><span class="cefr-badge cefr-c1">C1</span></td>
                <td><strong>perceive, articulate, advocate, scrutinize, synthesize</strong></td>
                <td>Native-level elegance, stylistic precision, rhetorical impact, rapid adaptation.</td>
            </tr>
        </tbody>
    </table>
</div>
"""

# Inject Verb Map & CEFR Roadmap right after the article introduction or before section #v-be
target_sub = '<section class="verb-section" id="v-be">'
updated_html = html.replace(target_sub, verb_map_html + cefr_roadmap_html + target_sub)

# Insert "Why this verb matters" callouts into verb sections
why_callouts = {
    'id="v-be"': '<div class="verb-why-box"><strong>💡 Why "To Be" Matters:</strong> You will use this verb for identity, age, feelings, physical states, location, and forming continuous tenses ("I am reading") across almost every language.</div>',
    'id="v-have"': '<div class="verb-why-box"><strong>💡 Why "To Have" Matters:</strong> Essential for possession, obligations ("have to"), bodily states (hunger/thirst in Romance languages), and compound tenses ("I have seen").</div>',
    'id="v-do"': '<div class="verb-why-box"><strong>💡 Why "To Do" Matters:</strong> The engine for questions, negatives, daily activities, chores, and non-creative tasks.</div>',
    'id="v-make"': '<div class="verb-why-box"><strong>💡 Why "To Make" Matters:</strong> Used whenever something is created, produced, or resulted in a new state or decision.</div>',
    'id="v-go"': '<div class="verb-why-box"><strong>💡 Why "To Go" Matters:</strong> Anchors travel, routines, invitations, future intentions ("going to"), and hundreds of idiomatic expressions.</div>',
    'id="v-come"': '<div class="verb-why-box"><strong>💡 Why "To Come" Matters:</strong> Connects origin, arrivals, returning home, and inviting people to join an event.</div>',
    'id="v-say"': '<div class="verb-why-box"><strong>💡 Why "To Say / Tell" Matters:</strong> Fundamental for reporting conversation, sharing stories, giving instructions, and asking for clarification.</div>',
    'id="v-get"': '<div class="verb-why-box"><strong>💡 Why "To Get" Matters:</strong> The ultimate Swiss-army knife verb in English, replacing receive, become, arrive, obtain, and fetch.</div>',
    'id="v-see"': '<div class="verb-why-box"><strong>💡 Why "To See / Look" Matters:</strong> Essential for visual perception, understanding ("I see!"), social meetings, and watching media.</div>',
    'id="v-know"': '<div class="verb-why-box"><strong>💡 Why "To Know" Matters:</strong> Distinguishes knowing facts vs. being familiar with people/places across languages (e.g. savoir vs connaître).</div>'
}

for verb_id, callout in why_callouts.items():
    if verb_id in updated_html:
        # insert callout inside verb-head or right after grammar note
        updated_html = updated_html.replace(f'<section class="verb-section" {verb_id}>\n        <div class="verb-head">', f'<section class="verb-section" {verb_id}>\n        {callout}\n        <div class="verb-head">')

data['blocks'][0]['text'] = updated_html

with open('posts/top-10-verbs.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated posts/top-10-verbs.json successfully!")
