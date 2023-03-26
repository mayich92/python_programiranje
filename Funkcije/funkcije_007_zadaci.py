# Zadatak 14.
# simulirati dječju igru "par-nepar"

import random

izbori = ['par', 'nepar']

def validate_fingers(finger_number):
    if 0 <= finger_number <= 10:
        return True
    else:
        return False

def evaluacija(prsti_korisnik, prsti_racunalo, pn):
    zbroj = prsti_korisnik + prsti_racunalo
    if (zbroj % 2 == 0 and pn == 'par') or (zbroj % 2 == 1 and pn == 'nepar'):
        status = 'pobjeda'
    else:
        status = 'poraz'
    return status

def igra():
    print("Dobrodošli u igru Par-nepar!")
    while True:
        pn = input("Unesite par ili nepar: ").lower()
        if pn not in izbori:
            continue
        unos_prstiju = -1
        while not validate_fingers(unos_prstiju):
            unos_prstiju = int(input("Unesite broj prstiju koje ćete pokazati (0-10): "))
        # racunalo = random.choice(izbori)    # random.choices(izbori, k=1) ili random.choices(izbori)[0]
        racunalo = random.randint(0, 10)
        # print(pn, unos_prstiju, racunalo)
        # if unos_prstiju > 10 or unos_prstiju < 0:
        #     continue
        status = evaluacija(unos_prstiju, racunalo, pn)
        print(f"Računalo je pokazalo {racunalo} ", end='')    # alternativno koristiti dictionary
        if racunalo == 1:
            print("prst. ")
        elif racunalo in [2, 3, 4]:
            print("prsta. ")
        else:
            print("prstiju. ")
        print(f"Status: {status}")

        # Izlaz iz while loopa
        izlaz = input('Želite li izaći iz programa (DA/NE)? ').upper()
        if izlaz == 'DA':
            print("Hvala Vam na igranju igre Par-nepar! ")
            break

igra()
# igra()