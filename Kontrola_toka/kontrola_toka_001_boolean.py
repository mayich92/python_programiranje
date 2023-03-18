a = 5
b = 3

a = 'g'
b = 'h'

# print(f"{a} > {b}: {a > b}")
# print(f"{a} < {b}: {a < b}")
# print(f"{a} == {b}: {a == b}")
# print(f"{a} != {b}: {a != b}")
# print(f"{a} <= {b}: {a <= b}")
# print(f"{a} >= {b}: {a >= b}")


c = 6
d = 5

# print(not c % d == 0)

ime = "Domagoj"
prezime = "Marić"
# print(ime != "Dominik" and prezime == "Marić")
# print(not ime == "Dominik" and prezime == "Marić")
# print(ime == "Dominik" or prezime == "Marić")

lista = [1, 2, 3]
# print(2 in lista)
# print(not 2 in lista)
# print(2 not in lista)

lista1 = list(range(10))
lista2 = list(range(200))
# print(len(lista1) > len(lista2))


lista3 = [5, 6, 4]
# print(sum(lista3))
# print(max(lista3))
# print(min(lista3))

# print(5 > 4 is True)
# print(5 > 4)
# print(5 > 4 is False)
# print(not 5 > 4)

broj = 4
# print(type(broj) == int)

dct = {'a':1, 'b':2}
value = dct.get('c')
# print(value is None)    # izbjegavati operator "is"

# print(id(value))
# print(id(None))

prvi = True
drugi = False
# NOR
nor = not(prvi or drugi)

# NAND
nand = not(prvi and drugi)

prvi = [True, False]
drugi = [True, False]
print('Prvi Drugi NOR NAND')
for i in prvi:
    for j in drugi:
        nor = not(i or j)
        nand = not(i and j)
        print(i, j, nor, nand)