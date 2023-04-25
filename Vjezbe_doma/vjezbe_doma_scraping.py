# zadatak 25.
# Napisati program u PY koji korisniku daje informacije o trenutnom valutnim tečajevima. Primjerice, ako korisnik zatraži informacije za DKK (dansku krunu), ispisat će mu se:
# Trenutni tečaj za valutu DKK (država: Danska):
# Kupovni za devize: 7,676281
# Srednji za devize: 7,452700
# Prodajni za devize: 7,229119
# Aktualnu tečajnu listu scrapati s HPB poveznice  : https://www.hpb.hr/hr/tecajna-lista/2652

import requests
from bs4 import BeautifulSoup

url = 'https://www.hpb.hr/hr/tecajna-lista/2652'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', attrs={'class': 'tecajnaLista'})

currency_code = input('Unesite kod valute (npr. USD, EUR, DKK): ').upper()
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if cells[0].text == currency_code:
        country = cells[1].text
        buying_rate = cells[2].text
        middle_rate = cells[3].text
        selling_rate = cells[4].text
        print(f'Trenutni tečaj za valutu {currency_code} (država: {country}):')
        print(f'Kupovni za devize: {buying_rate}')
        print(f'Srednji za devize: {middle_rate}')
        print(f'Prodajni za devize: {selling_rate}')
        break
else:
    print('Nepoznati kod valute.')