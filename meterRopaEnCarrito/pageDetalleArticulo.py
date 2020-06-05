from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PaginaDetalleArticulo():
    def __init__(self, wait_elem):
        self.wait_elem = wait_elem
        self.inputCantidad = (By.ID, 'quantity_wanted')
        self.plusBtnClass = (By.CLASS_NAME, 'icon-plus')
        self.cantidadCarrito = (By.ID, 'layer_cart_product_quantity')

    def agregarCantidad(self, cantidad):
        self.wait_elem(self.inputCantidad).clear()
        self.wait_elem(self.inputCantidad).send_keys(cantidad)
        
    def click_botonMas(self):
        self.wait_elem(self.plusBtnClass).click()
        self.wait_elem(self.plusBtnClass).click()
        self.wait_elem(self.plusBtnClass).click()

    def verificarCantidad(self):
        return self.wait_elem(self.cantidadCarrito).text

    def pulsar_btn_enter(self):
        self.wait_elem(self.inputCantidad).send_keys(Keys.ENTER)
