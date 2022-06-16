from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.maximize_window()
browser.get('https://www.baidu.com/')
time.sleep(2)

element1 = browser.find_element(By.ID,'kw')
element1.send_keys("网络爬虫")
time.sleep(1)



element2 = browser.find_element(By.ID,'su')
element2.click()
time.sleep(2)

browser.close()
