import requests
from bs4 import BeautifulSoup

url = "https://www.whatsmyua.info/"

headers = {'User-Agent': 'Algebra Python Programiranje'}
r = requests.get(url, headers=headers)
data = r.text

soup = BeautifulSoup(data, "html.parser")
rawua = soup.find('li', {'id': 'rawUa'}).text
print(rawua)