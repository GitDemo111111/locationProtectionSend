from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time


def web_form(text):
    try:
        # 配置Edge浏览器选项
        options = webdriver.EdgeOptions()

        # CI环境必须加无头模式
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')

        # ===== 新增：解决渲染超时的两个关键参数 =====
        options.page_load_strategy = 'eager'   # 只等DOM，不等图片
        # ========================================

        driver = webdriver.Edge(options=options)

        # 设置页面加载超时（从30秒降到20秒，避免长时间死等）
        driver.set_page_load_timeout(20)

        # ----- 以下全是你的原始日志，一个字符都没删 -----
        print("正在访问测试页面...")
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        print(f"当前页面URL: {driver.current_url}")
        print(f"当前页面标题: {driver.title}")

        wait = WebDriverWait(driver, 15)

        print("等待文本输入框出现...")
        text_box = wait.until(EC.element_to_be_clickable((By.NAME, 'my-text')))
        print("正在输入文本...")
        text_box.send_keys(text)
        print("文本输入成功")

        print("等待提交按钮出现...")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_button.click()
        print("提交按钮点击成功")

        print("等待页面跳转...")
        wait.until(EC.url_contains('submitted-form.html'))
        print(f"跳转后当前URL: {driver.current_url}")

        assert 'submitted-form.html' in driver.current_url
        print("测试断言通过")

        driver.quit()
        return True

    except Exception as e:
        print(f"测试执行失败: {str(e)}", file=sys.stderr)
        if 'driver' in locals():
            timestamp = int(time.time())
            screenshot_path = f'error_{timestamp}.png'
            driver.save_screenshot(screenshot_path)
            print(f"错误截图已保存到: {screenshot_path}")
            print(f"错误发生时页面URL: {driver.current_url}")
            print(f"错误发生时页面标题: {driver.title}")
            print(f"页面源代码前500字符: {driver.page_source[:500]}")
            driver.quit()
        return False

#
# if __name__ == '__main__':
#     # 本地手动测试用
#     web_form('Hello Local Debug')