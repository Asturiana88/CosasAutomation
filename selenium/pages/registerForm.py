from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.common.by import By


class RegisterFormPage():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.link_registration_form = (By.LINK_TEXT,"registration form")
        self.tc = unittest.TestCase('__init__')


    def verify_register(self):
        self.driver.implicitly_wait(5)
        register_link = self.driver.find_element(*self.link_registration_form)
        self.tc.assertEqual(register_link.text, "registration form")

