
class Employee:

    employee_count = 0
    cumm_salary = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
        Employee.cumm_salary += self.salary
    
    def display_employee(self):
        print(f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}')
    
    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}'

    # __add__, __sub__, __mul__, ..., __mod__, __pow__, ..., __lt__, __gt__, __eq__, __ge__...

    # def __eq__(self, other):
    #     return self.salary == other.salary    


e1 = Employee('Alice', 'Data Scientist', 7_000)
e2 = Employee('Charlie', 'Software Developer', 12_000)
e3 = Employee('Bob', 'Data Engineer', 8_000)


employees = [e1, e2, e3]
for e in employees:
    e.display_employee()

print("Ukupni trošak na zaposlenike: ", Employee.cumm_salary)


print(e1 < e2)
employees.sort()
for e in employees:
    e.display_employee()

print('-'*50)
print(str(e1))