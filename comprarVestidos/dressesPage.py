
class DressesPage():
    def __init__(self, Mydriver):
        self.driver = Mydriver
        self.dressesBtn = 'DRESSES'
        self.casualDressesSection = '//*[@id="categories_block_left"]/div/ul/li[1]/a'
        self.firstDress = 'product_img_link'
        self.quantity_input = 'quantity_wanted'
        self.submitBtn = "button[name='Submit']"
        self.sizes_sel = 'group_1'
        self.formateo_size = "option[title='{}']"
        self.quantity_verif =  "span[id='layer_cart_product_quantity']"
        self.price_verif =  "span[id='layer_cart_product_price']"
        self.price_shipping =  "span[class='ajax_cart_shipping_cost']"
        self.total_price =  "span[class='ajax_block_cart_total']"
        self.name_prod_verif = "span[id='layer_cart_product_title']"
        self.sort_price_select = "option[value='price:asc']"
        self.view_list = 'icon-th-list'
        self.btn_second_elem = '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[2]/a[1]'
        

    def go_dresses(self):
        #self.driver.find_element_by_css_selector(self.dressesBtn).click()
        self.driver.find_element_by_link_text(self.dressesBtn).click()

    def go_casual_dresses(self):
        self.driver.find_element_by_xpath(self.casualDressesSection).click()
        print("Click casual OK!")
    
    def go_first_dress(self):
        self.driver.find_element_by_class_name(self.firstDress).click()
        print("Click First Dress OK!")

    def select_quantity_dress(self, quantity):
        self.driver.find_element_by_id(self.quantity_input).click()
        self.driver.find_element_by_id(self.quantity_input).clear()
        self.driver.find_element_by_id(self.quantity_input).send_keys(quantity)
        print("Click quantity OK!")
        return quantity
    
    def return_quantity(self):
        return self.driver.find_element_by_css_selector(self.quantity_verif).text

    def return_price_verif(self):
        return self.driver.find_element_by_css_selector(self.price_verif).text

    def return_price_shipping(self):
        return self.driver.find_element_by_css_selector(self.price_shipping).text

    def return_price_total(self):
        return self.driver.find_element_by_css_selector(self.total_price).text

    def return_name_prod_verif(self):
        return self.driver.find_element_by_css_selector(self.name_prod_verif).text   

    def select_size_dress(self, size):
        sizes_select = self.driver.find_element_by_id(self.sizes_sel)
        sizes_select.find_element_by_css_selector(self.formateo_size.format(size)).click()
        print("Click size OK!")

    def add_to_cart(self):
        self.driver.find_element_by_css_selector(self.submitBtn).click()
        print("Click Add to cart OK!")

    def select_lower_first(self):
        self.driver.find_element_by_css_selector(self.sort_price_select).click()
        print("Click Sort Lower First OK!")

    def change_view_list(self):
        self.driver.find_element_by_class_name(self.view_list).click()
        print("Click View List OK!")

    def add_to_Cart_second_elem(self):
        self.driver.find_element_by_xpath(self.btn_second_elem).click()
        print("Click Second Element OK!")