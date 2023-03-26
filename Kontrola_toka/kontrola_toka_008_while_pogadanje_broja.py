'''
Sjećate se Računalnog razmišljanja i pogađanja broja između 1 i 100.
Sada imate dovoljno znanja da napišete program
koji će Vam omogućiti igranje igre pogađanje broja.
'''

import random

# import time


zamisljeni_broj = random.randint(1, 100)

broj_pokusaja = 0
while True:
    unos = input('Unesite broj: ')
    unos = int(unos)
    broj_pokusaja += 1
    if unos == zamisljeni_broj:
        print(f"Pogodili ste broj! Iskoristili ste {broj_pokusaja} pokušaja.")
        break
    elif unos > zamisljeni_broj:
        print("Vaš broj je VEĆI od zamišljenog broja!")
    elif unos < zamisljeni_broj:
        print("Vaš broj je MANJI od zamišljenog broja!")

