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
    valuta = input("Valuta: (HRK/EUR):")
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
        "valuta": valuta
    }
    print("Račun uspješno kreiran.\nBroj računa: ", broj_racuna)

