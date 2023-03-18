glazbena_abeceda = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]
glazbena_abeceda.extend(glazbena_abeceda)
početni_ton = input("Unesi početni ton:").upper()

pozicija = glazbena_abeceda.index(početni_ton)

indeks_drugog_tona = pozicija + 4
indeks_treceg_tona = pozicija + 7
indeks_drugog_tona_mol = pozicija + 3
indeks_treceg_tona_mol = pozicija + 7

print(f'Durski akord je {glazbena_abeceda[pozicija]}, {glazbena_abeceda[indeks_drugog_tona]}, {glazbena_abeceda[indeks_treceg_tona]}')
print(f'Molski akord je {glazbena_abeceda[pozicija]}, {glazbena_abeceda[indeks_drugog_tona_mol]}, {glazbena_abeceda[indeks_treceg_tona_mol]}')
