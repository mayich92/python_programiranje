import tkinter as tk
from tkinter import messagebox
import json
import random

# Load the data from JSON files
with open('german_english.json', 'r', encoding='utf-8') as f:
    german_data = json.load(f)

with open('english_german.json', 'r', encoding='utf-8') as f:
    english_data = json.load(f)

def sample_dict(vocab, N):
    new_dict = {}
    src_words = list(vocab.keys())
    chosen_words = random.choices(src_words, k=N)
    for word in chosen_words:
        translation = vocab[word]
        new_dict[word.lower()] = translation.lower()
    return new_dict

def check_translation():
    selected_lang = lang_var.get()
    N = int(entry_words.get())

    if selected_lang == 'DE':
        words = sample_dict(german_data, N)
    elif selected_lang == 'EN':
        words = sample_dict(english_data, N)

    correct = 0

    for word, translation in words.items():
        input_translation = entry_translation.get().lower()

        if input_translation == translation:
            correct += 1
        else:
            messagebox.showinfo("Netočno", f"Netočno! Točan prijevod za riječ '{word}' je '{translation}'")

    percentage = round((correct / N) * 100, 2)
    messagebox.showinfo("Rezultat", f"Točnih odgovora: {correct}\nPostotak točnosti: {percentage}%")

# Create the main window
window = tk.Tk()
window.title("Prevoditelj DE->EN")

# Number of words section
label_words = tk.Label(window, text="Unesite broj riječi koliko želite vježbati:")
label_words.pack()
entry_words = tk.Entry(window)
entry_words.pack()

# Translation direction section
label_lang = tk.Label(window, text="Unesite izvorni jezik:")
label_lang.pack()
lang_var = tk.StringVar()
lang_var.set("DE")
radio_de = tk.Radiobutton(window, text="DE", variable=lang_var, value="DE")
radio_de.pack()
radio_en = tk.Radiobutton(window, text="EN", variable=lang_var, value="EN")
radio_en.pack()

# Word and translation entry section
label_word = tk.Label(window, text="Riječ:")
label_word.pack()
entry_translation = tk.Entry(window)
entry_translation.pack()

# Button to check the translation
button_check = tk.Button(window, text="Provjeri prijevod", command=check_translation)
button_check.pack()

# Start the main GUI loop
window.mainloop()
