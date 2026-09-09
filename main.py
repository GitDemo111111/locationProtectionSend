# 导入Selenium库的核心模块
# 原因：这些模块提供了浏览器自动化所需的基本功能
from selenium import webdriver
# 导入By类，用于指定元素定位策略
# 原因：通过ID、NAME、CSS_SELECTOR等方式定位页面元素
from selenium.webdriver.common.by import By
# 导入WebDriverWait类，用于实现显式等待
# 原因：显式等待比固定等待更可靠，可以等待特定条件满足后再继续执行
from selenium.webdriver.support.ui import WebDriverWait
# 导入expected_conditions模块，提供常用的等待条件
# 原因：这些条件可以用于判断元素是否可见、可点击等状态
from selenium.webdriver.support import expected_conditions as EC
# 导入sys模块，提供系统相关的参数和函数
# 原因：用于将错误信息输出到标准错误流(stderr)
import sys
# 导入time模块，提供时间相关的函数
# 原因：用于生成时间戳，作为错误截图的文件名
import time


# 定义web_form函数，用于测试Web表单提交功能
# 参数text: 要在表单中输入的文本
# 返回值: 测试成功返回True，失败返回False
def web_form(text):
    try:
        # 创建Edge浏览器选项对象
        # 原因：通过选项对象可以配置浏览器的各种启动参数和行为
        options = webdriver.ChromeOptions()

        # 添加无头模式参数
        # 原因：CI环境通常没有图形界面，需要无头模式运行
        # 使用'--headless=new'参数启用新版无头模式，性能更好
        options.add_argument('--headless=new')

        # 添加禁用沙箱参数
        # 原因：CI环境中可能需要绕过OS安全模型，避免权限问题
        options.add_argument('--no-sandbox')

        # 禁用/dev/shm使用
        # 原因：解决CI环境中共享内存不足的问题，避免浏览器崩溃
        options.add_argument('--disable-dev-shm-usage')

        # 禁用GPU加速
        # 原因：无头模式下不需要GPU加速，可减少资源占用
        options.add_argument('--disable-gpu')

        # 设置窗口大小
        # 原因：某些元素在不同窗口大小下可能显示不同，设置固定大小确保一致性
        options.add_argument('--window-size=1920,1080')

        # ===== 新增：解决渲染超时的两个关键参数 =====
        # 设置页面加载策略为'eager'
        # 原因：'eager'策略只等待DOM加载完成，不等待所有资源(如图片)加载完成
        # 这可以显著减少页面加载时间，避免因等待资源加载而超时
        options.page_load_strategy = 'eager'  # 只等DOM，不等图片
        # ========================================

        # 初始化Edge浏览器驱动
        # 原因：创建浏览器实例，用于后续的自动化操作
        driver = webdriver.Chrome(options=options)

        # 设置页面加载超时时间为20秒
        # 原因：从默认的30秒降到20秒，避免因页面加载问题导致测试长时间挂起
        driver.set_page_load_timeout(20)

        # ----- 以下全是你的原始日志，一个字符都没删 -----
        # 打印访问测试页面的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("正在访问测试页面...")

        # 访问测试页面
        # 原因：打开Selenium官方提供的测试表单页面
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')

        # 打印当前页面URL
        # 原因：确认页面是否正确加载
        print(f"当前页面URL: {driver.current_url}")

        # 打印当前页面标题
        # 原因：确认页面是否正确加载
        print(f"当前页面标题: {driver.title}")

        # 创建显式等待对象，设置最长等待时间为15秒
        # 原因：使用显式等待比固定等待更可靠，可以等待特定条件满足后再继续执行
        wait = WebDriverWait(driver, 15)

        # 打印等待文本输入框的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("等待文本输入框出现...")

        # 等待文本输入框可点击
        # 原因：确保输入框已加载且可交互，避免因元素未加载完成而操作失败
        text_box = wait.until(EC.element_to_be_clickable((By.NAME, 'my-text')))

        # 打印正在输入文本的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("正在输入文本...")

        # 在文本框中输入传入的文本
        # 原因：模拟用户在表单中输入文本的操作
        text_box.send_keys(text)

        # 打印文本输入成功的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("文本输入成功")

        # 打印等待提交按钮的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("等待提交按钮出现...")

        # 等待提交按钮可点击
        # 原因：确保按钮已加载且可点击，避免因元素未加载完成而操作失败
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))

        # 点击提交按钮
        # 原因：模拟用户点击提交按钮的操作
        submit_button.click()

        # 打印提交按钮点击成功的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("提交按钮点击成功")

        # 打印等待页面跳转的提示信息
        # 原因：便于在日志中跟踪测试执行进度
        print("等待页面跳转...")

        # 等待URL包含'submitted-form.html'
        # 原因：确认页面已跳转到提交成功页面
        wait.until(EC.url_contains('submitted-form.html'))

        # 打印跳转后的URL
        # 原因：确认页面是否正确跳转
        print(f"跳转后当前URL: {driver.current_url}")

        # 断言URL包含'submitted-form.html'
        # 原因：验证页面是否正确跳转到提交成功页面
        assert 'submitted-form.html' in driver.current_url

        # 打印测试断言通过的提示信息
        # 原因：便于在日志中确认测试成功
        print("测试断言通过")

        # 关闭浏览器
        # 原因：释放资源，避免浏览器进程残留
        driver.quit()

        # 返回True表示测试成功
        # 原因：便于调用者判断测试是否成功
        return True

    # 捕获所有异常
    # 原因：处理测试过程中可能出现的各种错误
    except Exception as e:
        # 打印错误信息到标准错误流
        # 原因：便于在CI日志中查看错误详情
        print(f"测试执行失败: {str(e)}", file=sys.stderr)

        # 检查driver变量是否存在
        # 原因：避免在driver未初始化时尝试访问其属性
        if 'driver' in locals():
            # 生成时间戳
            # 原因：为错误截图创建唯一的文件名
            timestamp = int(time.time())

            # 设置截图路径
            # 原因：保存错误截图便于后续分析失败原因
            screenshot_path = f'error_{timestamp}.png'

            # 保存错误截图
            # 原因：记录错误发生时的页面状态，便于调试
            driver.save_screenshot(screenshot_path)

            # 打印截图保存路径
            # 原因：便于查找错误截图
            print(f"错误截图已保存到: {screenshot_path}")

            # 打印错误发生时的页面URL
            # 原因：确认错误发生时所在的页面
            print(f"错误发生时页面URL: {driver.current_url}")

            # 打印错误发生时的页面标题
            # 原因：确认错误发生时所在的页面
            print(f"错误发生时页面标题: {driver.title}")

            # 打印页面源代码前500个字符
            # 原因：查看页面结构，便于分析元素定位问题
            print(f"页面源代码前500字符: {driver.page_source[:500]}")

            # 关闭浏览器
            # 原因：释放资源，避免浏览器进程残留
            driver.quit()

        # 返回False表示测试失败
        # 原因：便于调用者判断测试是否成功
        return False


# if __name__ == '__main__':
#     # 本地手动测试用
#     # 原因：直接运行此脚本时执行测试，便于本地调试
#     web_form('Hello Local Debug')
