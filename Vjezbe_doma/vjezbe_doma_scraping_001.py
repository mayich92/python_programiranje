# Napisati program u PY koji servira korisniku trenutne meteo informacije o specificiranom mjestu (kratki opis stanja i temperaturu). Informacije možete preuzeti s ove stranice : https://www.vrijeme.net/
# Primjer izvođenja:
# Unesite ime mjesta: Čakovec
# Mjesto:  Čakovec
# Trenutno vrijeme:  malo oblačno
# Trenutna temperatura:  21°
# Napomene:
# testirajte da vaše rješenje radi za mjesta poput (hint: pogledajte što stoji u URL-u za određeno mjesto):
# Čakovec, Đakovo, Šibenik...
# Slavonski Brod, Sveti Martin na Muri...
# napredna inačica zadatka: pored trenutnog stanja servirati korisniku i prognozu za sljedeća 3 dana

import requests
from bs4 import BeautifulSoup

url = 'https://www.vrijeme.net/'
city = input('Unesite ime mjesta: ')

response = requests.get(f'{url}{city}.html')
soup = BeautifulSoup(response.text, 'html.parser')

try:
    location = soup.find('h1').text.strip()
    weather = soup.find('div', {'class': 'temp'}).text.strip()
    temperature = soup.find('div', {'class': 'stanje'}).text.strip()
    print(f"Mjesto: {location}")
    print(f"Trenutno vrijeme: {weather}")
    print(f"Trenutna temperatura: {temperature}")
except AttributeError:
    print('Nepoznato mjesto. Pokušajte ponovno.')

#napredna inačica

import requests
from bs4 import BeautifulSoup

url = 'https://www.vrijeme.net/'
location = input('Unesite ime mjesta: ')
params = {'lokacija': location}
response = requests.get(url, params=params)

soup = BeautifulSoup(response.content, 'html.parser')
city = soup.find('div', class_='lokacija-info').h1.text.strip()
condition = soup.find('div', class_='trenutno-info').span.text.strip()
temp = soup.find('div', class_='trenutno-temperatura').span.text.strip()

print(f'Mjesto: {city}')
print(f'Trenutno vrijeme: {condition}')
print(f'Trenutna temperatura: {temp}')

forecast_days = []
forecast_conditions = []
forecast_temps = []

forecast = soup.find_all('div', class_='prognoza-item')
for day in forecast[:3]:
    forecast_days.append(day.find('div', class_='prognoza-datum').text.strip())
    forecast_conditions.append(day.find('div', class_='prognoza-stanje').text.strip())
    forecast_temps.append(day.find('div', class_='prognoza-temperatura').text.strip())

print('Prognoza za sljedeća 3 dana:')
for i in range(3):
    print(f'{forecast_days[i]} - {forecast_conditions[i]}, {forecast_temps[i]}')
