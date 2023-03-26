# maskiranje kreditne kartice - sve osim zadnje 4 znamenke
# primjer: 5214 7852 3691 1234 - #### #### #### 1234
# broj_kk = "5214-785-23691-4567"

N = 4


def maskiraj(broj_kk, znak):
    broj_kk = list(broj_kk)
    jesu_li_znamenke = [i.isdigit() for i in broj_kk]
    broj_znamenki = jesu_li_znamenke.count(True)

    broj_maskiranih = 0
    for i in range(len(broj_kk)):
        broj = broj_kk[i]
        if broj.isdigit():
            broj_kk[i] = znak
            broj_maskiranih += 1
        if broj_maskiranih >= broj_znamenki - N:
            break

    novi_broj_kk = ''.join(broj_kk)

    return novi_broj_kk


def program():
    while True:
        print("Dobrodošli u program za maskiranje brojeva kreditne kartice! ")
        broj = input("Unesite broj kreditne kartice (unesite prazan string za kraj): ")
        if not broj:
            print("Hvala Vam na korištenju programa za maskiranje brojeva kreditne kartice!")
            break
        znak = input("Unesite znak kojim želite maskirati brojke (unesite prazan string za default - # ): ")
        if not znak:
            znak = '#'
        novi = maskiraj(broj, znak)
        print(f"Vaš novi maskirani broj je {novi}")


program()