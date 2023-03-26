# Napravite aplikaciju za konverziju (u oba smjera):
# km u milju
# C u F
# kg u funtu
# litru u galon
# kW u ks

mj = ['km', 'milja', 'c', 'f', 'kg', 'funta', 'litra', 'galon', 'kw', 'ks']

print("Dobrodošli u pretvarač mjernih jedinica!")
print("Raspoložive mjerne jedinice su: ")
print(*mj, sep='\t')
while True:
    unos = input('Unesite brojčanu vrijednost: ')
    unos = float(unos)
    mjerna_jedinica = input('Unesite mjernu jedinicu Vaše vrijednosti: ').lower()
    rezultat = None
    if mjerna_jedinica == 'milja':
        rezultat = unos / 0.6214
    elif mjerna_jedinica == 'km':
        rezultat = 0.6214 * unos
    elif mjerna_jedinica == 'c':
        rezultat = (9 / 5) * unos + 32
    elif mjerna_jedinica == 'f':
        rezultat = (unos - 32) * (5 / 9)
    elif mjerna_jedinica == 'kg':
        rezultat = unos * 2.2046
    elif mjerna_jedinica == 'funta':
        rezultat = unos / 2.2046
    else:  # mjerna jedinica not in mj
        print("Unijeli ste nepodržanu mjernu jedinicu!")
        continue

    rezultat = round(rezultat, 2)
    print(f"Rezultat je {rezultat}.")
    izlaz = input('Želite li unijeti još vrijednosti (DA/NE)? ')
    if izlaz.lower() == 'ne':
        break