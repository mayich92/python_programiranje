# Zadatak 8.
# Napisati program koji kroz konzolu od korisnika prima listu brojčanih vrijednosti odvojenih zarezima te ispisuje najveću vrijednost u listi:
# a) korištenjem ugrađene funkcije max()
# b) korištenjem sortiranja (bez modificiranja liste)
# c) iteriranjem kroz listu i manualnom provjerom
# Primjer izvođenja:
# Unesite brojčane vrijednosti odvojene zarezom: 1, 76, 5, 260, 0.3
# Unesene vrijednosti su:  [1.0, 76.0, 5.0, 260.0, 0.3]
# Najveća vrijednost (pomoću funkcije max):  260.0
# Najveća vrijednost (pomoću sortiranja):  260.0
# Najveća vrijednost (manualno, pomoću iteriranja):  260.0

user_list = input("Unesite brojčane vrijednosti odvojene zarezom:").split(',')
user_list = ([float(num) for num in user_list])
print(f"Unesene vrijednosti su: {user_list}")
sorted_list = sorted(user_list)
print(f"Najveća vrijednost (pomoću funkcije max): {max(user_list)}")
print(f"Najveća vrijednost (pomoću sortiranja): {(sorted_list[-1])}")

largest_number = user_list[0]
for num in user_list:
    if num > largest_number:
        largest_number = num
print(f"Najveća vrijednost (manualno, pomoću iteriranja): {largest_number}")
