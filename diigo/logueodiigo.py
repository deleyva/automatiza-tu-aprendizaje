# Logueo en diigo

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import time

user = input('Usuario: ')
passwd = getpass.getpass('Contraseña: ')

browser = webdriver.Firefox()
browser.get('https://www.diigo.com/sign-in?referInfo=https%3A%2F%2Fwww.diigo.com')

try:
    elem_user = browser.find_element_by_name('Username')
    elem_user.send_keys('deleyva_catedu1')
    elem_pass = browser.find_element_by_name('password')
    elem_pass.send_keys(passwd)
    sign_in = browser.find_element_by_id('loginButton')
    sign_in.click()
    time.sleep(5)
    bulk_edit = browser.find_elements_by_class_name('text')[1]
    bulk_edit.click()
    time.sleep(2)
    select_item = browser.find_elements_by_class_name('BookmarkItem')

    for item in select_item:
        fuente = ActionChains(browser).move_to_element(item).click().perform()
        tres_puntos = browser.find_element_by_xpath('//*[@id="library"]/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[6]/div/i')
        tres_puntos.click()
        time.sleep(1)
        export_csv = browser.find_elements_by_xpath('//*[@id="library"]/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div[6]/div/div/a[6]')
        time.sleep(2)
        export_csv[0].click()
        time.sleep(5)
        x = browser.find_element_by_class_name('close')
        x.click()

except:
    print('Was not able to find an element with that name.')    
