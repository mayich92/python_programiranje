class Racun:
    '''Klasa za upravljanje racunima'''

    prinos_blagajne = 0
    br_racuna = 1

    def __init__(self, datum, stavke, pdv):
        self.broj_racuna = Racun.br_racuna
        Racun.br_racuna += 1
        self.datum = datum
        self.stavke = stavke
        self.pdv = pdv
        self.ukupno = 0

    def dodaj_stavku(self, st):
        self.stavke.append(st)
        self.ukupno += st.cijena
        Racun.prinos_blagajne += st.cijena


class Stavka:
    def __init__(self, ime, cijena):
        self.ime = ime
        self.cijena = cijena


# izračun PDV-a -> osnovica, pdv, ukupno?
# metoda za "lijepi" ispis stavki računa
# glavni program, konzolni alat -> unos stavki i računa (nije bitno za danas)

r1 = Racun('18.4.', [], '25')
s1 = Stavka('kruh', 10)
r1.dodaj_stavku(s1)
r2 = Racun('18.4.', [], '25')
s2 = Stavka('jogurt', 12)
r2.dodaj_stavku(s2)

print(r1.broj_racuna, r1.ukupno)
print(r2.broj_racuna, r2.ukupno)
print(Racun.prinos_blagajne)


def novi_racun():
    r = Racun()
    # ...
    while True:
        # dodavanje stavki
        s = Stavka()
        r.append(s)
        break


def blagajna():
    while True:
        print("Kreiram novi račun....")
        novi_racun()
        # dok korisnik želi unositi račune
        break