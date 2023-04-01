# Zadatak 15. - Hangman

import random

wordbank = [
    'traka',
    'evaluacija',
    'datoteka'
]


def hangman():
    odabrana_rijec = random.choice(wordbank)
    maskirana_rijec = ['_' for c in odabrana_rijec]
    # maskirana_rijec = ' '.join(maskirana_rijec)
    pokusaja = 6
    iskoristeno = []
    while pokusaja > 0 and "_" in maskirana_rijec:
        print('-' * 50)
        print("Riječ: ", ' '.join(maskirana_rijec))
        print("Broj pokušaja: ", pokusaja)
        print("Iskorištena slova: ", end='')
        print(*iskoristeno, sep=' ')
        slovo = ""
        while not slovo.isalpha() or len(slovo) != 1:
            slovo = input("Unesite slovo: ")
        if slovo in iskoristeno:
            print("Već ste iskoristili to slovo! ")
            continue
        else:
            iskoristeno.append(slovo)

        if slovo in odabrana_rijec:
            print(f"Vaše slovo se pojavljuje {odabrana_rijec.count(slovo)} puta u riječi!")
            for i in range(len(odabrana_rijec)):
                slovo_rijeci = odabrana_rijec[i]
                if slovo_rijeci == slovo:
                    maskirana_rijec[i] = slovo
        else:
            pokusaja -= 1
            print("Vaše slovo se ne nalazi u riječi! ")
            continue
    if pokusaja == 0:
        print(f"Nažalost niste pogodili riječ, riječ je bila: {odabrana_rijec}")
    else:
        print(f"Bravo! Pogodili ste riječ, riječ je bila: {odabrana_rijec}")


print("Dobrodošli u Hangman!")
while True:
    hangman()
    izlaz = input("Želite li nastaviti igrati (da/ne)? ").lower()
    if izlaz == 'ne':
        break