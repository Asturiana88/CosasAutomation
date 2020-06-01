from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')

time.sleep(5)

user_box = driver.find_element_by_name('userName')
pass_box = driver.find_element_by_name('password')
submit_btn = driver.find_element_by_name('login')

user_box.send_keys('test')
pass_box.send_keys('test')
submit_btn.click()

time.sleep(5)
link_register = driver.find_element_by_link_text("registration form")
assert link_register.text == "registration form"

driver.quit()