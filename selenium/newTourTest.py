import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from pages.pageIndex import *
from pages.RegisterPage import *


class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com/')
        self.page_index = PageIndex(self.driver)
        self.page_register = RegisterPage(self.driver)
        time.sleep(2)

    def test_dropDowns(self):
        self.page_index.click_register()
        self.page_register.select_country_by_index(5)
        self.page_register.verify_country("ARGELIA")

    def test_register(self):
        self.page_index.login('test','test')
        link_register = self.driver.find_element_by_link_text("registration form")
        self.assertEquals(link_register.text, "registration form" )


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()