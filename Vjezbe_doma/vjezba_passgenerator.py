import random
import tkinter as tk


# Funkcija za generiranje lozinke
def generate_password():
    length = int(length_entry.get())
    complexity = int(complexity_entry.get())

    # ASCII kodovi za velika slova, mala slova i posebne znakove
    uppercase_letters = list(range(65, 91))
    lowercase_letters = list(range(97, 123))
    special_characters = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

    # Dodavanje znakova ovisno o kompleksnosti lozinke
    password_characters = []
    if complexity >= 1:
        password_characters += uppercase_letters
    if complexity >= 2:
        password_characters += lowercase_letters
    if complexity >= 3:
        password_characters += special_characters

    # Generiranje lozinke
    password = ''
    for i in range(length):
        password += chr(random.choice(password_characters))

    # Prikaz lozinke
    password_label.config(text=password)


# Stvaranje prozora
window = tk.Tk()
window.title('Generator Lozinke')

# Stvaranje i dodavanje elemenata na prozor
length_label = tk.Label(window, text='Dužina lozinke:')
length_entry = tk.Entry(window)
complexity_label = tk.Label(window, text='Kompleksnost lozinke:')
complexity_entry = tk.Entry(window)
password_label = tk.Label(window, text='')
generate_button = tk.Button(window, text='Generiraj lozinku', command=generate_password)

length_label.pack()
length_entry.pack()
complexity_label.pack()
complexity_entry.pack()
password_label.pack()
generate_button.pack()

# Pokretanje aplikacije
window.mainloop()
