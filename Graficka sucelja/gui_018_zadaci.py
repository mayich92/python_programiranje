# Zadatak 34.
# Napraviti GUI koji korisniku daje nasumični citat (quotes.toscrape.com) od odabranog autora
# Autore ponuditi u dropdown menu

import os
import requests
from bs4 import BeautifulSoup
import time
import json
import tkinter as tk
from tkinter import messagebox
import random

def fill_base(filepath):
    url_template = "https://quotes.toscrape.com/page/"
    DELAY = 2
    page_to_end_on = 10
    quotes_base = []
    page = 1
    while page <= page_to_end_on:
        url = url_template + str(page)
        print('Currently scraping: ', url)
        time.sleep(DELAY)
        r = requests.get(url)
        data = r.text

        soup = BeautifulSoup(data, "html.parser")
        quotes = soup.find_all('div', class_='quote')    
        if not quotes:
            break
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            t = (text, author)
            quotes_base.append(t)
        
        page += 1

    author_quote = {}
    for quote in quotes_base:
        text, author = quote
        if author not in author_quote.keys():
            author_quote[author] = [text]
        else:
            author_quote[author].append(text)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(author_quote, f, indent=4)
    

# fill_base("GUI/quotes.json")
quotes_file = "GUI/quotes.json"
if not os.path.exists(quotes_file):
    fill_base(quotes_file)

with open(quotes_file, 'r', encoding='utf-8') as f:
    quotes_base = json.load(f)

root = tk.Tk()
root.title('Quotes generator')

var = tk.StringVar()
var.set('nedefinirano')

def generate():
    chosen_author = var.get()
    quotes = quotes_base[chosen_author]
    generated_quote = random.choice(quotes)
    messagebox.showinfo(title='Citat', message=generated_quote)

base_font = ('Helvetica', 16)

author_label = tk.Label(root, text='Autor: ', font=base_font)
author_label.grid(row=0, column=0, padx=(10,20))

options = list(quotes_base.keys())

author_option = tk.OptionMenu(root, var, *options)
author_option.grid(row=0, column=1)


start_button = tk.Button(root, text='Daj citat', font=base_font, command=generate)
start_button.grid(row=1, columnspan=2, pady=30)

exit_button = tk.Button(root, text='Izlaz', font=base_font, command=root.destroy)
exit_button.grid(row=2, columnspan=2)

root.mainloop()