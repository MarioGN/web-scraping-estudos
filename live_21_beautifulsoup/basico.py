from selenium import webdriver
from bs4 import BeautifulSoup as bs


class Page:
    def __init__(self, driver):
        self.driver = driver


chromeDriver = webdriver.Chrome()
chromeDriver.get('http://google.com')

html = chromeDriver.page_source