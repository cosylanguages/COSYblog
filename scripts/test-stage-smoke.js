const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const PORT = 8092;
const ROOT = path.resolve(__dirname, '..');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml'
};

function startServer() {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      let reqPath = decodeURIComponent(req.url.split('?')[0]);
      let filePath = path.join(ROOT, reqPath);

      if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }

      if (!fs.existsSync(filePath)) {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
        return;
      }

      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';

      fs.readFile(filePath, (err, content) => {
        if (err) {
          res.writeHead(500, { 'Content-Type': 'text/plain' });
          res.end('500 Internal Server Error');
        } else {
          res.writeHead(200, { 'Content-Type': contentType });
          res.end(content);
        }
      });
    });

    server.listen(PORT, () => resolve(server));
    server.on('error', reject);
  });
}

const POST_SLUGS = [
  'replace-very-50-stronger-adjectives',
  'stop-translating-10-sentence-frames',
  'top-10-verb-synonyms-intermediate-plateau'
];

async function runStageSmokeTests() {
  console.log('🧪 Starting Stage Mode Smoke Tests...');
  const server = await startServer();
  console.log(`🌐 Server running at http://localhost:${PORT}/`);

  const browser = await chromium.launch({ headless: true });
  let totalErrors = 0;

  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

    for (const slug of POST_SLUGS) {
      console.log(`\n--- Testing Post in Stage Mode: "${slug}" ---`);
      const pageErrors = [];
      page.on('pageerror', (err) => pageErrors.push(err.message));

      // 1. Test Stage Mode (?stage=1)
      const stageUrl = `http://localhost:${PORT}/blog/${slug}.html?stage=1`;
      await page.goto(stageUrl, { waitUntil: 'networkidle' });

      await page.waitForSelector('.stage-frame-16-9', { timeout: 10000 });
      console.log(`  ✓ Stage frame visible`);

      // Advance 5 beats using Next button
      for (let i = 0; i < 5; i++) {
        await page.click('#btn-next');
        await page.waitForTimeout(100);
      }

      const activeCounterText = await page.evaluate(() => {
        return document.querySelector('#beat-counter')?.textContent || '';
      });
      console.log(`  ✓ Advanced beats, counter: "${activeCounterText}"`);

      if (pageErrors.length > 0) {
        console.error(`❌ [${slug}] Page errors in stage mode:`, pageErrors);
        totalErrors += pageErrors.length;
      } else {
        console.log(`  ✅ [${slug}] Stage mode passed without errors.`);
      }

      // 2. Test Teleprompter Script Mode (?script=1)
      console.log(`\n--- Testing Post in Script Mode: "${slug}" ---`);
      const scriptUrl = `http://localhost:${PORT}/blog/${slug}.html?script=1`;
      await page.goto(scriptUrl, { waitUntil: 'networkidle' });

      await page.waitForSelector('.teleprompter-wrapper', { timeout: 10000 });
      console.log(`  ✅ [${slug}] Script mode loaded successfully.`);
    }
  } finally {
    await browser.close();
    server.close();
  }

  if (totalErrors > 0) {
    console.error(`\n❌ Stage mode smoke test failed with ${totalErrors} errors.`);
    process.exit(1);
  } else {
    console.log('\n🎉 All Stage Mode Smoke Tests Passed Successfully!');
  }
}

runStageSmokeTests().catch(err => {
  console.error('❌ Stage smoke test execution failed:', err);
  process.exit(1);
});
