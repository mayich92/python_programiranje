
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name}    Age: {self.age}")

lista_osoba1 = []
osoba1 = ['Bojan', 15]
osoba2 = ['Damir', 20]
lista_osoba1.append(osoba1)
lista_osoba1.append(osoba2)

# print(*lista_osoba1, sep='\n')

lista_osoba2 = []
osoba1 = Person('Bojan', 15)
osoba2 = Person('Damir', 20)
lista_osoba2.append(osoba1)
lista_osoba2.append(osoba2)

# for osoba in lista_osoba2:
#     osoba.display_person()


class Vozilo:
    def __init__(self, tip, snaga, reg):
        self.tip = tip
        self.snaga = snaga
        self.reg = reg
    
    def prikazi_snagu(self):
        print(f"Snaga: {self.snaga}")

    def prikazi_marku(self):
        print(f"Marka: {self.marka}")

v1 = Vozilo('automobil', '200 KS', 'ZG-1234-AB')
print(v1.tip)
v1.tip = 'motocikl'
print(v1.tip)
v1.marka = 'BMW'
print(v1.marka)
v1.prikazi_marku()

# del v1.snaga    # izbjegavati brisanje atributa na instanci
# print(v1.snaga)

# hasattr, getattr, setattr, delattr
print(hasattr(v1, 'reg'))
print(hasattr(v1, 'prezime'))

setattr(v1, 'reg', 'OS-1234-AB')    # ekvivalentno v1.reg = 'OS-1234-AB'
print(getattr(v1, 'reg'))    # ekvivalentno print(v1.reg)

delattr(v1, 'snaga')    # ekvivalent del v1.snaga, također nije preporučljivo raditi
print(hasattr(v1, 'snaga'))