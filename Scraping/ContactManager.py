from FileManager import *

import os
os.chdir('Scraping')

# f = open_file('fajl.txt', 'r')
# print(read_from_file(f))
# # write_to_file(f, 'CustomError je poruka')
# close_file(f)

class Osoba:
    def __init__(self, ime, oib, email, telefon, adresa):
        self.ime = ime
        self.oib = oib
        self.email = email
        self.telefon = telefon
        self.adresa = adresa
    
    def ispis(self):
        print('='*50)
        print(self.ime)
        # ...
        print(self.adresa)

class Djelatnik(Osoba):
    def __init__(self, ime, prezime, oib, email, telefon, adresa, radno_mjesto):
        super().__init__(ime, oib, email, telefon, adresa)
        self.prezime = prezime
        self.radno_mjesto = radno_mjesto
    
    def ispis(self):
        pass
        # za DZ
        # super().ispis()

class Kupac(Osoba):
    def __init__(self, ime, oib, email, telefon, adresa, djelatnost):
        super().__init__(ime, oib, email, telefon, adresa)
        self.djelatnost = djelatnost
    
    def ispis(self):
        pass

kupci = []
djelatnici = []

print('Pokrećem unos kupaca...')
while True:
    ime = input('Unesite ime kupca: ')
    # ...
    end = input('Želite li unijeti još kupaca?').lower()
    if end == 'NE':
        break

print('Pokrećem unos djelatnika...')
while True:
    ime = input('Unesite ime kupca: ')
    # ...
    end = input('Želite li unijeti još kupaca?').lower()
    if end == 'NE':
        break

# pohrana unesenih kupaca i djelatnika u odgovarajuće datoteke
# txt ili json

kupci = [
    {
        'ime': 'Domagoj',
        'oib': 12345678901
    },
    {
        'ime': 'Alice',
        'oib': 12345678901
    }
]
