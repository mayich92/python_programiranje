# Zadatak 31
# igra kamen-papir-škare u obliku GUI
# opcija a: tri obične tipke
# opcija b: tri radiobutton tipke - TODO
# label čuva rezultat

import tkinter as tk
import random

user_score = 0
bot_score = 0
options = ['kamen', 'škare', 'papir']
base_font = ('Helvetica', 14)

root = tk.Tk()
result = tk.StringVar()
result.set('Niste još odigrali!')
score = tk.StringVar()
score.set('Rezultat je 0:0')
root.title('Kamen papir škare')

def bot_win():
    result.set('Računalo je pobijedilo!')
    global bot_score
    bot_score += 1

def user_win():
    result.set('Korisnik je pobijedilo!')
    global user_score
    user_score += 1

def process(choice):
    
    bot_choice = random.choice(options)
    if choice == bot_choice:
        result.set('Neriješeno!')
    elif choice == 'škare':
        if bot_choice == 'kamen':
            bot_win()
        else:
            user_win()
    elif choice == 'kamen':
        if bot_choice == 'papir':
            bot_win()
        else:
            user_win()
    elif choice == 'papir':
        if bot_choice == 'škare':
            bot_win()
        else:
            user_win()
    else:
        raise ValueError('Nepoznata vrijednost odabira!')
    score.set(f'Rezultat je {user_score}:{bot_score}')

# alternativno koristiti po jednu funkciju za svaki button
# def process_kamen():
#     process('kamen')

b1 = tk.Button(root, text='Kamen', command=lambda: process('kamen'), font=base_font)
b1.pack()

b2 = tk.Button(root, text='Škare', command=lambda: process('škare'), font=base_font)
b2.pack()

b3 = tk.Button(root, text='Papir', command=lambda: process('papir'), font=base_font)
b3.pack()

label_result = tk.Label(root, textvariable=result, font=base_font)
label_result.pack()

label_score = tk.Label(root, textvariable=score, font=base_font)
label_score.pack()

exit_button = tk.Button(root, text='Izlaz', command=root.destroy, font=base_font)
exit_button.pack()

root.mainloop()