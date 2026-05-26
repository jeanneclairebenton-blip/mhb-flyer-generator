const fs = require('fs');
const html = fs.readFileSync('test.html', 'utf-8');
// Find the logo
let m = html.match(/data:image\/png;base64,([^"]+)/);
if (m) {
  let b64 = m[1].replace(/\s+/g,'');
  fs.writeFileSync('images/logo.png', Buffer.from(b64, 'base64'));
}
