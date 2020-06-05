from selenium import webdriver

DRIVER_PATH = 'Chromedriver.exe'

def get_driver():
    return webdriver.Chrome(DRIVER_PATH)