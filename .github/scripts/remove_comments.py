import re
import sys

def remove_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    stats = {'html': 0, 'css': 0, 'js_line': 0, 'js_block': 0}
    deleted_html = []
    deleted_css = []
    deleted_js_line = []
    deleted_js_block = []

    def repl_html(m):
        stats['html'] += 1
        deleted_html.append(m.group(0))
        return ''
    content = re.sub(r'<!--.*?-->', repl_html, content, flags=re.DOTALL)

    def repl_css(m):
        style_content = m.group(1)
        def repl_css_comment(cm):
            stats['css'] += 1
            deleted_css.append(cm.group(0))
            return ''
        new_style = re.sub(r'/\*.*?\*/', repl_css_comment, style_content, flags=re.DOTALL)
        return f'<style>{new_style}</style>'
    content = re.sub(r'<style>(.*?)</style>', repl_css, content, flags=re.DOTALL)

    def repl_js(m):
        script_content = m.group(1)
        def repl_js_line(cm):
            stats['js_line'] += 1
            deleted_js_line.append(cm.group(0))
            return ''
        new_script = re.sub(r'//.*?$', repl_js_line, script_content, flags=re.MULTILINE)
        def repl_js_block(cm):
            stats['js_block'] += 1
            deleted_js_block.append(cm.group(0))
            return ''
        new_script = re.sub(r'/\*.*?\*/', repl_js_block, new_script, flags=re.DOTALL)
        return f'<script>{new_script}</script>'
    content = re.sub(r'<script>(.*?)</script>', repl_js, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return stats, deleted_html, deleted_css, deleted_js_line, deleted_js_block

def print_deleted(title, items, limit=80):
    if not items:
        print(f'  {title}: 0 个')
        return
    print(f'  {title}: {len(items)} 个')
    for idx, item in enumerate(items, 1):
        short = item[:limit] + ('…' if len(item) > limit else '')
        print(f'    [{idx}] {short}')

for file in ['index.html']:
    print(f'\n📄 处理 {file}')
    stats, html_comments, css_comments, js_line_comments, js_block_comments = remove_comments(file)
    print_deleted('HTML 注释', html_comments)
    print_deleted('CSS 注释', css_comments)
    print_deleted('JS 行注释', js_line_comments)
    print_deleted('JS 块注释', js_block_comments)
    print(f'✅ 总计删除: HTML {stats["html"]}, CSS {stats["css"]}, JS行 {stats["js_line"]}, JS块 {stats["js_block"]}')