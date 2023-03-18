lista1 = [4, 5, 6]
lista1.append(7)
lista2 = lista1
lista3 = lista1.copy()
lista1.append(8)

id1 = id(lista1)
id2 = id(lista2)
id3 = id(lista3)

# print(f'Lista 1: {lista1}\t{id1}')
# print(f'Lista 2: {lista2}\t{id2}')
# print(f'Lista 3: {lista3}\t{id3}')



# list comprehensions

n = 20
lista_kvadrata = []
for i in range(1, n+1):
    lista_kvadrata.append(i ** 2)
    # kvadrat = i**2
    # lista_kvadrata.append(kvadrat)
# print(lista_kvadrata)

lista_kvadrata_lc = [i**2 for i in range(1, n+1)]
print(lista_kvadrata_lc)
lista_kubova_lc = [i**3 for i in range(1, n+1)]
print(lista_kubova_lc)

abeceda_lc = [chr(i) for i in range(65, 90+1)]
print(abeceda_lc)

lista_vrijednosti = [3.14, 2.71, 9.99, 49]
lista_kalkulacija = [vrijednost**0.5 for vrijednost in lista_vrijednosti]
print(lista_kalkulacija)