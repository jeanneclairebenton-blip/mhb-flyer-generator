import re
import base64

with open('test.html', 'r') as f:
    html = f.read()

# find the logo base64
match = re.search(r'data:image/png;base64,([A-Za-z0-9+/=]+)', html)
if match:
    b64_data = match.group(1)
    with open('logo.png', 'wb') as out_f:
        out_f.write(base64.b64decode(b64_data))
    print("logo.png written.")
