# Zadatak 31
# igra kamen-papir-škare u obliku GUI
# v
# opcija b: tri radiobutton tipke
# label čuva rezultat

import tkinter as tk
import random

class GUI:
    def __init__(self):
        self.user_score = 0
        self.bot_score = 0
        self.options = ['kamen', 'škare', 'papir']
        self.base_font = ('Helvetica', 14)

        self.master = tk.Tk()
        self.master.title('Kamen papir škare')

        self.var = tk.StringVar()
        self.var.set(None)

        self.result = tk.StringVar()
        self.result.set('Niste još odigrali!')

        self.score = tk.StringVar()
        self.score.set('Rezultat je 0:0')

        b1 = tk.Radiobutton(self.master, text='Kamen', command=self.process, 
            font=self.base_font, variable=self.var, value='kamen')
        b1.pack()

        b2 = tk.Radiobutton(self.master, text='Škare', command=self.process, 
            font=self.base_font, variable=self.var, value='škare')
        b2.pack()

        b3 = tk.Radiobutton(self.master, text='Papir', command=self.process, 
            font=self.base_font, variable=self.var, value='papir')
        b3.pack()

        label_result = tk.Label(self.master, textvariable=self.result, font=self.base_font)
        label_result.pack()

        label_score = tk.Label(self.master, textvariable=self.score, font=self.base_font)
        label_score.pack()

        exit_button = tk.Button(self.master, text='Izlaz', 
            command=self.master.destroy, font=self.base_font)
        exit_button.pack()

    def bot_win(self):
        self.result.set('Računalo je pobijedilo!')
        self.bot_score += 1

    def user_win(self):
        self.result.set('Korisnik je pobijedilo!')
        self.user_score += 1

    def process(self):
        choice = self.var.get()
        bot_choice = random.choice(self.options)
        if choice == bot_choice:
            self.result.set('Neriješeno!')
        elif choice == 'škare':
            if bot_choice == 'kamen':
                self.bot_win()
            else:
                self.user_win()
        elif choice == 'kamen':
            if bot_choice == 'papir':
                self.bot_win()
            else:
                self.user_win()
        elif choice == 'papir':
            if bot_choice == 'škare':
                self.bot_win()
            else:
                self.user_win()
        else:
            raise ValueError('Nepoznata vrijednost odabira!')
        self.score.set(f'Rezultat je {self.user_score}:{self.bot_score}')



gui = GUI()
gui.master.mainloop()

# gui2 = GUI()
# gui2.master.mainloop()
