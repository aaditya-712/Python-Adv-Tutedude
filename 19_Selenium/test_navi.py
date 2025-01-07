from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
time.sleep(2)
driver.get('https://www.wikipedia.org')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
