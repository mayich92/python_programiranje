
adresar = {
    'Domagoj': 'Zagreb',
    'Alice': 'New York',
    'Angela': 'Berlin'
}

lista_osoba = ['Alice', 'Angela', 'Bob']

# prekinut će program    # KeyError
# for osoba in lista_osoba:
#     mjesto = adresar[osoba]
#     print(f"Osoba: {osoba}    Mjesto: {mjesto}")

for osoba in lista_osoba:
    if osoba in adresar.keys():
        mjesto = adresar[osoba]
    else:
        mjesto = 'nedefinirano'
    print(f"Osoba: {osoba}    Mjesto: {mjesto}")


print('-'*50)

for osoba in lista_osoba:
    try:
        mjesto = adresar[osoba]
    except KeyError:
        mjesto = 'nedefinirano'
    print(f"Osoba: {osoba}    Mjesto: {mjesto}")

print('-'*50)
try:
    2.5 * 'test'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except:
    print('Nepoznati error')

print('ostatak programa')