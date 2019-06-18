""" 
    Exemplo de PO no google.com
"""
from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'q'
        self.btn_search = 'btnK'
        self.btn_lucky = 'btnI'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)

        self.driver.find_element_by_name(
            self.btn_search).click()
    
    def lucky(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
            
        self.driver.find_element_by_name(
            self.btn_lucky).click()


ch = webdriver.Chrome()
g = Google(ch)
g.navigate()
g.lucky('live de python')

# fechar navegador
# ch.quit() 