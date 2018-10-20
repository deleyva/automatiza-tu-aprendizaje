from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
linkElem = browser.find_element_by_id('login-signin')
linkElem.click()
time.sleep(5)
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
linkElem = browser.find_element_by_id('login-signin')
linkElem.click()