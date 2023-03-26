# Zadatak 15.
# Napraviti igru Hangman/Vješalo. Računalo generira nasumično neku riječ iz svoje baze (definirajte listu s nekoliko riječi),
# koju korisnik treba pogoditi slovo po slovo, a za to ima 6 pokušaja.
# Riječ se korisniku prikazuje maskirano, svako slovo je donja crta,
# a kod pogotka slova sve pojave tog slova se pojavljuju na svom mjestu u prikazu riječi. U slučaju pogrešnog odabira smanjuje se broj preostalih pokušaja.

# Napomene:
# korisniku se u svakom potezu trebaju pokazati slova koja je već unio, a ako unese ponovno neko od tih slova,
# to mu se ne treba brojati kao pokušaj i treba mu se ispisati odgovarajuća poruka
# dva su različita ishoda igre te svaki ishod treba imati odgovarajuću poruku korisniku
# 1. korisniku je ponestalo pokušaja
# 2. korisnik je pogodio riječ (nema više donjih crta u riječ, sva slova su prikazana)



import random

print("Dobrodošli u igru Hangman!")
lista_rijeci = ["stol", "kuća", "auto", "pas", "subota", "putovanje", "radijator"]
# nasumicni_izbor = random.choice(lista_rijeci)
nasumicni_izbor = "radijator"
broj_pokusaja = 6
maskirni_izbor = len(nasumicni_izbor) * "_"
lista_unesenih_slova = []

while broj_pokusaja > 0:
    print(f"Riječ: {maskirni_izbor}")
    print(f"Preostalih pokušaja: {broj_pokusaja}")
    uneseno_slovo = input("Unesite slovo po izboru: ")
    lista_unesenih_slova.append(uneseno_slovo)
    nova_lista = " ".join(lista_unesenih_slova)
    print(f"Iskorištena slova: {nova_lista}")
    ponavljanje_istog_slova_u_rijeci = nasumicni_izbor.count(uneseno_slovo)
    index_slova = nasumicni_izbor.index(uneseno_slovo)
    print(index_slova)


    if uneseno_slovo in nasumicni_izbor:
        # maskirni_izbor.replace( "_" , uneseno_slovo)
        print(f"To slovo se pojavljuje u riječi {ponavljanje_istog_slova_u_rijeci} puta.")
        for slovo in nasumicni_izbor:
            index_slova = nasumicni_izbor.index(uneseno_slovo)
            # maskirni_izbor[index_slova]=uneseno_slovo
            print(index_slova)
    else:
        print("To slovo se ne pojavljuje u riječi.")
        broj_pokusaja -= 1






