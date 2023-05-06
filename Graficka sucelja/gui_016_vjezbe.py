import random
import string
import tkinter as tk

# 1x Label duljina lozinke?
# 1x Entry duljina lozinke
# 1x Label opcije:
# 4x Checkbox
# 1x Button pokreni
# 1x Label za rezultat
# 1x Button za izlaz

base_font = ('Helvetica', 14)
mala_slova = string.ascii_lowercase
velika_slova = string.ascii_uppercase
brojke = string.digits
simboli = string.punctuation

def generate():
    characters = ''
    pl = int(pass_length.get())
    if use_lower.get():
        characters += mala_slova
    if use_upper.get():
        characters += velika_slova
    if use_digits.get():
        characters += brojke
    if use_symbols.get():
        characters += simboli
    if characters:
        list_password = random.choices(characters, k=pl)
        string_password = ''.join(list_password)
        result.set('Vaša lozinka je: {}'.format(string_password))


# checkbox = tk.Checkbutton(root, text='Zaokruži rezultat na cijeli broj?', variable=round_bool)
# checkbox.grid(row=2, columnspan=2)

root = tk.Tk()
root.title('Password generator')
pass_length = tk.StringVar()
use_lower = tk.BooleanVar()
use_lower.set(True)
use_upper = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

length_label = tk.Label(root, text='Unesite duljinu lozinke:', font=base_font)
length_label.grid(row=0, column=0, padx=(10,20))

length_entry = tk.Entry(root, textvariable=pass_length, font=base_font)
length_entry.grid(row=0, column=1, padx=(20,10))

options_label = tk.Label(root, text='Opcije:', font=base_font)
options_label.grid(row=1, columnspan=2)

c1 = tk.Checkbutton(root, text='Koristiti mala slova?', variable=use_lower, font=base_font)
c1.grid(row=2, columnspan=2)

c2 = tk.Checkbutton(root, text='Koristiti velika slova?', variable=use_upper, font=base_font)
c2.grid(row=3, columnspan=2)

c3 = tk.Checkbutton(root, text='Koristiti znamenke?', variable=use_digits, font=base_font)
c3.grid(row=4, columnspan=2)

c4 = tk.Checkbutton(root, text='Koristiti simbole?', variable=use_symbols, font=base_font)
c4.grid(row=5, columnspan=2)

start_button = tk.Button(root, text='Generiraj', font=base_font, command=generate)
start_button.grid(row=6, columnspan=2)

result = tk.StringVar()
result.set('Niste generirali lozinku!')

result_label = tk.Label(root, textvariable=result, font=base_font)
result_label.grid(row=7, columnspan=2)

exit_button = tk.Button(root, text='Izlaz', command=root.destroy, font=base_font)
exit_button.grid(row=8, columnspan=2)

root.mainloop()