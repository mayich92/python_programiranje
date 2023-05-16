# Zadatak 36.
# Cezarova šifra - supstitucija
# 1x entry za tekst
# 1x entry za pomak
# 1x radio za smjer
# messagebox za ispis šifriranog
# start button i exit button
import tkinter as tk
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift, direction):
    new_text = ''
    for c in text:
        if c not in alphabet:
            new_text += c
            continue
        index_original = alphabet.index(c)
        new_index = index_original - shift if direction == 'left' else index_original + shift
        new_index = new_index % len(alphabet)
        new_letter = alphabet[new_index]
        new_text += new_letter
    return new_text

# def invert_caesar(text, shift, direction):
#     new_text = ''
#     for c in text:
#         index_original = alphabet.index(c)
#         new_index = index_original - shift if direction == 'right' else index_original + shift
#         new_index = new_index % len(alphabet)
#         new_letter = alphabet[new_index]
#         new_text += new_letter
#     return new_text

def process():
    t, s, d = text.get(), shift.get(), direction.get()
    s = int(s)
    r = caesar(t, s, d)
    result.set(r)

root = tk.Tk()
root.title('Cezarova šifra')

text = tk.StringVar()
shift = tk.StringVar()
direction = tk.StringVar()
result = tk.StringVar()
result.set('Niste unijeli parametre!')

base_font = ('Helvetica', 16)

text_label = tk.Label(root, text='Tekst: ', font=base_font)
text_label.grid(row=0, column=0, pady=10, padx=10)

text_entry = tk.Entry(root, textvariable=text, font=base_font)
text_entry.grid(row=0, column=1, pady=10, padx=10)
shift_label = tk.Label(root, text='Pomak: ', font=base_font)
shift_label.grid(row=1, column=0, pady=10, padx=10)

shift_entry = tk.Entry(root, textvariable=shift, font=base_font)
shift_entry.grid(row=1, column=1, pady=10, padx=10)

direction_label = tk.Label(root, text='Smjer: ', font=base_font)
direction_label.grid(row=2, column=0, pady=10, padx=10)

direction_entry = tk.Entry(root, textvariable=direction, font=base_font)
direction_entry.grid(row=2, column=1, pady=10, padx=10)

result_label = tk.Label(root, textvariable=result, font=base_font)
result_label.grid(row=3, columnspan=2, pady=10)

start_button = tk.Button(root, text='Šifriraj', font=base_font, command=process)
start_button.grid(row=4, columnspan=2, pady=10)

exit_button = tk.Button(root, text='Izlaz', font=base_font, command=root.destroy)
exit_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()