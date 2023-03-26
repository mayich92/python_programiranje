# Je li riječ palindrom?

def palindrom(string):
    # return string == string[::-1]    # vraća True ili False
    vrijednost = ''
    if string == string[::-1]:
        vrijednost = 'Vaš string JE palindrom'
    else:
        vrijednost = 'Vaš string NIJE palindrom'
    return vrijednost

    # if string == string[::-1]:
    #     return 'Vaš string JE palindrom'
    # else:
    #     return 'Vaš string NIJE palindrom'

# while True:
#     unos = input('Unesite riječ (unesite KRAJ za kraj programa): ')
#     if unos.upper() == 'KRAJ':
#         break
#     print(palindrom(unos))

import random

izbori = ['kamen', 'škare', 'papir']

def evaluacija(unos, zamisljeni_izbor):
    if unos == zamisljeni_izbor:
        print(f"Neriješeno! Računalo je također odabralo {unos}")
    elif unos == 'kamen':
        if zamisljeni_izbor == 'škare':
            print('Pobijedili ste!')
        else:    # zamisljeni_izbor == papir
            print('Izgubili ste!')
    elif unos == 'škare':
        if zamisljeni_izbor == 'papir':
            print('Pobijedili ste!')
        else:    # zamisljeni_izbor == kamen
            print('Izgubili ste!')
    elif unos == 'papir':
        if zamisljeni_izbor == 'kamen':
            print('Pobijedili ste!')
        else:    # zamisljeni_izbor == škare
            print('Izgubili ste!')
    elif unos not in izbori:
        print("Niste unijeli validnu vrijednost! ")

def igra():
    while True:
        zamisljeni_izbor = random.choice(izbori)
        unos = input("Unesite kamen, škare ili papir: ")
        evaluacija(unos, zamisljeni_izbor)
        izlaz_iz_programa = input('Želite li završiti program (DA/NE)? ')
        if izlaz_iz_programa.lower() == 'da':
            break

igra()