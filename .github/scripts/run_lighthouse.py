import json
import subprocess
import sys
import os

SITE_URL = os.environ.get('SITE_URL', 'https://ldy2330785100.github.io/ldy/')
OUTPUT_HTML = 'lighthouse-report.html'
OUTPUT_JSON = 'lighthouse-summary.json'

def run_lighthouse(url):
    cmd_html = [
        'lighthouse', url,
        '--output=html',
        f'--output-path={OUTPUT_HTML}',
        '--chrome-flags=--headless',
        '--preset=desktop',
        '--throttling-method=devtools'
    ]
    result_html = subprocess.run(cmd_html, capture_output=True, text=True)
    if result_html.returncode != 0:
        print('Lighthouse HTML 生成失败')
        print(result_html.stderr)
        sys.exit(1)

    cmd_json = [
        'lighthouse', url,
        '--output=json',
        f'--output-path={OUTPUT_JSON}',
        '--chrome-flags=--headless',
        '--preset=desktop',
        '--throttling-method=devtools'
    ]
    result_json = subprocess.run(cmd_json, capture_output=True, text=True)
    if result_json.returncode != 0:
        print('Lighthouse JSON 生成失败')
        print(result_json.stderr)
        sys.exit(1)

    with open(OUTPUT_JSON, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data

def extract_scores(lhr):
    categories = lhr.get('categories', {})
    scores = {}
    for name, data in categories.items():
        score = data.get('score', 0)
        if score is not None:
            scores[name] = int(score * 100)
        else:
            scores[name] = 0
    return scores

def main():
    print(f'开始 Lighthouse 测试，目标: {SITE_URL}')
    lhr = run_lighthouse(SITE_URL)
    scores = extract_scores(lhr)
    print('\nLighthouse 评分结果:')
    for name, value in scores.items():
        print(f'  {name}: {value}')
    performance = scores.get('performance', 0)
    if performance < 80:
        print(f'\n⚠️ 性能评分 {performance} 低于阈值 80，请检查报告详情')
    else:
        print(f'\n✅ 性能评分 {performance} 符合阈值要求 (>=80)')
    with open('lighthouse-summary.json', 'w', encoding='utf-8') as f:
        json.dump({
            'url': SITE_URL,
            'scores': scores,
            'full_report': lhr
        }, f, indent=2)
    print(f'\n详细报告已保存: {OUTPUT_HTML} 和 {OUTPUT_JSON}')

if __name__ == '__main__':
    main()