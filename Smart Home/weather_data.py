import sqlite3
from datetime import datetime

def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect("/home/maja/Desktop/weather_data.db")
    c = conn.cursor()

    # Create the weather_data table
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sensor_type TEXT,
            value REAL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

create_database()
