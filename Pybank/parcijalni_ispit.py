import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

racuni = {}
def kreiranje_racuna():
    print("Kreiranje računa tvrtke")
    naziv = input("Naziv tvrtke:")
    ulica_i_broj = input("Ulica i poštanski broj:")
    postanski_broj = input("Poštanski broj:")
    grad = input("Grad:")
    oib = input("OIB:")
    while len(oib) !=11:
        print("Pogrešan broj znakova za OIB, pokušajte ponovno!")
        oib = input("OIB:")
    odgovorna_osoba = input("Unesite ime i prezime odgovorne osobe:")
    iznos = float(input("Unesite iznos po želji:"))
    valuta = input("Valuta: (HRK/EUR):").upper()
    while valuta not in ["HRK","EUR"]:
        print("Pogrešna valuta, pokušajte ponovno!")
        valuta = input("Valuta: (HRK/EUR):")
    godina, mjesec = input("Datum otvaranja računa (GGGG-MM): ").split("-")
    redni_broj = str(len(racuni)+1).zfill(5)
    broj_racuna = f"BA-{godina}-{mjesec}-{redni_broj}"
    racuni[broj_racuna] = {
        "naziv": naziv,
        "ulica_i_broj": ulica_i_broj,
        "postanski_broj": postanski_broj,
        "grad": grad,
        "oib": oib,
        "odgovorna_osoba": odgovorna_osoba,
        "stanje": iznos,
        "valuta": valuta,
        "promet": []
    }
    print(f"Račun uspješno kreiran.\nBroj računa: ", broj_racuna)

def prikazi_stanje_racuna():
    print("Prikaz stanja računa")
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna in racuni:
        print("Trenutno stanje na računu: ", racuni[broj_racuna]["stanje"], racuni[broj_racuna]["valuta"])
    else:
        print("Račun ne postoji.")

def prikaz_prometa_po_racunu():
    print("Prikaz prometa po računu")
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna in racuni:
        print("Promet po računu" , broj_racuna)
    for transakcija in racuni[broj_racuna]["promet"]:
        print(transakcija["datum"], "-", transakcija["opis"], "-", transakcija["iznos"],
    racuni[broj_racuna]["valuta"])
    else:
        print("Nema transakcija na ovom računu!")

def polog_novca_na_racun():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna in racuni:
        iznos = float(input("Unesite iznos za polog: "))
        valuta = input("Valuta (EUR ili HRK): ")
    print("Uspješno ste položili novce na Vaš račun!")

def podizanje_novca_sa_racuna():
    dnevni_limit_u_kunama = 5000
    dnevni_limit_u_eurima = 655
    broj_racuna = input("Unesite broj računa:")
    iznos = float(input("Unesite iznos za isplatu: "))
    valuta = input("Valuta (EUR ili HRK): ")
    if broj_racuna in racuni and dnevni_limit_u_kunama <=5000 or dnevni_limit_u_eurima <=655 :
        print("Uspješno ste podignuli novce sa računa.")
    else:
        print("Premašili ste Vaš dnevni limit.")


print("GLAVNI IZBORNIK")
print("1. Kreiranje racuna")
print("2. Prikaz stanja racuna")
print("3. Prikaz prometa po racunu")
print("4. Polog novca na racun")
print("5. Podizanje novca s racuna")
print("6. Izlaz")

opcija = input("Odaberite opciju: ")

if opcija == "1":
    kreiranje_racuna()

elif opcija == "2":
 prikazi_stanje_racuna()

elif opcija == "3":
    prikaz_prometa_po_racunu()

elif opcija == "4":
    polog_novca_na_racun()

elif opcija == "5":
    podizanje_novca_sa_racuna()

elif opcija == "6":
    print("Doviđenja!")

else:
    print("Nepoznata opcija")








