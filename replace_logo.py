import base64
import re

# 1. Base64 encode the new logo
with open('/Users/jeanneclairebenton/.gemini/antigravity/brain/a94ad1a4-16fe-46be-ba1a-3f8e3b5dddb8/media__1775249368853.png', 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

img_tag = f'<img src="data:image/png;base64,{b64_img}" height="65" style="height:65px;object-fit:contain;display:block;" alt="Myers Home Buyers Logo">'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the flex gap:10px wrapper (UI and Print versions)
# The wrapper contains an img tag, then a div containing "Myers" and "Home Buyers"
pattern_ui = r'(<div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">\s*)<img[^>]*>[\s\S]*?<div[^>]*>[\s\S]*?Myers[\s\S]*?Home Buyers[\s\S]*?</div>(\s*</div>)'
new_html = re.sub(pattern_ui, r'\1' + img_tag + r'\2', html)

# Replace the flex gap:12px wrapper (Email template)
pattern_email = r'(<div style="display:flex;align-items:center;gap:12px;">\s*)<img[^>]*>[\s\S]*?<div[^>]*>[\s\S]*?Myers[\s\S]*?Home Buyers[\s\S]*?</div>(\s*</div>)'
new_html = re.sub(pattern_email, r'\1' + img_tag + r'\2', new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

