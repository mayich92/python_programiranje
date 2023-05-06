import sqlite3
import os

os.chdir('Baze podataka')

query = '''
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''

db_name = 'tvrtke_db.db'

try:
    sqlite_connection = sqlite3.connect(db_name)

    cursor = sqlite_connection.cursor()

    cursor.execute(query)
    sqlite_connection.commit()
    
    print("Tablica je uspješno kreirana!")

    cursor.close()

except sqlite3.Error as e:
    print("Dogodila se greška: ", e)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija uspješno zatvorena.")