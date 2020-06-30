import unittest
from selenium import webdriver
from loginPage import PaginaLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.PageLogin = PaginaLogin(self.driver)
        self.PageLogin.login()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'email')))

    def test_login_format_Error(self):
        self.PageLogin.ingreso_user_pasword('asddffdf', 'dffsddddsdd')
        error = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="center_column"]/div[1]/ol/li')))
        self.assertEqual(error.text, 'Invalid email address.')

    def test_login_autentication_Error(self):
        self.PageLogin.ingreso_user_pasword('pepe@pepepe.com', 'dffsddddsdd')
        error = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="center_column"]/div[1]/ol/li')))
        self.assertEqual(error.text, 'Authentication failed.')



if __name__ == "__main__":
    unittest.main()