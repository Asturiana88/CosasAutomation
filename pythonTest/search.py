import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItems import PageItems

class SearchCases(unittest.TestCase):

    def setUp(self): # for eachTest
     self.driver = webdriver.Chrome('Chromedriver.exe')
     self.driver.get('http://automationpractice.com/index.php')
     self.indexPage = PageIndex(self.driver)
     self.itemPage = PageItems(self.driver)

    
    def test_search_no_elements(self):
     self.indexPage.search('hola') 
     time.sleep(2)
     self.assertEqual(self.itemPage.return_no_element_text(), 'No results were found for your search "hola"')


    def test_search_find_dresses(self):
     self.indexPage.search('dress')  
     time.sleep(2)
     self.assertTrue('DRESS' in self.itemPage.return_section_title())


    def tearDown(self):
                    self.driver.close()
     self.driver.quit()


if __name__ == "__main__":
    unittest.main()