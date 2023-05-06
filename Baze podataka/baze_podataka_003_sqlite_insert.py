import sqlite3
import os

os.chdir('Baze podataka')

lista_djelatnika = [
    ('Alice', 'alice@algebra.hr'),
    ('Bob', 'bob@algebra.hr'),
    ('Charlie', 'charlie@algebra.hr')    # probajte upisati pod mail bob@algebra.hr -> NOT UNIQUE
]

lista_djelatnika = [
    ('Domagoj', 'domagoj@algebra.hr')
]


query = '''
INSERT INTO Employees (name, email)
VALUES (?, ?)
'''

db_name = 'tvrtke_db.db'

try:
    sqlite_connection = sqlite3.connect(db_name)

    cursor = sqlite_connection.cursor()

    for djelatnik in lista_djelatnika:
        cursor.execute(query, djelatnik)    # (4,)    # tuple s jednom vrijednošću

    sqlite_connection.commit()
    
    print("Tablica je popunjena!")

    cursor.close()

except sqlite3.Error as e:
    print("Dogodila se greška: ", e)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija uspješno zatvorena.")