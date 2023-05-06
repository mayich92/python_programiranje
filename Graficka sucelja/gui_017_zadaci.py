# Zadatak 33.
# GUI za telefonski imenik
# sučelje se sastoji od gumbova brojki i entry fielda
# iz JSON datoteke se treba loadati kontakte (key:value -> ime:broj)

import json
import tkinter as tk
from tkinter import messagebox

contacts_filepath = 'GUI/kontakti.json'

with open(contacts_filepath, 'r', encoding='utf-8') as f:
    contacts = json.load(f)

for name in contacts.keys():
    number = contacts[name]
    number = number.replace(' ', '')   # regex \s, funkcija re.sub()
    contacts[name] = number

root = tk.Tk()
root.title('Imenik')
base_font = ('Helvetica', 14)

number = tk.StringVar()

def add_to_entry(digit):
    current = number.get()
    new = current + digit
    number.set(new)

def delete_last():
    current = number.get()
    if current:
        new = current[:-1]
        number.set(new)

def process():
    entered_number = number.get()
    for name in contacts:
        if contacts[name] == entered_number:
            messagebox.showinfo(title='Pronađen kontakt', message='Kontakt: {}'.format(name))
            break
    else:
        messagebox.showwarning(title='Nije pronađen kontakt', message='U bazi ne postoji taj kontakt!')

number_entry = tk.Entry(root, textvariable=number, font=base_font)
number_entry.grid(row=0, columnspan=3, pady=(10, 20))

# button1 = tk.Button(root, text='1', command=lambda: add_to_entry('1'), font=base_font)
# button1.grid(row=1, column=0, ipadx=20)
# button2 = tk.Button(root, text='2', command=lambda: add_to_entry('2'), font=base_font)
# button2.grid(row=1, column=1, ipadx=20)
# button3 = tk.Button(root, text='3', command=lambda: add_to_entry('3'), font=base_font)
# button3.grid(row=1, column=2, ipadx=20)
# button4 = tk.Button(root, text='4', command=lambda: add_to_entry('4'), font=base_font)
# button4.grid(row=2, column=0, ipadx=20)
# button5 = tk.Button(root, text='5', command=lambda: add_to_entry('5'), font=base_font)
# button5.grid(row=2, column=1, ipadx=20)
# button6 = tk.Button(root, text='6', command=lambda: add_to_entry('6'), font=base_font)
# button6.grid(row=2, column=2, ipadx=20)
# button7 = tk.Button(root, text='7', command=lambda: add_to_entry('7'), font=base_font)
# button7.grid(row=3, column=0, ipadx=20)
# button8 = tk.Button(root, text='8', command=lambda: add_to_entry('8'), font=base_font)
# button8.grid(row=3, column=1, ipadx=20)
# button9 = tk.Button(root, text='9', command=lambda: add_to_entry('9'), font=base_font)
# button9.grid(row=3, column=2, ipadx=20)

# alternativno pozicioniranje tipki 1-9
for n in range(1, 10):
    button = tk.Button(root, text=str(n), command=lambda num=n: add_to_entry(str(num)), font=base_font)
    i = n-1
    row = i // 3
    column = i % 3
    button.grid(row=row+1, column=column, ipadx=20)

button0 = tk.Button(root, text='0', command=lambda: add_to_entry('0'), font=base_font)
button0.grid(row=4, column=1, ipadx=20)

erase_button = tk.Button(root, text='<-', command=delete_last, font=base_font)
erase_button.grid(row=4, column=2, ipadx=20)

start_button = tk.Button(root, text='Pokreni pretragu', font=base_font, command=process)
start_button.grid(row=5, columnspan=3)

exit_button = tk.Button(root, text='Izlaz', font=base_font, command=root.destroy)
exit_button.grid(row=6, columnspan=3)

root.mainloop()