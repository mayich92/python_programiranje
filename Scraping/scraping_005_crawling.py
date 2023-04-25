import requests
from bs4 import BeautifulSoup
import time

url_template = "https://quotes.toscrape.com/page/"
DELAY = 2
page_to_end_on = 5
quotes_base = []
page = 1
while page <= page_to_end_on:
    url = url_template + str(page)
    print('Currently scraping: ', url)
    time.sleep(DELAY)
    r = requests.get(url)
    data = r.text

    soup = BeautifulSoup(data, "html.parser")
    quotes = soup.find_all('div', class_='quote')    
    if not quotes:
        break
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        t = (text, author)
        quotes_base.append(t)
    
    page += 1

for quote in quotes_base:
    print(quote[0])
    print(quote[1])
    print('-'*50)