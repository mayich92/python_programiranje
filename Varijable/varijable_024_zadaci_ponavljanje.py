lista = [2, 4, 9]
lista.append('a')
lista.extend(['ca', 5.46])

# print(lista)
# print(*lista, sep='\n')

dct1 = {'a': 2, 'b': 5}
dct2 = {'c': 7, 'b': 6}

dct1.update(dct2)
# print(dct1)

dct3 = {**dct1, **dct2}
# print(dct3)



# # Zadatak 1
# print('Dobrodošli u brojač riječi!')
# text = input('Unesite tekst: ')
# words = text.split()
# # print(words)
# word_count = len(words)
# # word_count = text.count(' ') + 1
# print(f'Vaš tekst ima {word_count} riječi.')



# Zadatak 2
# a)

# CONVERSION = 2.54
# inches = float(input("Unesite broj inča: "))
# cm = inches * CONVERSION
# print(f"Unesena duljina je jednaka {cm} cm.")

# b)
# masa = float(input("Unesite masu (kg): "))
# visina = float(input("Unesite visinu (cm): "))
# visina /= 100
# BMI = masa / (visina ** 2)
# BMI = round(BMI, 2)

# print(f"Vaš BMI indeks je {BMI}.")


# Zadatak 3

# opisi = {
#     'py': 'Python source kod',
#     'docx': 'Microsoft Word dokument',
#     'pdf': 'Portable Document Format'
# }

# filename = input("Unesite ime datoteke: ")
# filename = filename.lower()
# parts = filename.split('.')
# extension = parts[-1]
# # extension = filename.split('.')[-1]
# description = opisi.get(extension, "nepoznat tip datoteke")
# print(f"Vaša datoteka ima ekstenziju .{extension} i to je {description}.")


# Dodatna vježba
from pprint import pprint

months = {
    'siječanj': {
        'redni_broj': 1,
        'dana_u_mjesecu': [31]
    },
    'veljača': {
        'redni_broj': 2,
        'dana_u_mjesecu': [28, 29]
    },
    'ožujak': {
        'redni_broj': 3,
        'dana_u_mjesecu': [31]
    }
}

broj_dana_u_veljaci = months['veljača']['dana_u_mjesecu']
broj_dana_u_veljaci = months.get('veljača').get('dana_u_mjesecu')
print(broj_dana_u_veljaci)

pprint(months)