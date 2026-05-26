import re
import base64

with open('test.html','r') as f:
    html = f.read()

m = re.search(r'data:image/png;base64,(iVBORw0KGgoAAAANSUhEUgAAApgAAALICAYAAADbv4A\+AAEAA?[A-Za-z0-9+/=]+)', html)
if m:
    b64_data = m.group(1)
    with open('logo.png','wb') as o:
        o.write(base64.b64decode(b64_data))
        print('Saved SVG/PNG to logo.png')
