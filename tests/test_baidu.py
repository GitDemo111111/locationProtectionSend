from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time


def test_web_form():
    try:
        # 配置Edge浏览器选项
        # 原因：使用Edge替代Chrome，需要使用EdgeOptions
        options = webdriver.EdgeOptions()

        # 添加无头模式参数
        # 原因：CI环境通常没有图形界面，需要无头模式运行
        options.add_argument('--headless')

        # 添加禁用沙箱参数
        # 原因：CI环境中可能需要绕过OS安全模型
        options.add_argument('--no-sandbox')

        # 禁用/dev/shm使用
        # 原因：解决CI环境中共享内存不足的问题
        options.add_argument('--disable-dev-shm-usage')

        # 禁用GPU加速
        # 原因：无头模式下不需要GPU加速，可减少资源占用
        options.add_argument('--disable-gpu')

        # 设置窗口大小
        # 原因：某些元素在不同窗口大小下可能显示不同
        options.add_argument('--window-size=1920,1080')

        # 初始化Edge浏览器驱动
        # 原因：使用Edge浏览器进行测试
        driver = webdriver.Edge(options=options)

        # 设置页面加载超时时间
        # 原因：防止页面加载过久导致测试挂起
        driver.set_page_load_timeout(30)

        # 访问测试页面
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')

        # 创建显式等待对象
        # 原因：使用显式等待比固定等待更可靠
        wait = WebDriverWait(driver, 15)

        # 等待并定位文本输入框
        # 原因：确保输入框已加载且可交互
        text_box = wait.until(
            EC.element_to_be_clickable((By.NAME, 'my-text'))
        )
        text_box.send_keys('Hello CI')

        # 等待并定位提交按钮
        # 原因：确保按钮已加载且可点击
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        submit_button.click()

        # 等待页面标题更新
        # 原因：确认页面已跳转到提交成功页面
        wait.until(EC.title_contains('Submitted'))
        assert 'Submitted' in driver.title

    except Exception as e:
        # 捕获并打印异常信息
        # 原因：便于在CI日志中查看错误详情
        print(f"测试执行失败: {str(e)}", file=sys.stderr)

        # 截图保存错误现场
        # 原因：便于后续分析失败原因
        if 'driver' in locals():
            timestamp = int(time.time())
            driver.save_screenshot(f'error_{timestamp}.png')
        raise
    finally:
        # 确保浏览器会被关闭
        # 原因：即使测试失败也要清理资源，避免CI环境残留进程
        if 'driver' in locals():
            driver.quit()
