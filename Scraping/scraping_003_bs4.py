import requests
from bs4 import BeautifulSoup

url = "https://www.algebra.hr"

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, "html.parser")
paragrafi = soup.find_all('p')
# for paragraf in paragrafi:
#     print(paragrafi)

# print(paragrafi[0])
# print(paragrafi[0].text)

# for p in paragrafi:
#     print(p.text)
#     print('-'*200)

# poveznice = soup.find_all('a')
# hrefovi_poveznica = [i.get('href') for i in poveznice]
# print(*hrefovi_poveznica, sep='\n')

novosti = soup.find_all('div', class_='col-12 col-md-3')
print(novosti[0].get_text())
datum_prve_objave = novosti[0].find('time')
print(datum_prve_objave.text)
