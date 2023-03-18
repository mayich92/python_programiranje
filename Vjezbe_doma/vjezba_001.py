# ime = input("Unesite Vaše ime: ")
# prezime = input("Unesite Vaše prezime: ")
# godina_rodenja = int(input("Unesite godinu Vašeg rođenja: "))
# trenutna_godina = 2023
# broj_godina =  trenutna_godina - godina_rodenja
# puno_ime_i_broj_godina = f"Bok, {ime} {prezime}, imaš {broj_godina}. godinu."
#
# print(puno_ime_i_broj_godina)


# lista = [1, 2, 3, 4, 5, 6, 7, "osam" , 9, 10]
# print(lista[-1])
# print(lista[4])
# print(lista[::2])
# jedan_broj = int(input("Unesite jedan broj: "))
# lista.append(jedan_broj)
# print(lista)
# lista.pop(7)
# print(lista)
# lista.remove(10)
# print(lista)

# ime = input("Unesite Vaše ime:")
# broj_godina = int(input("Unesite Vaš broj godina: "))
# broj_godina_za_pet_godina = broj_godina + 5
# print(f'Bok {ime}, za 5 godina imati cete {broj_godina_za_pet_godina} godina.')

# brojevi = []
# brojevi.append(float(input("Unesite broj: ")))
# brojevi.append(float(input("Unesite broj: ")))
# brojevi.append(float(input("Unesite broj: ")))
# brojevi.append(float(input("Unesite broj: ")))
# brojevi.append(float(input("Unesite broj: ")))
# prosjek = sum(brojevi) / len(brojevi)
# print(len(brojevi))
# print("Prosjek brojeva je:", prosjek)

pet_brojeva = []
pet_brojeva.append(float(input("Unesite broj: ")))
pet_brojeva.append(float(input("Unesite broj: ")))
pet_brojeva.append(float(input("Unesite broj: ")))
pet_brojeva.append(float(input("Unesite broj: ")))
pet_brojeva.append(float(input("Unesite broj: ")))


pet_brojeva.remove(max(pet_brojeva))
pet_brojeva.remove(min(pet_brojeva))
print("Preostali brojevi su: " , pet_brojeva)
