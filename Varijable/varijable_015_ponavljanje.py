a = 5          # integer, int()
# a += 1       # a = a + 1
b = 3.14       # float, float()
c = "tekst"    # string, (str)
d = True       # boolean, bool()
e = "r"        # string duljine 1

lista = [a, b, c, d, e]
print(lista)

f = 2

zbroj = a + b     # 8.14
dijeljenje = a / f   # 2.5
cjelobrojno_dijeljenje = a // f   #2(.5 se odbacuje)
modulo = a % f     #1
potencija = a ** f #25

tekst = "abcd"
print(tekst[0])    #a
print(tekst[1:3])  # bc
print(tekst[-1])   #d
print(tekst[::-1]) #dcba
print(tekst[::2])  #ac

tekst = tekst.upper()

# .lower()
# .capitalize()
# .title()

lista = list(tekst)
tekst2 = "12,34"
cijena = tekst2.split(".")
print(cijena[0])

lista = ["12", "34"]
cijena_string = ".".join(lista)
print(cijena_string)

lista = [True, "tekst"]
lista.append(1)
# remove, pop za uklanjanje

# .sort() .reverse()
lista.extend([2,3])

 # .index(), .count()
 for element in lista:
     print(element, end='\n\n')