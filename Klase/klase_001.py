
class Person:
    broj_osoba = 0
    sva_imena = []

    def __init__(self, input_name, age):
        self.name = input_name
        self.person_age = age
        Person.broj_osoba += 1
        Person.sva_imena.append(self.name)

p1 = Person('Domagoj', 27)
p2 = Person('Ana', 20)
p3 = Person("Ružica", 41)
print(p1.name, p1.person_age)
print(p2.name, p2.person_age)
print(Person.broj_osoba)
print(Person.sva_imena)