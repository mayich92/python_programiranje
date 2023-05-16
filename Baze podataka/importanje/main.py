
from citanje_iz_jsona import process_json

filepaths = [
    'Baze podataka/importanje/pinovi.json', 
    'Baze podataka/importanje/pinovi2.json'
]


all_dct = {}
for filepath in filepaths:
    dct = process_json(filepath)
    # all_dct = {**dct, **all_dct}
    all_dct.update(dct)

print(all_dct)