import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'
r = requests.get(url)

# 1. metoda
text_data = r.text
dct = json.loads(text_data)

# 2. metoda
json_data = r.json()

# for entry in json_data:
#     print(entry['name'])
#     print(entry['company']['name'])
#     print('-'*50)

domains = []
for entry in json_data:
    email = entry['email']
    domain = email.split('.')[-1]
    domains.append(domain)

from collections import Counter
c = Counter(domains)
print(c.most_common(3))