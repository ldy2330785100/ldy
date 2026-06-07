import re
import os
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, d):
        self.text.append(d)
    def get_data(self):
        return ''.join(self.text)

def strip_tags(html_content):
    s = MLStripper()
    s.feed(html_content)
    return s.get_data()

with open('changelog.html', 'r', encoding='utf-8') as f:
    content = f.read()

entry_pattern = r'<div class="entry">.*?<div class="date">(.*?)</div>.*?<div>(.*?)</div>.*?</div>'
match = re.search(entry_pattern, content, re.DOTALL)
if not match:
    print('未找到 entry')
    exit(1)

date = match.group(1).strip()
inner = match.group(2)

ver_match = re.search(r'<strong>(.*?)</strong>', inner)
version = ver_match.group(1) if ver_match else 'unknown'

lines = re.split(r'<br\s*/?>', inner)
body_lines = []
for line in lines[1:]:
    line = strip_tags(line).strip()
    if not line:
        continue
    m = re.match(r'^(\S+\s+)([^：]+)：(.*)$', line)
    if m:
        emoji_part = m.group(1)
        type_text = m.group(2)
        desc = m.group(3)
        formatted = f'{emoji_part}**{type_text}**：{desc}'
        body_lines.append(formatted)
    else:
        body_lines.append(line)

body_content = '<br>\n'.join(body_lines)
markdown_body = f'### **{version}** {date}\n\n{body_content}'

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f'body<<EOF\n{markdown_body}\nEOF\n')