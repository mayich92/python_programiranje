import sqlite3
import os

conn = sqlite3.connect('plants.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                photo BLOB,
                humidity_soil TEXT,
                light TEXT,
                temperature TEXT,
                supstrat TEXT
            )''')
# Function to convert image to binary data
def convert_image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        blob_data = file.read()
    return blob_data

# Ubacivanje biljaka u bazu podataka
plants = [
    (1, 'Tulipan', convert_image_to_binary(os.path.join('images','tulipan.jpg')), 'Tjedno', 'Tamnija', 'Toplija', 'Dodajte supstrat A'),
    (2, 'Ruža', convert_image_to_binary(os.path.join('images','ruza.jpg')), 'Dnevno', 'Svjetlija', 'Hladnija', 'Dodajte supstrat B'),
    (3, 'Orhideja',convert_image_to_binary(os.path.join('images', 'orhideja.jpg')), 'Mjesečno', 'Tamnija', 'Toplija', 'Dodajte supstrat C'),
    (4, 'Božur', convert_image_to_binary(os.path.join('images','bozur.jpg')), 'Tjedno', 'Svjetlija', 'Toplija', 'Dodajte supstrat D'),
    (5, 'Zumbul',convert_image_to_binary(os.path.join('images', 'zumbul.jpg')), 'Dnevno', 'Tamnija', 'Hladnija', 'Dodajte supstrat E'),
    (6, 'Jaglac', convert_image_to_binary(os.path.join('images','jaglac.jpg')), 'Mjesečno', 'Svjetlija', 'Hladnija', 'Dodajte supstrat F'),
    (7, 'Kaktus', convert_image_to_binary(os.path.join('images','kaktus.jpg')), 'Tjedno', 'Tamnija', 'Toplija', 'Dodajte supstrat G'),
    (8, 'Tratinčica',convert_image_to_binary(os.path.join('images', 'tratincica.jpg')), 'Dnevno', 'Svjetlija', 'Toplija', 'Dodajte supstrat H'),
    (9, 'Maslačak', convert_image_to_binary(os.path.join('images','maslacak.jpg')), 'Mjesečno', 'Tamnija', 'Hladnija', 'Dodajte supstrat I'),
    (10, 'Ciklama', convert_image_to_binary(os.path.join('images','ciklama.jpg')), 'Tjedno', 'Svjetlija', 'Hladnija', 'Dodajte supstrat J')
]

c.executemany('INSERT INTO plants VALUES (?, ?, ?, ?, ?, ?, ?)', plants)

# Potvrda promjena i zatvaranje veze s bazom podataka
conn.commit()
conn.close()