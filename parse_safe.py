import re, base64
with open('test.html','r') as f: html = f.read()
m = re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)', html)
if m:
    b64 = m.group(1).strip()
    b64 += "=" * ((4 - len(b64) % 4) % 4)
    with open('logo.png','wb') as o:
        o.write(base64.b64decode(b64))
