import sqlite3
import os

os.chdir('Baze podataka')
db_name = 'osobe.db'

create_table_query = '''
CREATE TABLE IF NOT EXISTS People (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age int,
    street VARCHAR(150)
);
'''

people = [
    ('Alice', 20, 'Street 1'),
    ('Bob', 30, 'Street 2'),
    ('Charlie', 40, 'Street 3')
]

insert_query = '''
INSERT INTO People (name, age, street)
VALUES (?, ?, ?)
'''

select_query = '''
SELECT * FROM People
'''

strict_select_query = '''
SELECT *
FROM People
WHERE name="Alice"
'''

delete_query = '''
DELETE FROM People
WHERE id >= 4 AND id <= 6
'''

update_query = '''
UPDATE People
SET age=21
WHERE name="Alice"
'''

try:
    sql_conn = sqlite3.connect(db_name)
    cursor = sql_conn.cursor()
    cursor.execute(select_query)
    # for person in people:
    #     cursor.execute(insert_query, person)
    # sql_conn.commit()
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
except sqlite3.Error as e:
    print(e)
finally:
    if sql_conn:
        sql_conn.close()