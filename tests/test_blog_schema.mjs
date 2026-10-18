import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { validatePostSchema } = require('../scripts/validate-blog-schema.js');

test('validatePostSchema - Valid schema object passes validation', () => {
  const validPost = {
    id: 'post-test-001',
    slug: 'test-valid-post',
    language: 'en',
    translationOf: 'base-test-post',
    draft: false,
    desk: 'Words',
    format: 'essay',
    level: 'B1',
    issue: {
      number: 'Vol. 2026.10',
      title: "JY DM's birthday & His favs"
    },
    date: '2026-10-15',
    title: 'Test Valid Post Title',
    kicker: 'TEST KICKER',
    dek: 'This is a valid test post deck description.',
    tags: ['Test', 'Schema'],
    readingTime: 3,
    podcast: {
      episode: 1,
      audioUrl: 'audio/test-valid-post.mp3'
    },
    artDirection: {
      palette: ['#0d9488', '#faf7f2', '#1e293b'],
      fonts: {
        display: 'Fraunces',
        text: 'DM Sans',
        accent: 'Fraunces Italic'
      },
      layout: 'magazine-spread',
      motif: 'editorial-stars',
      seed: 'test-001',
      coverOverride: null
    },
    blocks: [
      {
        type: 'heading',
        level: 2,
        text: 'Test Heading',
        say: 'Test heading speech script',
        beat: { duration: 800, camera: 'zoom-in' }
      },
      {
        type: 'paragraph',
        text: 'Test paragraph content block.'
      },
      {
        type: 'table',
        headers: ['Column 1', 'Column 2'],
        rows: [['Cell 1', 'Cell 2']]
      }
    ]
  };

  const errors = validatePostSchema(validPost, 'test-valid-post');
  assert.equal(errors.length, 0, `Expected 0 errors, got: ${errors.join('; ')}`);
});

test('validatePostSchema - Invalid schema objects fail validation', () => {
  const invalidPost = {
    id: 'post-invalid',
    slug: 'invalid-post',
    language: 'unknown_lang',
    desk: 'Invalid Desk Name',
    format: 'unsupported_format',
    blocks: []
  };

  const errors = validatePostSchema(invalidPost, 'invalid-post');
  assert.ok(errors.length > 0, 'Expected validation errors for invalid schema object.');
});
