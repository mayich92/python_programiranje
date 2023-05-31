# Napisati program koji pomoću rekurzivne funkcije ispisuje sve moguće potencijalne lozinke (Brute Force napad).
# Napredna verzija:
# Navedenu funkciju iskoristiti (uz modifikacije) kako bi se složio sustav koji ispituje jačinu korisnikove lozinke (koju korisnik unese kroz konzolu ili GUI). Jačinu lozinke označava vrijeme koje je potrebno da se ona probije brute force metodom.
# Napomene:
# uzmite da lozinke mogu sadržavati samo alfanumeričke znakove (engleska abeceda, lower+upper i znamenke)
# uzmite u obzir da jakost lozinke eksponencijalno raste povećavanjem njezine duljine - već kod duljine 6 čeka se oko 5 minuta
# Primjer rada:
# Dobrodošli u ispitivač jakosti lozinki!
# Unesite lozinku: abcd
# Vaša lozinka abcd probijena je u 0.08 sekundi
# Unesite lozinku: a1b2c
# Vaša lozinka a1b2c probijena je u 7.14 sekundi


import time

CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def brute_force(password, attempt=''):
    if attempt == password:
        return True
    if len(attempt) == len(password):
        return False

    for char in CHARSET:
        if brute_force(password, attempt + char):
            return True

    return False


def test_password_strength(password):
    start_time = time.time()
    result = brute_force(password)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)

    if result:
        print(f"Vaša lozinka {password} probijena je u {elapsed_time} sekundi")
    else:
        print("Neuspješno probijanje lozinke")


def main():
    print("Dobrodošli u ispitivač jakosti lozinki!")
    password = input("Unesite lozinku: ")
    test_password_strength(password)


if __name__ == '__main__':
    main()
