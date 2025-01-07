from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
driver.maximize_window()

search_box = driver.find_element(By.NAME, 'q')
# time.sleep(5)

search_box.send_keys('Selenium')
time.sleep(5)

button = driver.find_element(By.NAME, 'btnK')
button.click()


# this input is used to prevent the window from being closed automatically
input()
