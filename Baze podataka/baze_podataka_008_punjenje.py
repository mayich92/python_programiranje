import hashlib
import sqlite3

import os

os.chdir('Baze podataka')

def hash_text(text):
    text = text.encode() 
    return hashlib.md5(text).hexdigest()

db_name = 'accounts_db.db'

query = '''
INSERT INTO Accounts (username, pass, name)
VALUES (?, ?, ?)
'''

query_create_table = '''
CREATE TABLE IF NOT EXISTS Accounts (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    pass TEXT,
    name TEXT
);
'''

users = [
    {'username': 'dmaric', 'pass': '12345678', 'name': 'Domagoj'},
    {'username': 'admin', 'pass': 'password', 'name': 'Administrator'}
]

accounts = []
for user in users:
    account = (user['username'], hash_text(user['pass']), user['name'])
    accounts.append(account)

try:
    sql_connection = sqlite3.connect(db_name)
    cursor = sql_connection.cursor()

    cursor.execute(query_create_table)
    sql_connection.commit()
    
    print("Tablica je uspješno kreirana!")
    for account in accounts:
        cursor.execute(query, account)
    sql_connection.commit()
    
    print("Accountovi uneseni!")
    cursor.close()
except sqlite3.Error as e:
    print('Error: ', e)
finally:
    if sql_connection:
        sql_connection.close()