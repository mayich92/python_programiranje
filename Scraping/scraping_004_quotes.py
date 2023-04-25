import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, "html.parser")
quotes = soup.find_all('div', class_='quote')    
# quotes = soup.find_all('div', {'class': 'quote'})    # alternativan način za specifikaciju klase

# prvi = quotes[0]
# print(prvi.find('span', class_='text').text)
# print(prvi.find('small', class_='author').text)

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'Tekst: {text}')
    print(f'Autor: {author}')