# from pprint import pprint    # pretty print

adresar = {
    "Domagoj": "+385 99 123 4567",
    "Marko": "+385 1 789 4563"
}

# print(adresar)    # ispis cijelog rječnika u jednom redu
# pprint(adresar)    # kod velikih rječnika korisno za ispis po linijama (pregledniji ispis)

adresar["Vanja"] = "+385 456 4567"    # dodavanje nove stavke u rječnik

print(adresar['Domagoj'])    # vraća vrijednost za ključ Domagoj
# print(adresar['Denis'])    # proizvodi error jer Denisa nema među ključevima
print(adresar.get('Denis'))    # vraća None (type -> NoneType)
print(adresar.get('Vladimir', 'Tog imena nema u adresaru! '))    # postavljena defaultna vrijednost je vraćena


print(adresar.items())
print(adresar.keys())
print(adresar.values())

print(list(adresar.keys()))

for key in adresar.keys():
    print(f'Ime: {key}\tBroj telefona: {adresar[key]}')
    # print(key, adresar[key])