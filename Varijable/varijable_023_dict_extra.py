adresar = {
    'Ivaa': 'Osijek',
    'Bojana': 'Zagreb',
    'Bruno': 'Rijeka'
}

# ispravljanje imena ključa
adresar['Ivana'] = adresar.get('Ivaa')
adresar.pop('Ivaa')

adresar['Zvonimir'] = 'Split'
adresar['Bruno'] = 'Crikvenica'

# prvi_izbaceni = adresar.popitem()    # adresar.pop('Zvonimir')
# drugi_izbaceni = adresar.popitem()
# print(prvi_izbaceni, drugi_izbaceni)

# adresar.clear()    # briše sve stavke u rječniku
print(adresar)
print(adresar['Ivana'])
print(adresar.get('Bojana'))
print(adresar.get('Anita', 'TBD'))

print(adresar.items())
print(adresar.keys())
print(adresar.values())

# naprednije
print(sorted(list(adresar.keys())))
print(sorted(list(adresar.values())))