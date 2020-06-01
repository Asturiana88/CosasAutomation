import time


class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.user_box = self.driver.find_element_by_name('userName')
        self.pass_box = self.driver.find_element_by_name('password')
        self.submit_btn = self.driver.find_element_by_name('login')
        self.register_link = self.driver.find_element_by_link_text('REGISTER')

    def click_register(self):
        self.register_link.click()

    
    def login(self, user_name,paswd):
        self.user_box.send_keys(user_name)
        self.pass_box.send_keys(paswd)
        self.submit_btn.click()
        time.sleep(2)