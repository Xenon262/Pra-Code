from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge()
browser.get('https://www.taobao.com/')

try:
    element = WebDriverWait(browser,10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR,'.nav-hd li')
        )
    )
    print(element[1].text)
    print("资源加载成功")
except:
    print("资源加载失败")
finally:
    print("清理资源")
    browser.close()