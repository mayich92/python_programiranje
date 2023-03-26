import random

izbori = ['kamen', 'škare', 'papir']

while True:
    zamisljeni_izbor = random.choice(izbori)
    unos = input("Unesite kamen, škare ili papir: ")
    if unos == zamisljeni_izbor:
        print(f"Neriješeno! Računalo je također odabralo {unos}")
    elif unos == 'kamen' and zamisljeni_izbor == 'škare':
        print(f"Pobijedili ste, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos == 'škare' and zamisljeni_izbor == 'papir':
        print(f"Pobijedili ste, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos == 'papir' and zamisljeni_izbor == 'kamen':
        print(f"Pobijedili ste, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos == 'škare' and zamisljeni_izbor == 'kamen':
        print(f"Računalo je pobijedilo, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos == 'kamen' and zamisljeni_izbor == 'papir':
        print(f"Računalo je pobijedilo, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos == 'papir' and zamisljeni_izbor == 'škare':
        print(f"Računalo je pobijedilo, računalo je zamislilo {zamisljeni_izbor}!")
    elif unos not in izbori:
        print("Niste unijeli validnu vrijednost! ")
        continue
    izlaz_iz_programa = input('Želite li završiti program (DA/NE)? ')
    if izlaz_iz_programa.lower() == 'da':
        break