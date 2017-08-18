#! python3

import os, sys
import time
import random
from selenium import webdriver


#This program is for personal and internal use, its should not work on other PC


#randTime = random.randint()
randTime_Float = random.uniform(0.6, 2.2)


#Run Google chrome
chrome_path = "C:\Python\programs\selenium_driver_chrome\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)

#Reach to  web
browser.get('SOME URL')

#Login to  web
account = browser.find_element_by_name('loginId')
account.send_keys('XXXXXX')
password = browser.find_element_by_name('password')
password.send_keys('12345')

time.sleep(randTime_Float)
loginBtn = browser.find_element_by_id("button-1016")
loginBtn.click()

#waiting for login
time.sleep(5)

#Press "OK" when info jump out.
okayBtn = browser.find_element_by_id("ext-gen383")
okayBtn.click()

#Choose personal queries
personalQueries = browser.find_element_by_class_name("x-tree-node-anchor")
personalQueries.click()

#Find MIPS_ALL
time.sleep(2)
mips_all = browser.find_element_by_xpath("//span[text()='MIPS_ALL']")
mips_all.click()

#Select export to excel
time.sleep(2)
exportToExcelBtn = browser.find_element_by_id("ext-gen491")
exportToExcelBtn.click()

#Click "YES" for 2007 ver excel when the panel jump out
time.sleep(2)
clickYesFor2007Btn = browser.find_element_by_id("ext-gen389")
clickYesFor2007Btn.click()

#Close Chrome and CMD
time.sleep(3)
browser.quit()


