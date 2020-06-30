import unittest
from selenium import webdriver
#from helpers.xmlReader import *
#from helpers.data import *
import time
from selenium.webdriver.support.ui import Select
from pages.pageIndex import PageIndex
from pages.RegisterPage import RegisterPage
from pages.registerForm import RegisterFormPage
import xmlrunner
import HtmlTestRunner
import sys


class newTours(unittest.TestCase):
    def setUp(self):
        #self.configuracion = xmlReader()
        self.driver = webdriver.Chrome('chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        #if self.configuracion.obtener_datos('browser'=='chrome'):
         #   self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self.driver.get('http://newtours.demoaut.com/')
        #self.driver.maximize_window()
        self.page_index = PageIndex(self.driver)            
        self.page_register = RegisterPage(self.driver)
        self.page_reg_form = RegisterFormPage(self.driver)
        self.tc = unittest.TestCase('__init__')

    @unittest.skip("no quiero que se corra")    #skip case
    #@unittest.skipIf(2>1, "solo si 2 mayor que 1")
    def test_dropDowns(self):
        my_data = Test_data()
        self.page_index.click_register()
        self.page_register.select_country_by_index(5)
        self.page_register.verify_country(my_data.country)


    def test_register(self):
        self.page_index.login('test','test')
        #link_register = self.driver.find_element_by_link_text("registration form")
        self.page_reg_form.verify_register()

    @unittest.skipUnless(sys.platform.startswith("linux"), "solo para linux ")
    def test_login_by_tabs(self,):
        self.page_index.login_by_tab('test', 'test')


    def tearDown(self):
        self.driver.quit()

# if __name__ == "__main__":
#     unittest.main(
#         testrunner = xmlrunner.XMLTestRunner(output=='output'),
#         failfast=False,buffer=False,catchbrak=False)
#         #python -m xmlrunner newTourTest.py  // se corre en consola

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))