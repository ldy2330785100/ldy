import json
import sys
import os
from playwright.sync_api import sync_playwright

SITE_URL = os.environ.get('SITE_URL', 'https://ldy2330785100.github.io/ldy/')
REPORT_FILE = 'compatibility-report.json'

def test_browser(browser_type, device=None):
    results = {
        'browser': browser_type.name,
        'device': device,
        'passed': True,
        'errors': [],
        'logs': []
    }
    try:
        context_args = {}
        if device:
            from playwright.sync_api import devices
            context_args = devices[device]
        browser = browser_type.launch(headless=True)
        context = browser.new_context(**context_args) if device else browser.new_context()
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))
        page.goto(SITE_URL, wait_until='networkidle')
        page.wait_for_timeout(1000)

        if page.get_by_text('加载视频中').is_visible():
            results['logs'].append('视频加载占位符可见')
        if page.get_by_text('加载作品中').is_visible():
            results['logs'].append('作品加载占位符可见')

        settings_btn = page.locator('#settingsToggle')
        if settings_btn.is_visible():
            settings_btn.click()
            page.wait_for_timeout(500)
            if page.locator('.settings-panel.show').is_visible():
                results['logs'].append('设置面板打开成功')
                dark_btn = page.locator('.theme-btn[data-theme="dark"]')
                if dark_btn.is_visible():
                    dark_btn.click()
                    page.wait_for_timeout(500)
                    body_class = page.get_attribute('body', 'class')
                    if 'dark-theme' in body_class:
                        results['logs'].append('深色模式切换成功')
                    else:
                        results['errors'].append('深色模式切换失败，body 类未更新')
                else:
                    results['errors'].append('未找到深色模式按钮')
                close_btn = page.locator('#closeSettings')
                if close_btn.is_visible():
                    close_btn.click()
                    page.wait_for_timeout(300)
            else:
                results['errors'].append('设置面板未弹出')
        else:
            results['errors'].append('设置按钮不可见')

        font_tab = page.locator('.settings-nav-btn[data-tab="appearance"]')
        if font_tab.is_visible():
            font_tab.click()
            page.wait_for_timeout(300)
            font_option = page.locator('.font-option[data-font="font1"]')
            if font_option.is_visible():
                font_option.click()
                page.wait_for_timeout(500)
                body_class = page.get_attribute('body', 'class')
                if 'use-font1' in body_class:
                    results['logs'].append('字体切换成功')
                else:
                    results['errors'].append('字体切换失败')
            else:
                results['errors'].append('字体选项不可见')
        else:
            results['errors'].append('外观标签不可见')

        if errors:
            results['passed'] = False
            results['errors'].extend(errors)
        browser.close()
    except Exception as e:
        results['passed'] = False
        results['errors'].append(str(e))
    return results

def main():
    print(f'开始兼容性测试，目标: {SITE_URL}')
    all_results = []
    with sync_playwright() as p:
        browsers = [p.chromium, p.firefox, p.webkit]
        devices_to_test = ['iPhone 12', 'Pixel 5']
        for browser in browsers:
            print(f'\n测试浏览器: {browser.name}')
            res = test_browser(browser)
            all_results.append(res)
            print(f'  结果: {"✅ 通过" if res["passed"] else "❌ 失败"}')
            if res['errors']:
                for err in res['errors']:
                    print(f'    错误: {err}')
            for log in res['logs']:
                print(f'    日志: {log}')
        for device_name in devices_to_test:
            print(f'\n测试设备: {device_name} (WebKit)')
            res = test_browser(p.webkit, device=device_name)
            all_results.append(res)
            print(f'  结果: {"✅ 通过" if res["passed"] else "❌ 失败"}')
            if res['errors']:
                for err in res['errors']:
                    print(f'    错误: {err}')
            for log in res['logs']:
                print(f'    日志: {log}')
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f'\n兼容性测试报告已保存: {REPORT_FILE}')
    any_failed = any(not r['passed'] for r in all_results)
    if any_failed:
        print('\n⚠️ 部分兼容性测试未通过，请检查上述详细报告')
    else:
        print('\n✅ 所有兼容性测试均通过')

if __name__ == '__main__':
    main()