import sqlite3
import os

os.chdir('Baze podataka')

query = 'SELECT sqlite_version();'

db_name = 'sqlite_python.db'

try:
    sqlite_connection = sqlite3.connect(db_name)

    cursor = sqlite_connection.cursor()

    cursor.execute(query)
    records = cursor.fetchall()

    print("Verzija naše SQLite instalacije je: ", records)
    cursor.close()

except sqlite3.Error as e:
    print("Dogodila se greška: ", e)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija uspješno zatvorena.")