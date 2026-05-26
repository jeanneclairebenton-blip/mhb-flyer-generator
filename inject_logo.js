const fs = require('fs');
const b64 = fs.readFileSync('/Users/jeanneclairebenton/.gemini/antigravity/scratch/mhb-flyer-generator/logo.png').toString('base64');
const dataUrl = 'data:image/png;base64,' + b64;
let html = fs.readFileSync('/Users/jeanneclairebenton/.gemini/antigravity/scratch/mhb-flyer-generator/index.html', 'utf8');

// Replace both occurrences of the logo src
html = html.replace(/src="logo\.png"/g, 'src="' + dataUrl + '"');
html = html.replace(/src="https:\/\/jeanneclairebenton-blip\.github\.io\/mhb-flyer-generator\/logo\.png"/g, 'src="' + dataUrl + '"');

fs.writeFileSync('/Users/jeanneclairebenton/.gemini/antigravity/scratch/mhb-flyer-generator/index.html', html);
console.log('Logo injected successfully!');
