"""Spider for crawling the web
"""
# pylint: disable=C0103

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com'
the_html = requests.get(url)
the_html_text = the_html.text

soup = BeautifulSoup(the_html_text, 'lxml')
for link in soup.findAll('a'):
    href = link.get('href')
    print(href)
