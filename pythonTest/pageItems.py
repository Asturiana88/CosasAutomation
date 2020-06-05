class PageItems():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.resultadoXpath = '//*[@id="center_column"]/h1/span[1]'
        self.noResultBanner = '//*[@id="center_column"]/p'

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.noResultBanner).text

    def return_section_title(self):
        return self.driver.find_element_by_xpath(self.resultadoXpath).text