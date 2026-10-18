const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function getJsFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      if (['node_modules', 'vocabulary', 'data', '.git'].includes(file)) {
        continue;
      }
      getJsFiles(filePath, fileList);
    } else if (file.endsWith('.js') || file.endsWith('.mjs')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const jsFiles = getJsFiles('.');
let errorCount = 0;

console.log(`Checking JS syntax in ${jsFiles.length} files using node --check...`);

for (const file of jsFiles) {
  try {
    execSync(`node --check "${file}"`, { stdio: 'pipe' });
  } catch (err) {
    console.error(`❌ SyntaxError in ${file}:`);
    console.error(err.stderr ? err.stderr.toString() : err.message);
    errorCount++;
  }
}

if (errorCount > 0) {
  console.error(`\nFound ${errorCount} JS syntax errors.`);
  process.exit(1);
} else {
  console.log('✅ All JS files passed syntax check successfully!');
}
