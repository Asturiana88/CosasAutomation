import unittest
from selenium import webdriver
from dressesPage import DressesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.dressesPage = DressesPage(self.driver)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, 'DRESSES')))
        self.dressesPage.go_dresses()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[1]/a')))

    #@unittest.skip("Skip")  
    def test_ingreso_seccion_dresses(self):
        self.dressesPage.go_casual_dresses()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'product_img_link')))
        self.dressesPage.go_first_dress()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'quantity_wanted')))
        cantidad = self.dressesPage.select_quantity_dress(5)
        self.dressesPage.select_size_dress('L')
        self.dressesPage.add_to_cart()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-medium')))
        self.assertTrue(str(cantidad) == self.dressesPage.return_quantity(), 'The quantity is not 5')
        self.assertTrue('$130.00' == self.dressesPage.return_price_verif(), 'The Price is not $130.00')
        self.assertTrue('$2.00' == self.dressesPage.return_price_shipping(), 'The Shipping Price is not $2.00')
        self.assertTrue('$132.00' == self.dressesPage.return_price_total(), 'The Shipping Price is not $132.00')
        self.assertTrue('Printed Dress' == self.dressesPage.return_name_prod_verif(), 'The Price is not Printed Dress')

    def test_Lower_First(self):
        self.dressesPage.select_lower_first()
        self.dressesPage.change_view_list()
        self.dressesPage.add_to_Cart_second_elem()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-ok')))
        self.assertTrue('$50.99' == self.dressesPage.return_price_verif(), 'The Price is not $50.99')
        self.assertTrue('$2.00' == self.dressesPage.return_price_shipping(), 'The Shipping Price is not $2.00')
        self.assertTrue('$52.99' == self.dressesPage.return_price_total(), 'The Shipping Price is not $52.99')
        self.assertTrue('Printed Dress' == self.dressesPage.return_name_prod_verif(), 'The Price is not Printed Dress')


if __name__ == "__main__":
    unittest.main()