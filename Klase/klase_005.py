
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_person(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

e1 = Employee('Domagoj', 27, 10000)
print(e1.name, e1.salary)
e1.print_person()

a = 5
print(type(a))
print(type(a) == int)
print(isinstance(a, int))

b = {}
print(isinstance(b, set))
print(isinstance(b, dict))

print('-'*50)
print(type(e1))
print(type(e1) == Person)
print(isinstance(e1, Employee))
print(isinstance(e1, Person))

print(issubclass(Person, Employee))
print(issubclass(Employee, Person))