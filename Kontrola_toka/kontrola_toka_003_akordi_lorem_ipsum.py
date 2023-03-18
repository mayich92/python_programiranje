# kromatska_skala = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]    # nastavlja se ciklički
# kromatska_skala.extend(kromatska_skala)

# '''
# kromatska_skala = kromatska_skala * 2    # alternativa za .extend() sa samim sobom
# print("Dostupni tonovi su: {}".format(kromatska_skala))
# '''

# # durski akord: 0,4,7
# # molski akord: 0,3,7

# # algoritam:
# # korisnik unese početni ton
# # ispis: Durski akord čine note: ...
# # ispis: Molski akord čine note: ...


# pocetni = input("Unesite željeni početni ton: ")
# blokirati_program = False
# if not pocetni[0].isalpha():
#     print('Unos je nevaljan!')
#     blokirati_program = True
# elif pocetni[0].islower():
#     tip_akorda = 'mol'
# else:
#     tip_akorda = 'dur'

# if not blokirati_program:
#     pocetni = pocetni.upper()
#     indeks_pocetnog = kromatska_skala.index(pocetni)
#     print(indeks_pocetnog)
#     indeks_drugog_tona_dur = indeks_pocetnog+4
#     indeks_drugog_tona_mol = indeks_pocetnog+3
#     indeks_treceg_tona = indeks_pocetnog+7
#     drugi_ton_dur = kromatska_skala[indeks_drugog_tona_dur]
#     drugi_ton_mol = kromatska_skala[indeks_drugog_tona_mol]
#     treci_ton = kromatska_skala[indeks_treceg_tona]

#     if tip_akorda == 'mol':
#         print(f'Molski akord čine note {pocetni}, {drugi_ton_mol} i {treci_ton}')
#     else:
#         print(f'Durski akord čine note {pocetni}, {drugi_ton_dur} i {treci_ton}')


lorem_ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Fusce at consequat libero. Pellentesque vitae laoreet urna, 
nec aliquet augue. Morbi aliquet felis nulla, non pharetra metus feugiat non. 
Mauris sed eleifend nunc. Duis sed semper ante. 
Integer ac molestie elit, a volutpat nibh. 
Phasellus sagittis non sem et semper. 
Suspendisse tempor faucibus sagittis. 
Morbi blandit dictum auctor. 
Aenean faucibus at lorem et tincidunt.
'''

lorem_ipsum = lorem_ipsum.lower()
lorem_ipsum_words = lorem_ipsum.split()

lorem_ipsum_words = [word.strip('?.,!') for word in lorem_ipsum_words]

input_word = input("Unesite riječ: ")
# word_occ = lorem_ipsum_words.count(input_word)

word_occ = 0
for word in lorem_ipsum_words:
    print(word)
    if word == input_word:
        word_occ += 1
print(f'Vaša riječ se pojavljuje {word_occ} puta.')
