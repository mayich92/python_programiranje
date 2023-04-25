import imp


import requests
import os

os.chdir('Scraping')

url = 'https://books.toscrape.com/'

r = requests.get(url)
data = r.text

filename = 'books.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(data)

