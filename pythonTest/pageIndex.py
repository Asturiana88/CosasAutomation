class PageIndex():
    def __init__(self, myDriver):
        self.queryTop = 'search_query_top'
        self.submitSearch = 'submit_search'
        self.driver = myDriver

    def search(self, item):
        self.driver.find_element_by_id(self.queryTop).send_keys(item)
        self.driver.find_element_by_name(self.submitSearch).click()
