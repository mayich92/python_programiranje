from datetime import datetime

PDV = 25


def obracun_pdv(ukupno, stopa):
    # print('Obračun PDV funkcija')
    koeficijent = (stopa / 100) + 1
    osnovica = ukupno / koeficijent
    iznos_pdv = ukupno - osnovica
    osnovica, iznos_pdv = round(osnovica, 2), round(iznos_pdv, 2)
    return osnovica, iznos_pdv


class Racun:
    '''Klasa za upravljanje racunima'''

    prinos_blagajne = 0
    br_racuna = 1

    def __init__(self, datum, stavke, pdv):
        self.datum = datum
        self.broj_racuna = self.generiraj_broj_racuna()
        Racun.br_racuna += 1
        self.stavke = stavke

        self.pdv = pdv
        self.ukupno = 0

    def generiraj_broj_racuna(self):
        redni = str(Racun.br_racuna).zfill(5)
        dt = self.datum
        return dt + '-' + redni

    # def obracun_pdv(self, ukupno):
    #     print('Obračun PDV metoda')
    #     koeficijent = (self.pdv/100) + 1
    #     osnovica = ukupno/koeficijent
    #     iznos_pdv = ukupno - osnovica
    #     return osnovica, iznos_pdv

    def dodaj_stavku(self, st):
        self.stavke.append(st)
        self.ukupno += st.cijena
        Racun.prinos_blagajne += st.cijena

    def ispis_racuna(self):
        print('-' * 60)
        print(f'ISPIS RAČUNA: ({self.broj_racuna})')
        print('-' * 60)
        for i, stavka in enumerate(self.stavke):
            redni_broj = str(i + 1).zfill(3)
            osnovica, iznos_pdv = obracun_pdv(stavka.cijena, self.pdv)
            ime = stavka.ime
            while len(ime) < 20:
                ime = ' ' + ime
            print(f"{redni_broj}.\t{ime}\t{osnovica}\t{iznos_pdv}\t{stavka.cijena} EUR")
        print('-' * 60)
        print(f"Ukupan iznos računa: {self.ukupno} EUR")
        print('-' * 60)


class Stavka:
    def __init__(self, ime, cijena):
        self.ime = ime
        self.cijena = cijena


# izračun PDV-a -> osnovica, pdv, ukupno?
# metoda za "lijepi" ispis stavki računa
# glavni program, konzolni alat -> unos stavki i računa (nije bitno za danas)

# r1 = Racun('18.4.', [], '25')
# s1 = Stavka('kruh', 10)
# r1.dodaj_stavku(s1)
# r2 = Racun('18.4.', [], '25')
# s2 = Stavka('jogurt', 12)
# r2.dodaj_stavku(s2)

# print(r1.broj_racuna, r1.ukupno)
# print(r2.broj_racuna, r2.ukupno)
# print(Racun.prinos_blagajne)

def novi_racun():
    trenutno = datetime.now()
    datum = trenutno.strftime('%d%m%y')
    r = Racun(datum, [], PDV)
    while True:

        ime = input("Unesite ime stavke: ")
        if not ime:
            print('Ime ne smije biti prazno! ')
            continue
        cijena = input("Unesite cijenu stavke: ")
        try:
            cijena = float(cijena)
        except ValueError:
            print('Cijena nije pravilna!')
            continue
        s = Stavka(ime, cijena)
        r.dodaj_stavku(s)
        end = input('Želite li unijeti još stavki? '.upper()).lower()
        if end == 'ne':
            break
    r.ispis_racuna()


def blagajna():
    print("Dobrodošli u program Blagajna!")
    while True:
        print("Kreiram novi račun....")
        novi_racun()

        end = input('Želite li izdati još računa? '.upper()).lower()
        if end == 'ne':
            break
    print("Hvala na korištenju programa Blagajna! ")


blagajna()