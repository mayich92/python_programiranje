# lista = ["tekst", 1, 2.3]
# lista = [1, 2, 3]
# kvadrati = []
# for element in lista:
#     kvadrati.append(element**2)
# print(kvadrati)
#     #print(element*2, end=" ")
#
#
# stringovi = ["ab", "cd", "ef"]
# obrnuti_stringovi = []
# for string in stringovi:
#     obrnuti_stringovi.append(string[::-1])
#
# for stavka in obrnuti_stringovi:
#     print(stavka)


# lista = ["prvi", "drugi", "treci", "cetvrti"]
# for tekst in lista:
#     print(tekst)

# for i in range(len(lista)):
#     element = lista[i]
#     print(element)

lista = ["prvi", "drugi", "treci", "cetvrti"]
for i, element in enumerate(lista):
        print("Element {} nalazi se na indeksu {}".format(element, i))

BROJ_PONAVLJANJA = 10
for i in range(BROJ_PONAVLJANJA):    #umjesto i, ako ga ne koristimo, možemo staviti _
    print("Python")
