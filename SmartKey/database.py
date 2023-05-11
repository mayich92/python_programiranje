import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE users (
        ime TEXT,
        prezime TEXT,
        pin INTEGER,
        aktivan BOOLEAN
    )
''')

conn.commit()
conn.close()