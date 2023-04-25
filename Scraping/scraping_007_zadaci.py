import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.hnb.hr/statistika/glavni-makroekonomski-indikatori'
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')    # za brzinu koristiti lxml parser
# print(soup.prettify())
# table = soup.find('table', class_='border')
table = soup.find('tbody')
table_rows = table.find_all('tr')

all_table_data = []
for tr in table_rows:
    cells = tr.find_all('td')
    cell_data = [i.get_text() for i in cells]
    all_table_data.append(cell_data)

pprint(all_table_data)