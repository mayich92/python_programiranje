# brojevi = []
# for broj in range(0, 10):
#     brojevi.append(broj)
# # brojevi = brojevi[::2]
# brojevi = brojevi[:-2]
#
# # for broj in brojevi:
# #     print(broj, end=" ")
# # print()
# # # print(*brojevi, sep=" ")    #napredna verzija ispisa bez for petlje
# #
#
# vanjska_lista = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# # print(*vanjska_lista, sep="\n")    #napredna verzija ispisa matrice bez for petlje u novom redu
#
# nova_vanjska_lista = []
# for red in vanjska_lista:
#     novi_red = []
#     for element in red:
#         novi_red.append(element*5)
#     nova_vanjska_lista.append(novi_red)
#
# print(*nova_vanjska_lista, sep="\n")

matrica = [
    ["ab", "cd", "ef"],
    ["qw", "er", "tz"],
    ["as", "df", "gh"]
]

domene = []
for red in matrica:
    red_domena = []
    for stavka in red:
        obradjena_stavka = "." + stavka
        red_domena.append(obradjena_stavka)
    domene.append(red_domena)

for red in domene:
        print(red)
