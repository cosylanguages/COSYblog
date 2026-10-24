// Structure guard for long-form lesson articles (e.g., "Top 10 verbs, part 1").
// It catches errors in hand-edited/generated lesson articles:
// broken deep links, quizzes with invalid answer index, unbalanced HTML, and missing diagram speech scripts.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';

const VERBS = ['be', 'have', 'think', 'know', 'like', 'want', 'go', 'can', 'eat', 'drink'];
const text = (b) => JSON.stringify(b);

const filesToTest = ['top-10-verbs-en.json', 'top-10-verbs-fr.json'];

for (const filename of filesToTest) {
  const fileUrl = new URL(`../posts/${filename}`, import.meta.url);
  if (!fs.existsSync(fileUrl)) continue;

  const post = JSON.parse(fs.readFileSync(fileUrl, 'utf8'));

  test(`[${filename}] every verb has its own anchored section, plus the intro and the wrap-up`, () => {
    const ids = post.blocks.filter((b) => b.type === 'heading' && b.id).map((b) => b.id);
    for (const id of ['start', ...VERBS.map((v) => `verb-${v}`), 'verb-together']) {
      assert.ok(ids.includes(id), `missing heading id "${id}" in ${filename}`);
    }
    assert.equal(new Set(ids).size, ids.length, `heading ids must be unique in ${filename}`);
  });

  test(`[${filename}] every #anchor linked from the article exists`, () => {
    const ids = new Set(post.blocks.filter((b) => b.type === 'heading' && b.id).map((b) => b.id));
    const links = [...text(post.blocks).matchAll(/href=\\"#([a-z0-9-]+)\\"/g)].map((m) => m[1]);
    assert.ok(links.length >= 10, `the verb map should link to every verb in ${filename}`);
    for (const l of links) assert.ok(ids.has(l), `link to #${l} has no matching heading id in ${filename}`);
  });

  test(`[${filename}] every verb section ends with a quiz that has a valid answer`, () => {
    const quizzes = post.blocks.filter((b) => b.type === 'quiz');
    assert.ok(quizzes.length >= 30, `expected a quiz per verb (got ${quizzes.length}) in ${filename}`);
    for (const q of quizzes) {
      assert.ok(Array.isArray(q.options) && q.options.length >= 2, `quiz needs options: ${q.question} in ${filename}`);
      assert.ok(Number.isInteger(q.correctIndex) && q.correctIndex >= 0 && q.correctIndex < q.options.length, `bad correctIndex: ${q.question} in ${filename}`);
      assert.ok(q.explanation && q.explanation.length > 10, `quiz needs an explanation: ${q.question} in ${filename}`);
      assert.equal(new Set(q.options).size, q.options.length, `duplicate options: ${q.question} in ${filename}`);
    }
    let verbsWithQuiz = 0;
    let current = null;
    const seen = new Set();
    for (const b of post.blocks) {
      if (b.type === 'heading' && b.id) current = b.id;
      if (b.type === 'quiz' && current) seen.add(current);
    }
    for (const v of VERBS) { assert.ok(seen.has(`verb-${v}`), `verb-${v} has no quiz in ${filename}`); verbsWithQuiz++; }
    assert.equal(verbsWithQuiz, 10);
  });

  test(`[${filename}] no leaked template syntax or placeholders`, () => {
    const all = text(post.blocks);
    for (const bad of ['undefined', '[object', 'NaN', '${', 'TODO', 'lorem']) {
      assert.ok(!all.includes(bad), `found "${bad}" in ${filename}`);
    }
  });

  test(`[${filename}] HTML blocks are balanced and diagrams carry a spoken description`, () => {
    const count = (s, re) => (s.match(re) || []).length;
    for (const b of post.blocks.filter((x) => x.type === 'paragraph' && /^</.test(x.text) && x.text !== '<hr>')) {
      for (const tag of ['div', 'figure', 'table', 'ul', 'ol']) {
        assert.equal(count(b.text, new RegExp(`<${tag}[\\s>]`, 'g')), count(b.text, new RegExp(`</${tag}>`, 'g')), `unbalanced <${tag}> in ${filename}: ${b.text.slice(0, 70)}`);
      }
      if (/<figure/.test(b.text)) assert.ok(b.say && b.say.length > 20, `diagram without a "say" description in ${filename}: ${b.text.slice(0, 70)}`);
    }
  });

  if (filename === 'top-10-verbs-en.json') {
    test(`[${filename}] the English edition carries the podcast episode so the page can embed it`, () => {
      assert.ok(post.podcast && post.podcast.externalUrl, 'podcast.externalUrl is required for the embedded player');
    });
  }
}
