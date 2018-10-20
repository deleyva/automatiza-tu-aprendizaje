from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
time.sleep(2)
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)     # scrolls to bottom
time.sleep(3)
htmlElem.send_keys(Keys.HOME)    # scrolls to top