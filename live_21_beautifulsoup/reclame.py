from time import sleep
from bs4 import BeautifulSoup as bs
from selenium import webdriver


base_url = 'https://www.reclameaqui.com.br'
url_site = f'{base_url}/empresa/positivo-informatica/lista-reclamacoes/'

chromeDriver = webdriver.Chrome()
chromeDriver.get(url_site)

bs_obj = bs(chromeDriver.page_source, 'html.parser')

boxes = bs_obj.find('ul', {'class': 'complain-list'}).find_all('li')

href_links = [box.find('a', {'class': 'link-complain-id-complains'}).get('href') for box in boxes]
page_links = [f'{base_url}{link}' for link in href_links]

for link in page_links:
    chromeDriver.get(link)
    sleep(2)
    bs_page = bs(chromeDriver.page_source, 'html.parser')
    title = bs_page.find('h1', {'class': 'ng-binding'}).text
    complain = bs_page.find('div', {'class': 'complain-body'}).find('p').text
    print(f'Titulo: {title} \nReclamação:\n{complain}\n\n')
