import os

racuni = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
kreiranje_racuna()

def prikaz_stanja_racuna():
    print("Prikaz stanja računa")
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna in racuni:
        print("Trenutno stanje na računu: ", racuni[broj_racuna]["stanje"], racuni[broj_racuna]["valuta"])
    else:
        print("Račun ne postoji")
prikaz_stanja_racuna()

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
prikaz_prometa_po_racunu()

def polog_novca_na_racun():
    broj_racuna = input("Unesite broj računa: ")
    if broj_racuna in racuni:
        iznos = float(input("Unesite iznos za polog: "))
        valuta = input("Valuta (EUR ili HRK): ")
        print("Uspješno ste položili novce na Vaš račun!")

polog_novca_na_racun()

def podizanje_novaca_sa_racuna():
    dnevni_limit_u_kunama = 5000
    dnevni_limit_u_eurima = 655
    broj_racuna = input("Unesite broj računa:")
    iznos = float(input("Unesite iznos za isplatu: "))
    valuta = input("Valuta (EUR ili HRK): ")
    if broj_racuna in racuni and dnevni_limit_u_kunama <=5000 and dnevni_limit_u_eurima <=655 :
        print("Uspješno ste podignuli novce sa računa.")
    elif broj_racuna in racuni and dnevni_limit_u_kunama <=5000 and dnevni_limit_u_eurima <=655 :
        print("Premašili ste Vaš dnevni limit.")
podizanje_novaca_sa_racuna()







