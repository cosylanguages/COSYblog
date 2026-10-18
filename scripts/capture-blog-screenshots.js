/**
 * scripts/capture-blog-screenshots.js
 * Captures Playwright screenshots for 3 desks at 1280px (desktop) and 390px (mobile) viewports.
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function captureScreenshots() {
  console.log('📸 Capturing blog screenshots...');
  const browser = await chromium.launch();
  const outputDir = path.join(__dirname, '..', 'screenshots');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // 3 distinct desks:
  // 1. Words desk: blog/replace-50-overused-phrases.html
  // 2. Grammar Made Cosy desk: blog/top-5-favourite-grammar-rules.html
  // 3. Front Page desk: blog/welcome-to-cosy-blog.html

  const pagesToCapture = [
    { desk: 'words', file: 'blog/replace-50-overused-phrases.html' },
    { desk: 'grammar', file: 'blog/top-5-favourite-grammar-rules.html' },
    { desk: 'front_page', file: 'blog/welcome-to-cosy-blog.html' }
  ];

  for (const item of pagesToCapture) {
    const filePath = path.join(__dirname, '..', item.file);
    const fileUrl = `file://${filePath}`;

    // Desktop viewport (1280x800)
    const contextDesktop = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const pageDesktop = await contextDesktop.newPage();
    await pageDesktop.goto(fileUrl, { waitUntil: 'load' });
    await pageDesktop.waitForTimeout(500); // let flipbook js initialize
    const desktopScreenshotPath = path.join(outputDir, `${item.desk}-desktop-1280.png`);
    await pageDesktop.screenshot({ path: desktopScreenshotPath, fullPage: false });
    console.log(`  ✓ Saved ${desktopScreenshotPath}`);
    await contextDesktop.close();

    // Mobile viewport (390x844)
    const contextMobile = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const pageMobile = await contextMobile.newPage();
    await pageMobile.goto(fileUrl, { waitUntil: 'load' });
    await pageMobile.waitForTimeout(500);
    const mobileScreenshotPath = path.join(outputDir, `${item.desk}-mobile-390.png`);
    await pageMobile.screenshot({ path: mobileScreenshotPath, fullPage: false });
    console.log(`  ✓ Saved ${mobileScreenshotPath}`);
    await contextMobile.close();
  }

  await browser.close();
  console.log('✨ Screenshot capture complete!');
}

captureScreenshots().catch(err => {
  console.error('Error capturing screenshots:', err);
  process.exit(1);
});
