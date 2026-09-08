from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_web_form():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')

    # 等待输入框出现（定位器用 name='my-text'，绝对存在）
    wait = WebDriverWait(driver, 10)
    text_box = wait.until(EC.presence_of_element_located((By.NAME, 'my-text')))
    text_box.send_keys('Hello CI')

    # 点击提交按钮
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # 等待成功页面标题出现
    wait.until(EC.title_contains('Submitted'))
    assert 'Submitted' in driver.title

    driver.quit()