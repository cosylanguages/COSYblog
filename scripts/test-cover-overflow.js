#!/usr/bin/env node
/**
 * scripts/test-cover-overflow.js
 * Renders SVG covers for all blog post JSON files and multi-script test cases,
 * verifying that titles wrap and shrink properly without overflowing viewBox bounds.
 *
 * Usage: node scripts/test-cover-overflow.js
 */

const fs = require('fs');
const path = require('path');

const POSTS_DIR = path.join(__dirname, '..', 'posts');

const MULTI_SCRIPT_TEST_POSTS = [
  {
    title: "Stop Saying These 50 Phrases! Natural Conversational Upgrades for Intermediate English",
    slug: "test-latin-long",
    language: "en"
  },
  {
    title: "Чрезвычайно длинный заголовок на русском языке для проверки автоматического переноса строк и уменьшения шрифта без обрезки",
    slug: "test-cyrillic-long",
    language: "ru"
  },
  {
    title: "Εξαιρετικά μεγάλος τίτλος στα ελληνικά για τη δοκιμή αυτόματης προσαρμογής κειμένου και αποφυγής υπερχείλισης",
    slug: "test-greek-long",
    language: "el"
  },
  {
    title: "ძალიან გრძელი სათაური ქართულად ტექსტის ავტომატური გადატანის და შრიფტის ზომის შემცირების შესამოწმებლად",
    slug: "test-georgian-long",
    language: "ka"
  },
  {
    title: "Չափազանց երկար վերնագիր հայերենով տեքստի տեղավորման և տողադարձի ստուգման համար առանց կտրման",
    slug: "test-armenian-long",
    language: "hy"
  }
];

async function runCoverOverflowTest() {
  console.log('🧪 Testing SVG cover rendering and text container safe bounds...');

  const { renderCover } = await import('../js/art/generator.js');

  const postsToTest = [];

  // Load all JSON posts
  if (fs.existsSync(POSTS_DIR)) {
    const jsonFiles = fs.readdirSync(POSTS_DIR).filter(f => f.endsWith('.json'));
    jsonFiles.forEach(file => {
      const data = JSON.parse(fs.readFileSync(path.join(POSTS_DIR, file), 'utf-8'));
      postsToTest.push(data);
    });
  }

  // Append multi-script synthetic benchmarks
  postsToTest.push(...MULTI_SCRIPT_TEST_POSTS);

  console.log(`📋 Testing ${postsToTest.length} post cover(s)...`);

  let failures = 0;

  postsToTest.forEach((post) => {
    const width = 800;
    const height = 450;
    const svg = renderCover(post, { width, height, showText: true });

    if (!svg || !svg.includes('<svg')) {
      console.error(`❌ [${post.slug}] Failed to generate SVG.`);
      failures++;
      return;
    }

    // Parse Y attributes in rendered text nodes to check overflow
    const textYMatches = Array.from(svg.matchAll(/<text [^>]*y="(\d+)"[^>]*>/g)).map(m => parseInt(m[1], 10));

    // Parse rect attributes in cover-text-overlay box
    const overlayBoxMatch = svg.match(/<rect [^>]*class="cover-overlay-box"[^>]*y="(\d+)"[^>]*height="(\d+)"[^>]*\/>/);

    if (textYMatches.length > 0 && overlayBoxMatch) {
      const rectY = parseInt(overlayBoxMatch[1], 10);
      const rectHeight = parseInt(overlayBoxMatch[2], 10);
      const rectBottom = rectY + rectHeight;

      const maxTextY = Math.max(...textYMatches);

      if (maxTextY > rectBottom) {
        console.error(`❌ [${post.slug}] Text Y (${maxTextY}px) overflows text box bottom (${rectBottom}px).`);
        failures++;
        return;
      }

      if (rectBottom > height) {
        console.error(`❌ [${post.slug}] Text box bottom (${rectBottom}px) overflows SVG height (${height}px).`);
        failures++;
        return;
      }
    }

    console.log(`  ✓ [${post.slug}] Motif: ${post.artDirection?.motif || 'auto'} (${post.language || 'en'}) — OK`);
  });

  if (failures > 0) {
    console.error(`\n❌ Cover Overflow Test FAILED with ${failures} error(s).`);
    process.exit(1);
  } else {
    console.log(`\n✅ All ${postsToTest.length} post covers passed bounds and text container fit verification!`);
  }
}

if (require.main === module) {
  runCoverOverflowTest().catch(err => {
    console.error('Fatal error in cover overflow test:', err);
    process.exit(1);
  });
}

module.exports = { runCoverOverflowTest };
