# zadatak 25.
# Napisati program u PY koji korisniku daje informacije o trenutnom valutnim tečajevima. Primjerice, ako korisnik zatraži informacije za DKK (dansku krunu), ispisat će mu se:
# Trenutni tečaj za valutu DKK (država: Danska):
# Kupovni za devize: 7,676281
# Srednji za devize: 7,452700
# Prodajni za devize: 7,229119
# Aktualnu tečajnu listu scrapati s HPB poveznice  : https://www.hpb.hr/hr/tecajna-lista/2652


import requests
from bs4 import BeautifulSoup

def get_exchange_rates(currency_code):
    url = "https://www.hpb.hr/hr/tecajna-lista/2652"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", {"class": "tecajnica-table"})
    rows = table.tbody.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if cols[0].text.strip() == currency_code:
            country = cols[1].text.strip()
            buying_rate = cols[2].text.strip().replace(",", ".")
            middle_rate = cols[3].text.strip().replace(",", ".")
            selling_rate = cols[4].text.strip().replace(",", ".")
            print(f"Trenutni tečaj za valutu {currency_code} (država: {country}):")
            print(f"Kupovni za devize: {buying_rate}")
            print(f"Srednji za devize: {middle_rate}")
            print(f"Prodajni za devize: {selling_rate}")
            break
    else:
        print(f"Valuta {currency_code} nije pronađena u tečajnoj listi.")

# Primjer poziva funkcije za dansk kronu
get_exchange_rates("DKK")
