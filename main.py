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
        # CI环境必须禁用沙箱
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')

        driver = webdriver.Edge(options=options)
        driver.set_page_load_timeout(30)

        print("正在访问测试页面...")
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')

        wait = WebDriverWait(driver, 15)

        # 定位输入框
        print("等待文本输入框出现...")
        text_box = wait.until(EC.element_to_be_clickable((By.NAME, 'my-text')))

        # ⚠️ 修复点：这里必须用变量 text，而不是不存在的 inputText
        print("正在输入文本...")
        text_box.send_keys(text)
        print("文本输入成功")

        # 定位提交按钮
        print("等待提交按钮出现...")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        submit_button.click()
        print("提交按钮点击成功")

        # 等待跳转
        print("等待页面跳转...")
        wait.until(EC.url_contains('submitted-form.html'))

        # 断言 URL 正确
        assert 'submitted-form.html' in driver.current_url
        print("测试断言通过")

        driver.quit()
        return True  # 成功返回 True

    except Exception as e:
        print(f"测试执行失败: {str(e)}", file=sys.stderr)
        if 'driver' in locals():
            driver.save_screenshot(f'error_{int(time.time())}.png')
            driver.quit()
        return False  # 失败返回 False

    # if __name__ == '__main__':
    #     # 这里只用于本地手动测试，CI 不会执行这里
    #     test_web_form('Hello Local Debug')