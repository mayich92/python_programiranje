
class Parent:
    parent_attr = 100
    def __init__(self):
        print('Pozivanje konstruktora Parent')
    
    def parent_method(self):
        print("Pozivanje Parent metode")
    
    def neka_metoda(self):
        print('Neka metoda Parent')

class Child(Parent):
    def __init__(self):
        print("Pozivanje konstruktora Child")
    
    def neka_metoda(self):
        print('Neka metoda Child')


p1 = Parent()
c1 = Child()

c1.parent_method()
p1.neka_metoda()
c1.neka_metoda()
print(Child.parent_attr)