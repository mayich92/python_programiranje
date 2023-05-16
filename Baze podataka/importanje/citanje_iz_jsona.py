import json

# dct = {'Domagoj': '1234', 'Admin':'4567'}
# with open('Baze podataka/importanje/pinovi.json', 'w') as f:
#     json.dump(dct, f, indent=4)

def process_json(filepath):
    '''Funkcija koja cita JSON datoteku'''
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    result = process_json('Baze podataka/importanje/pinovi2.json')
    print(result)