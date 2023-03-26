
def isprintaj_bok():    # nema argumenata, ne vraća ništa
    print('Bok')
    print('Kako si')
    print('Što ima')

# isprintaj_bok()
# isprintaj_bok()

# for i in range(5):
#     isprintaj_bok()

# a = isprintaj_bok()
# print(a)

def isprintaj_string(tekst):    # prima 1 argument, ne vraća ništa
    print(tekst)

# isprintaj_string('bok')

def zbroj(a, b):    # prima 2 argumenta, zbraja ih, ne vraća ništa, ali ispisuje zbroj u konzolu
    c = a + b
    print(c)

# prvi = 5
# drugi = 6
# zbroj(prvi, drugi)
# b = zbroj(7, 8)
# print(b)

def obrnuti_string(tekst):    # prima 1 argument (u obliku stringa) i vraća 1 vrijednost na izlaz funkcije
    obrnuto = tekst[::-1]
    return obrnuto

rijec = 'Python'
obrnuta_rijec = obrnuti_string(rijec)
obrnuti_string('test')
# print(obrnuta_rijec)
# print(obrnuti_string(obrnuta_rijec))
# print(obrnuti_string('Java'))
# print(obrnuti_string(4))    # vraća grešku

def razlaganje_imena_datoteke(filename):     # prima jedan argument, vraća dvije vrijednosti kao tuple
    '''Ova funkcija vraca tuple (ime_datoteke_bez_ekstenzije, ekstenzija)'''
    dijelovi = filename.split('.')
    ekstenzija = dijelovi[-1]
    ostali_dijelovi = dijelovi[:-1]
    ostatak = '.'.join(ostali_dijelovi)
    return ostatak, ekstenzija

fajlovi = [
    'neka.datoteka.pdf',
    'nešto.docx',
    'skripta.py'
]
for fajl in fajlovi:
    # ekstenzija = razlaganje_imena_datoteke(fajl)[-1]
    # ime, ekstenzija = razlaganje_imena_datoteke(fajl)
    _, ekstenzija = razlaganje_imena_datoteke(fajl)
    # print(ekstenzija)


def produkt(prvi_broj, drugi_broj):
    return prvi_broj * drugi_broj

# print(produkt(2, 3))
# print(drugi_broj)    # drugi_broj definiran samo u dosegu svoje funkcije, unutar definicije funkcije

# help(razlaganje_imena_datoteke)

# print(obrnuti_string)

string1 = 'aplikacija'
string2 = obrnuti_string(string1)
string3 = str(string2.count('a'))
print(string1, string2, string3)

print(str(obrnuti_string('aplikacija').count('a')))