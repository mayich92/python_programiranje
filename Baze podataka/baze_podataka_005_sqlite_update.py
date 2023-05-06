
import sqlite3
import os

os.chdir('Baze podataka')


db_name = 'tvrtke_db.db'

# query = '''
# UPDATE Employees
# SET email="bob@bobo.com"
# WHERE id=2
# '''

query = '''
UPDATE Employees
SET name="Charly"
WHERE name="Charlie"
'''

try:
    sqlite_connection = sqlite3.connect(db_name)
    cursor = sqlite_connection.cursor()
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as e:
    print("Dogodio se error: ", e)
finally:
    if sqlite_connection:
        sqlite_connection.close()