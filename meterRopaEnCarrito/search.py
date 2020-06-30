import unittest
from selenium import webdriver
from pageIndex import PageIndex
from pageDetalleArticulo import PaginaDetalleArticulo     
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import PAGE_URL
from utils import get_driver

class SearchIndex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver = get_driver()
        self.driver.get(PAGE_URL)
        self.pagina_inicio = PageIndex(self._wait_for_elem)
        self.pagina_detalle_articulo = PaginaDetalleArticulo(self._wait_for_elem) 

    def _wait_for_elem(self, search_by):
        return WebDriverWait(self.driver, 10).until(
          EC.visibility_of_element_located(search_by)
        )

    def test_article_lookup(self):
        self.pagina_inicio.buscar_articulo('t-shirt')
        self.pagina_inicio.clickBtnNaranja()
        self.pagina_detalle_articulo.agregarCantidad(25)
        self.pagina_detalle_articulo.click_botonMas()
        self.pagina_detalle_articulo.pulsar_btn_enter()
        self.assertEqual('28', self.pagina_detalle_articulo.verificarCantidad())
        

if __name__ == "__main__":
    unittest.main()
