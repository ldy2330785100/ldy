import os
import re
from bs4 import BeautifulSoup

with open('changelog.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
entry = soup.select_one('.entry')
if not entry:
    raise SystemExit('No entry found')

date_elem = entry.select_one('.date')
date = date_elem.text.strip() if date_elem else ''

strong = entry.select_one('strong')
version = strong.text.strip() if strong else ''

entry_copy = entry.__copy__()
if date_elem:
    date_elem.extract()
if strong:
    strong.extract()

text = entry_copy.get_text(separator='\n')
lines = [line.strip() for line in text.splitlines() if line.strip()]

body_lines = []
for line in lines:
    if '：' not in line:
        continue
    parts = line.split('：', 1)
    left = parts[0].strip()
    right = parts[1].strip()
    if not left or not right:
        continue
    emoji = left[0] if left else ''
    type_part = left[1:].strip()
    body_lines.append(f"{emoji} **{type_part}**：{right}")

body = f"### **{version}** {date}\n\n" + "<br>\n".join(body_lines)

prerelease = 'true' if ('-alpha' in version or '-beta' in version or '-rc' in version) else 'false'

github_output = os.environ.get('GITHUB_OUTPUT')
if github_output:
    with open(github_output, 'a') as f:
        f.write(f"version={version}\n")
        f.write(f"date={date}\n")
        f.write(f"prerelease={prerelease}\n")
        f.write("body<<EOF\n")
        f.write(body + "\n")
        f.write("EOF\n")