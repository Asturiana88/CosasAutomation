class PaginaLogin():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.btnLogin = 'login'
        self.inputEmail = 'email'
        self.inputPaswd = 'passwd'
        self.sigInBtn = 'SubmitLogin'

    def login(self):
        self.driver.find_element_by_class_name(self.btnLogin).click()

    
    def ingreso_user_pasword(self, email, paswd):
        self.driver.find_element_by_id(self.inputEmail).send_keys(email)    
        self.driver.find_element_by_id(self.inputPaswd).send_keys(paswd)    
        self.driver.find_element_by_id(self.sigInBtn).click()
