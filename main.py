from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_baidu_search():
    # 初始化 Chrome 浏览器驱动
    driver = webdriver.Chrome()

    # 打开百度首页
    driver.get('http://www.baidu.com')

    # 在搜索框输入关键词
    driver.find_element(By.ID, 'kw').send_keys('selenium')

    # 点击搜索按钮
    driver.find_element(By.ID, 'su').click()

    # 等待页面加载
    time.sleep(2)
    # 等待页面加载
    time.sleep(2)

    # 关闭浏览器
    driver.quit()

    # 等待页面加载
    time.sleep(2)