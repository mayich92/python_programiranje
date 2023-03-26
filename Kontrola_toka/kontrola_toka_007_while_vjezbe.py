'''
Napravite aplikaciju za prikaz tablice množenja.
Korisnik treba moći unijeti do kojeg broja će se prikazati tablica.
'''

# granica = 10
# for i in range(1, granica+1):
#     for j in range(1, granica+1):
#         umnozak = i*j
#         print('{:>5}'.format(umnozak), end=' ')
#     print()

# print('-'*60)

# # i, j = 1, 1    # i=1;j=1

# i = 1
# while i < granica+1:
#     j = 1
#     while j < granica+1:
#         umnozak = i*j
#         print('{:>5}'.format(umnozak), end=' ')
#         j += 1
#     print()
#     i += 1


# while True:
#     granica = int(input('Unesite veličinu tablice: '))
#     for i in range(1, granica+1):
#         for j in range(1, granica+1):
#             umnozak = i*j
#             print('{:>5}'.format(umnozak), end=' ')
#         print()
#     print('-'*(6*granica))
#     izlaz = input('Želite li završiti program (DA/NE)? ')
#     if izlaz == 'DA':
#         break


# KALKULATOR
while True:
    prvi_broj = input("Unesite prvi broj: ")
    drugi_broj = input("Unesite drugi broj: ")
    operacija = input("Unesite operaciju (+, -, *, /): ")
    operacija = operacija.strip()

    prvi_broj, drugi_broj = float(prvi_broj), float(drugi_broj)

    if drugi_broj == 0 and operacija == '/':
        print("Pripazite na dijeljenje s nulom!")
        continue

    rezultat = None
    if operacija == '+':
        rezultat = prvi_broj + drugi_broj
    elif operacija == '-':
        rezultat = prvi_broj - drugi_broj
    elif operacija == '*':
        rezultat = prvi_broj * drugi_broj
    elif operacija == '/':
        rezultat = prvi_broj / drugi_broj
    else:
        print("Nažalost vaša operacija nije podržana! ")
        continue

    print(f"Rezultat vaše operacije je {rezultat}.")
    izlaz_iz_petlje = input("Želite li unijeti još brojeva (DA/NE)? ")
    if izlaz_iz_petlje.upper() == 'NE':
        break
