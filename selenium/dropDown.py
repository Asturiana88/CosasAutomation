from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get('http://newtours.demoaut.com/')

time.sleep(5)

driver.find_element_by_link_text('REGISTER').click()

time.sleep(2)

countryDD = Select(driver.find_element_by_name('country'))
countryDD.select_by_index(5)

driver.quit()