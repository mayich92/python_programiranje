# lista = [3,5,4,1]
# sortirana_lista = sorted(lista)     # .sort() specifično za liste funkcionira i mijenja izvornu listu
# print(sortirana_lista, lista)


# string = "\""
# print(string)


stringovi = [
    '\t',   #tabluator (tipka TAB)
     # '\n' # novi red
    '\a',   #specijalni znak
    '\"',   # obični dvostruki navodnici
    '\'',   # obični jednostruki navodnici
    '\c',   # invalid escape charachter
    '\ ',   # invalid escape charachter
    r'\t',  # raw string
]

for string in stringovi:
    print(string)
