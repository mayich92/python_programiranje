'''
https://www.w3schools.com/python/python_ref_set.asp
'''

# a = {1, 4, 6, 7}
# b = {2, 3, 5, 6, 9, 10}
# c = {}    # prazan rječnik
# d = set()    # prazan skup

# a.add(9)
# b.remove(10)

# print(a)
# print(b)
# unija = a.union(b)    # b.union(a)
# presjek = a.intersection(b)    # b.intersection(a)
# razlika1 = a.difference(b)    # elementi u a koji nisu u b
# razlika2 = b.difference(a)    # elementi u b koji nisu u a

# print(unija)
# print(presjek)
# print(razlika1)
# print(razlika2)
# e = {1, 2}
# f = {3, 4}

# print(e.isdisjoint(f))    # vraća True ako dva skupa nemaju nijedan zajednički član


lista = [1, 5, 6, 5, 6, 7]
skup = set(lista)
lista = list(skup)
# lista = list(set(lista))
print(lista)


a = {'abc', 'd', 1, False, 0}    # boolean -> False i 0 se unutar seta tretiraju kao duplikati
print(a)
# b = {1, 2, {3, 4}}    # nema nested struktura

c = {0, 0, 1, 1, 2}
print(c)