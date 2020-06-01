from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import unittest


class RegisterPage(unittest.TestCase):
    def __init__(self, myDriver):
        self.driver = myDriver
        self.countryDD = Select(self.driver.find_element_by_name('country'))

    def select_country_by_index(self, index):
        self.countryDD.select_by_index(index)
        time.sleep(2)   

    def verify_country(self,country):
        self.countryDD = Select(self.driver.find_element_by_name('country'))
        self.assertEquals(self.countryDD.first_selected_option.text.strip(), 'ANGUILLA')

