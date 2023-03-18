# lista = []
# for i in range(20, 31):
#     lista.append(i)
# print(lista)


# Napraviti konzolni program koji u tekstu koji korisnik unese prebrojava riječi i vraća rezultat korisniku na prikaz.
# Primjer izvršavanja:
# Dobrodošli u brojač riječi!
# Unesite tekst: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Vaš tekst ima 19 riječi.
'''
print("Dobrodošli u brojač riječi!")
tekst = input("Unesite tekst po želji: ")
rijeci = tekst.split()
broj_rijeci = len(rijeci)
print(f'Vaš tekst ima {broj_rijeci} riječi.')
'''

#  Napisati program koji pretvara inče u centimetre. Korisnik u konzolu ukuca broj inča, a program u konzolu ispisuje koliko je to centimetara.
# Primjer izvršavanja:
# Unesite duljinu u inčima: 1.2
# Pretvorena duljina je 3.048 cm.

'''
duljina = float(input("Unesite duljinu u inčima: "))
C = 2.54
pretvorena_duljina = duljina*C   #cm
print(f'Pretvorena duljina je {pretvorena_duljina} cm.')
'''

 # Napisati program koji za unesenu masu (u kilogramima) i visinu (u centimetrima) računa BMI indeks (BMI = masa [kg] / visina [m])

'''
masa = float(input("Unesite svoju težinu u kilogramima: "))
visina = float(input("Unesite svoju visinu u centimetrima : "))
BMI = masa / visina/0.01
print(f'Vaš BMI indeks je {BMI}')
'''

# Napisati program koji čita od korisnika iz konzole ime neke datoteke, a ispisuje u konzolu ekstenziju te datoteke te koji je to tip datoteke,
# sudeći po ekstenziji (npr. za ".py" ispisat će "Vaša datoteka ima ekstenziju .py i to je Python source kod").
# Napomene:
# program treba prepoznavati barem 3 različita tipa datoteka (proizvoljno odaberite)
# NE koristiti IF-ELIF-ELSE blokove, dovoljno je ono što smo naučili dosad
# uneseno ime datoteke može imati nekoliko točaka, npr. "neko.ime.datoteke.pdf" je validno ime za PDF datoteku
# dodatni bodovi: osigurati slučaj unošenja programu "nepoznate" ekstenzije
# Primjer izvršavanja:
# Unesite ime datoteke: dokument.docx
# Vaša datoteka ima ekstenziju .docx i to je Microsoft Word dokument.

# import os
#
# ime_datoteke = input("Unesi ime datoteke: ")
# ime_datoteke = os.path.splitext(ime_datoteke)
# ekstenzija = ime_datoteke[1]
#
# lista_datoteka = [".py", ".pdf", ".doc"]
# try:
#  pozicija = lista_datoteka.index(ekstenzija)
#
#  datoteke = {
#  ".py" : "Python source kod",
#  ".pdf" : "pdf datoteka",
#  ".doc" : "Microsoft datoteka"
#  }
#
#  print(f'Vaša datoteka ima ekstenziju {ekstenzija} i to je {datoteke.get(ekstenzija)}.')
# except ValueError as ve:
#  print(f'Unijeli ste ekstenziju {ekstenzija}, koja nije na listi')


# Napisati program koji je naprednija inačica programa iz zadatka 1 - program kao input prima tekst od korisnika, a kao izlaz izlistava sve jedinstvene riječi u tom tekstu abecednim redom.
# Napomene:
# pripaziti na interpunkcijske znakove (da vam primjerice zarez ne poremeti dvije identične riječi)
# rješenje treba raditi case-insensitive (RIJEČ i riječ se tretiraju kao jedno)
# Primjer izvršavanja:
# Dobrodošli u izlistavač jedinstvenih riječi!
# Unesite tekst: Svi za jednog, jedan za sve!
# Lista jedinstvenih riječi u Vašem tekstu:
# jedan
# jednog
# sve
# svi
# za

# import string
# print("Welcome to printing words program!")
# text = input("Enter your sentence: \n").lower()
#
# text = text.split()
# unique_words = [''.join(char for char in string if char.isalnum()) for string in text]
# unique_words = set(unique_words)
# unique_words = sorted(unique_words)
# for word in unique_words:
#     print(word)



# Napisati program koji kroz konzolu od korisnika prima listu brojčanih vrijednosti odvojenih zarezima te računa sljedeće:
# a) zbroj svih unesenih vrijednosti korištenjem integrirane funkcije sum()
# b) zbroj svih unesenih vrijednosti bez korištenja integriranih funkcija (neka rezultat iz a) dijela služi kao kontrola)
# c) umnožak svih unesenih vrijednosti (jako sličan princip kao u b))
# Napomena:
# neka svi rezultati kalkulacija budu zaokruženi na dva mjesta iza decimalne točke
# Primjer izvođenja:
# Unesite brojčane vrijednosti odvojene zarezom: 1.234, 5.678, 9
# Unesene vrijednosti su:  [1.234, 5.678, 9.0]
# Zbroj dobiven uz sum():  15.91
# Zbroj dobiven ručno:  15.91
# Umnožak dobiven ručno:  63.06

# numbers = input("Unesite brojčane vrijednosti odvojene zarezom:").replace(",", "").split()
# num_list = []
# for i in numbers:
#  i = float(i)
#  num_list.append(i)
# print(round(sum(num_list), 2))
#
# rucni_sum = 0.0
# for i in num_list:
#  rucni_sum = rucni_sum+i
# print(round(rucni_sum, 2))
#
# rucni_umnozak = 1.0
# for j in num_list:
#  rucni_umnozak *=j
# print(round(rucni_umnozak, 2))



# Postići ispis stavki rječnika (za neki već popunjeni rječnik) u obliku liste n-torki (tuplova), kao što to ispisuje metoda .items(), ali bez korištenja navedene metode.
# Bonus bodovi:
# implementacija korištenjem list comprehensiona
# Primjer izvođenja:
# Rječnik:  {'a': 1, 'b': 2, 'c': 3}
# Ispis stavki rječnika koristeći .items(): [('a', 1), ('b', 2), ('c', 3)]
# Ispis stavki rječnika ručno: [('a', 1), ('b', 2), ('c', 3)]

