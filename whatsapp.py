from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import bs4

import time
  
# Replace below path with the absolute path
# to chromedriver in your computer
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')

driver = webdriver.Chrome('/home/rushi/Desktop/Trade/chromedriver', chrome_options=options)
driver.set_page_load_timeout(360000)
driver.implicitly_wait(360000)

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 5000)


def send(name, msg):
    ele = driver.find_element_by_class_name("_1Ek-U").click()
    time.sleep(1)

    actions = ActionChains(driver)
    actions.send_keys(name)
    actions.perform()
    time.sleep(3)

    ele = driver.find_element_by_class_name("_3Dr46").click()
    actions = ActionChains(driver)
    actions.send_keys(msg + '\n')
    actions.perform()
    time.sleep(4)



# actions = ActionChains(driver)
# actions.send_keys(Keys.RETURN)
# actions.perform()
# time.sleep(3)
# source = driver.page_source
# src = bs4.BeautifulSoup(source, 'lxml')
# k = src.select('button')

def stop():
    driver.close()