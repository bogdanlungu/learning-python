# This program opens an url and extracts the data from it

# It extracts text, styles and JavaScript


import urllib.request
from html.parser import HTMLParser


class ParseHTML(HTMLParser):

    def handle_data(self, data):
        print("", data)

parser = ParseHTML()


def get_content():
    with urllib.request.urlopen("http://www.bbc.co.uk/") as url:
        s = url.read()
        s = s.decode(encoding='UTF-8', errors='ignore')
        s = parser.feed(s)
        print(s)

get_content()
