

import requests

url = "https://www.algebra.hr"
zaglavlja = {'User-Agent': 'Python programiranje'}
r = requests.get(url, headers=zaglavlja)
data = r.text    # r.content

print(data)