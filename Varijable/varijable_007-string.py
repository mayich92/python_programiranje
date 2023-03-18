'''
ime = "Petar \"Pero\""
prezime = "Perić"
puno_ime = ime + " " + prezime
print(puno_ime)
'''


ime = "Petar"
prezime = "Perić"
ispis1 = "Vaše ime je: {} {}".format(ime, prezime)
ispis2 = f"Vaše ime je: {ime} {prezime}"
ispis3 = "Vaše ime je: %s %s" % (ime, prezime)
print(ispis1)
print(ispis2)
print(ispis3)