lista = [1, 2, 3]
lista_prvi = lista[0]

skup = {1, 2, 3}

rjecnik = {'a': 1, 'b': 2}

prazan_rjecnik = {}
prazan_set = set()
prazna_lista = []

# lista[1] = 5
# rjecnik['b'] = 3
# skup.add(4)
# skup.remove(3)
# print(skup)

ntorka = (4, 5, 6)
# print(ntorka[0])
# ntorka[1] = 7    # ne može, zato što je tuple immutable, isto kao string

string = 'abc'
# string[-1] = 'd'    # string je isto immutable

# ntorka.append(7)    # ne postoji metoda, nije moguće mijenjati vrijednosti tuplea
# ntorka.add(7)    # ista stvar

prvi, drugi, treci = ntorka
nova_ntorka = prvi, treci
# print(nova_ntorka)


# masa, visina = float(input('Unesite masu')), float(input('Unesite visinu'))
# print(masa)
# print(visina)

a = 5
b = 6
# a, b = 5, 6
# a, b, c = 7, 8, 9
# print(c)

a = 5
b = 6

# u drugim prog. jezicima potrebno uvesti pomoćnu varijablu
# tmp = b
# b = a
# a = tmp

a, b = b, a

# print(a, b)


dct = {
    'Maja': 3,
    'Denis': 2
}

items = list(dct.items())

for i in dct.items():
    key, value = i
    print(f'Ključ: {key}\tVrijednost: {value}')
    # for element in i:
    #     print(element)

# t = ('a', 'b', 'c')
# for element in t:
#     print(element)

t = ('a', 'b', 'b', 'b', 'c')
print(t.count('b'))
print(t.index('b'))