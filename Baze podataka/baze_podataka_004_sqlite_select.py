import sqlite3
import os

os.chdir('Baze podataka')



query_select_all = '''
SELECT * FROM Employees
'''

modified_query = '''
SELECT id, email
FROM Employees 
WHERE name="Alice"
'''

db_name = 'tvrtke_db.db'

try:
    sqlite_connection = sqlite3.connect(db_name)

    cursor = sqlite_connection.cursor()

    cursor.execute(query_select_all)

    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()

except sqlite3.Error as e:
    print("Dogodila se greška: ", e)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("SQLite konekcija uspješno zatvorena.")