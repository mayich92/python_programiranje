import sqlite3

db_name = 'Baze podataka/accounts_db.db'
query = 'SELECT * FROM Accounts'

try:
    sql_connection = sqlite3.connect(db_name)
    cursor = sql_connection.cursor()

    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
    
    cursor.close()
except sqlite3.Error as e:
    print('Error: ', e)
finally:
    if sql_connection:
        sql_connection.close()