import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.keys import Keys #Para pulsar teclas especiales

class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        # self.user_box = self.driver.find_element_by_name('userName')
        # self.register_link = self.driver.find_element_by_link_text('REGISTER')
        self.user_box = (By.NAME, 'userName')
        self.pass_box = (By.NAME, 'password')
        self.submit_btn = (By.NAME, 'login')
        self.register_link = (By.LINK_TEXT, 'REGISTER')


    def click_register(self):
        #self.register_link.click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.register_link).click()
    

    def login(self, user_name,paswd):
        # self.user_box.send_keys(user_name)
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(paswd)
        try:
            submitW = WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(self.submit_btn))
            self.driver.find_element(*self.submit_btn).click()
        except:
             print("the button is not clickable")       
        # self.submit_btn.click()

    def login_by_tab(self, usr, pswd):
        self.driver.find_element(*self.user_box).send_keys(usr+Keys.TAB+pswd+Keys.TAB+Keys.ENTER)
