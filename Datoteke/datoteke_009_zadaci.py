# Zadatak 23
# učitati vrijednosti iz datoteke vrijednosti.txt, red = prva/druga

# import os
# os.chdir('Datoteke')


from distutils.dir_util import copy_tree


filepath = 'vrijednosti.txt'
filepath = r'D:\Podaci\online4\Documents\Domagoj Marić\Python\Datoteke\vrijednosti.txt'
filepath = 'D:/Podaci/online4/Documents/Domagoj Marić/Python/Datoteke/vrijednosti.txt'
filepath = 'D:\\Podaci\\online4\\Documents\\Domagoj Marić\\Python\\Datoteke\\vrijednosti.txt'

with open(filepath, 'r', encoding='utf-8') as f:
    data = f.read()

rows = data.split('\n')
values = []

for row in rows:
    if '/' not in row:
        continue
    if row.count('/') > 1:
        continue
    prvi, drugi = row.split('/')
    try:
        prvi = float(prvi)
        drugi = float(drugi)
    except ValueError:
        continue
    t = (prvi, drugi)
    values.append(t)

max_value = values[0][0] / values[0][1]    # uzimamo prvi par kao traženi (max vrijednost)  # alternativno -inf
max_first, max_second = values[0][0] , values[0][1]
for value_pair in values:
    prvi, drugi = value_pair
    # if drugi == 0:
    #     continue
    try:
        kvocijent = prvi / drugi
    except ZeroDivisionError:
        continue
    if kvocijent > max_value:
        max_value = kvocijent
        max_first, max_second = prvi, drugi

print("Najveća vrijednost {} postignuta je kroz par vrijednosti {} i {}".format(max_value, max_first, max_second))
