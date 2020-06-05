from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By


class RegisterPage(unittest.TestCase):
    def __init__(self, myDriver):
        self.driver = myDriver
        #self.countryDD = Select(self.driver.find_element_by_name('country'))
        self.countryDD = (By.NAME, 'country')
        self.tc = unittest.TestCase('__init__')


    def select_country_by_index(self, index):
        #self.countryDD.select_by_index(index)
        Select(self.driver.find_element(*self.countryDD)).select_by_index(index)
        self.driver.save_screenshot('screenshot.png') #toma screenshot

    def verify_country(self,country):
        #self.countryDD = Select(self.driver.find_element_by_name('country'))
        self.tc.assertEqual(Select(self.driver.find_element(*self.countryDD)).first_selected_option.text.strip(), country)
        #print("Before")
        self.driver.get_screenshot_as_file('screenshott.png') #toma screenshot
        #self.assertEqual(1,1)

