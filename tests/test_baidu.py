import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_baidu_search():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 关键：无头模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('http://www.baidu.com')
    driver.find_element(By.ID, 'kw').send_keys('selenium')
    driver.find_element(By.ID, 'su').click()
    time.sleep(2)

    assert 'selenium' in driver.title  # 有效断言
    driver.quit()