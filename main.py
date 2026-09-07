from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_baidu_search():
    # 初始化 Edge 浏览器驱动
    driver = webdriver.Edge()

    try:
        # 打开百度首页
        driver.get('http://www.baidu.com')

        # 使用显式等待确保搜索框加载完成并可交互
        # 原因：ElementNotInteractableException通常是因为元素尚未完全加载或被其他元素遮挡
        # WebDriverWait会等待最多10秒，直到元素可见并可点击
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'chat-textarea'))
        )
        search_box.send_keys('selenium')

        # 同样使用显式等待确保搜索按钮可点击
        # 原因：避免在按钮未完全加载时尝试点击
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'su'))
        )
        search_button.click()

        # 等待搜索结果加载
        # 原因：给页面足够时间加载搜索结果
        time.sleep(10)

    except Exception as e:
        # 捕获并打印异常信息
        # 原因：便于调试和了解具体错误原因
        print(f"发生错误: {e}")
    finally:
        # 确保浏览器最终会被关闭
        # 原因：即使发生异常也要关闭浏览器，避免残留进程
        driver.quit()


if __name__ == '__main__':
    test_baidu_search()
