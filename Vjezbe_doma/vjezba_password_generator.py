import random
import string
def password_generator():

    print("Dobrodošli u password generator!")

    lozinka = random.choices(string.ascii_letters + string.digits + string.punctuation, k=duljina_lozinke)
    nova_lozinka = "".join(lozinka)
    print(f"Vaša generirana lozinka je {nova_lozinka}.")

while True:
    duljina_lozinke = int(input("Koliku duljinu lozinke želite? (Unesite 0 za kraj programa.)"))
    if duljina_lozinke != 0:
        password_generator()
        print("-" * 100)
    else:
        print(f"Hvala na korištenju password generatora!")
        break








