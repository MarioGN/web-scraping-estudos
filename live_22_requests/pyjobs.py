from time import sleep

from collections import namedtuple
from requests import get
from bs4 import BeautifulSoup as bs


def trata_str(string):
    return string.split(':')[1].strip()

def get_links(url):
    pyjobs_request = get(url)
    page = bs(pyjobs_request.text, 'html.parser')
    page_list = page.find_all('a', {'class': 'page-link'})

    return [link.get('href') for link in page_list] 

def get_jobs(url):
    pyjobs_request = get(url)
    page = bs(pyjobs_request.text, 'html.parser')
    boxes = page.find_all('div', {'class': 'card-body'})[4:]

    for box in boxes:
        titulo = box.find('h4').text
        localizacao = box.find_all('h6')[0].text
        postagem = box.find_all('h6')[1].text
        skills = [span.text for span in box.find_all('span')]
        
        yield vaga(titulo, trata_str(localizacao), trata_str(postagem), skills)


vaga = namedtuple('Vaga', 'titulo localizacao postagem skills')

base_url = 'https://www.pyjobs.com.br'
start_url = f'{base_url}/?page=1'

links = get_links(start_url)


for link in links:
    sleep(1)
    url = ''.join([base_url, link])
    jobs = get_jobs(''.join([base_url, link]))

    for job in jobs:
        print('\n', job)
