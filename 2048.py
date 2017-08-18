#Simple version for automatic playing 2048

#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

chrome_path = "C:\Python\programs\selenium_driver_chrome\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)

browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

while True:
    time.sleep(random.uniform(0.1, 0.5))
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(random.uniform(0.1, 0.5))
    htmlElem.send_keys(Keys.UP)
    time.sleep(random.uniform(0.1, 0.5))
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(random.uniform(0.1, 0.5))
    htmlElem.send_keys(Keys.RIGHT)

