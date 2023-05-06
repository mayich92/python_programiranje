import sqlite3
import os
os.chdir('Baze podataka')

db_name = 'tvrtke_db.db'
query = '''
DELETE FROM Employees
WHERE id=2
'''

query_delete_all = '''
DELETE FROM Employees
'''

try:
    sqlite_connection = sqlite3.connect(db_name)
    cursor = sqlite_connection.cursor()
    cursor.execute(query)
    sqlite_connection.commit()
    cursor.close()
except sqlite3.Error as e:
    print("Error: ", e)
finally:
    if sqlite_connection:
        sqlite_connection.close()