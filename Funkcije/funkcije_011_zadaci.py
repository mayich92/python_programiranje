# Zadatak 16. - program za generiranje nasumičnih lozinki spec. duljine

import random
import string

# PRVI NAČIN
mala_slova = 'abcdefghijklmnopqrstuvwxyz'
velika_slova = mala_slova.upper()
simboli = '!#$%&/()=?'
brojke = '0123456789'
# velika_slova = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
izbori = mala_slova + velika_slova + brojke
# izbori = list(izbori)

# DRUGI NAČIN
mala_slova = string.ascii_lowercase
velika_slova = string.ascii_uppercase
sva_slova = string.ascii_letters
brojke = string.digits
simboli = string.punctuation
izbori = sva_slova + brojke

# TREĆI NAČIN
# for i in range(1, 150):
#     print(i, chr(i))
velika_slova = [chr(i) for i in range(65, 91)]
mala_slova = [chr(i) for i in range(97, 123)]
simboli = [chr(i) for i in range(33, 48)]
brojke = [chr(i) for i in range(48, 58)]
izbori = mala_slova + velika_slova + brojke


def password(duljina_lozinke, koristi_simbole):
    if koristi_simbole == 'da':
        lst_password = random.choices(izbori + simboli, k=duljina_lozinke)
    else:
        lst_password = random.choices(izbori, k=duljina_lozinke)
    string_password = ''.join(lst_password)
    return string_password


def program():
    print("Dobrodošli u program za generiranje lozinki!")
    while True:
        duljina = int(input("Unesite duljinu lozinke (unesite 0 za kraj programa): "))
        if duljina == 0:
            print("Hvala na korištenju programa! ")
            break
        elif duljina < 0:
            print("Duljina lozinke mora biti pozitivna!")
            continue
        else:
            koristiti_simbole = input('Želite li koristiti simbole (da/ne)? ').lower()
            p = password(duljina, koristiti_simbole)
            print(f"Vaša generirana lozinka je {p}")

# program()