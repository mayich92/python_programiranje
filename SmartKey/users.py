import sqlite3
import random

# lista s imenima, prezimenima i PIN-ovima
imena = ["Ana", "Ivan", "Petra", "Mario", "Luka"]
prezimena = ["Horvat", "Kovačević", "Marković", "Novak", "Babić"]
pini = [1234, 5678, 9012, 3456, 7890]

# povezivanje s bazom podataka
conn = sqlite3.connect('users.db')
c = conn.cursor()

# dodavanje 5 random korisnika u bazu
for i in range(5):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    pin = random.choice(pini)
    aktivan = random.choice([True, False])
    c.execute("INSERT INTO users (ime, prezime, pin, aktivan) VALUES (?, ?, ?, ?)", (ime, prezime, pin, aktivan))

# spremanje promjena i zatvaranje baze podataka
conn.commit()
conn.close()
