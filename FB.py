from selenium import webdriver
import time

username = 'sample'
password = 'usman'

url = 'https://www.facebook.com/'

driver = webdriver.Chrome("/Users/usman/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()

