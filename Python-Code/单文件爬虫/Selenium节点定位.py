from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get('https://www.taobao.com/')
time.sleep(2)

element = browser.find_elements(By.CSS_SELECTOR,'.nav-hd li')[1]
element.click()
time.sleep(1)
browser.maximize_window()