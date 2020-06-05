from selenium.webdriver.common.by import By


class PageIndex():
    def __init__(self, elem_waiter):
        self.elem_waiter = elem_waiter
        self.barraBusqueda = (By.ID, 'search_query_top')
        self.buscarBtn = (By.NAME, 'submit_search')
        self.colorNaranja = (By.ID,'color_1')

    def buscar_articulo(self, articulo):
        self.elem_waiter(self.barraBusqueda).send_keys(articulo)
        self.elem_waiter(self.buscarBtn).click()

    def clickBtnNaranja(self):
        self.elem_waiter(self.colorNaranja).click()
