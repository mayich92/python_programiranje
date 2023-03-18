# Zadatak 4. - napisati program koji izlistava JEDINSTVENE riječi u unesenom tekstu abecednim redom
# paziti na interpunkciju i case
# text = input("Unesite Vaš tekst: ")
# text = text.lower()

# # text = text.replace(".", "").replace("?", "").replace(",", "").replace("!", "")
# interpunkcija = ['.', '?', '!', ',']
# interpunkcija = ".?!,"
# for inter in interpunkcija:
#     text = text.replace(inter, "")
# # text = text.strip(".,?!")

# words = text.split()
# words = set(words)
# words = list(words)
# # words = list(set(words))
# words.sort()
# # words = sorted(words)

# for word in words:
#     print(word)


# Zadatak 5. - napisati program koji računa sumu i umnožak unesenih brojčanih vrijednosti odvojenih zarezom
# a) sum()    b) zbroj    c) umnožak

# unos = input("Unesite Vaše vrijednosti odvojene zarezom: ")
# vrijednosti = unos.split(',')
# vrijednosti = [float(v) for  v in vrijednosti]
# # vrijednosti = [float(v.strip()) for  v in vrijednosti]
# print(f"Zbroj pomoću sum() je {sum(vrijednosti)}")

# zbroj = 0
# umnozak = 1
# for v in vrijednosti:
#     zbroj += v
#     umnozak *= v
# # zbroj = round(zbroj, 2)
# # umnozak = round(umnozak, 2)

# zbroj, umnozak = round(zbroj, 2), round(umnozak, 2)

# print(f"Zbroj bez sum() je {zbroj}")
# print(f"Umnožak je {umnozak}")

# Zadatak 6. - simulirati formu .items() za neki rječnik

# dct = {'a': 1, 'b': 5, 'c': 8}
# print("Stavke: ", list(dct.items()))

# lista_tuplova = []
# for kljuc in dct.keys():
#     vrijednost = dct[kljuc]
#     tupl = (kljuc, vrijednost)
#     lista_tuplova.append(tupl)

# print("Stavke: ", lista_tuplova)

# lista_tuplova_lc = [(kljuc, dct[kljuc]) for kljuc in dct.keys()]

# print("Stavke: ", lista_tuplova_lc)


a = 1
b = 2
c = 3
t = a,b,c
a = 2
d,e,f = t
print(a,b,c,d,e,f,t)