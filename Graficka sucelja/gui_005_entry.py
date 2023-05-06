
from tabnanny import check
import tkinter as tk
from math import sqrt

result_font = ("Helvetica", 14, "bold")



def klik():
    input_value = e.get()
    input_value = float(input_value)
    sqrt_value = sqrt(input_value)
    if round_bool.get():
        sqrt_value = round(sqrt_value)
    else:
        sqrt_value = round(sqrt_value, 2)
    var.set('Korijen vašeg broja je: {}'.format(sqrt_value))

root = tk.Tk()
var = tk.StringVar()
var.set('Korijen vašeg broja je: -')
e = tk.StringVar()
round_bool = tk.BooleanVar()
# e.set('0')
root.title('Korijen')
# root.geometry('600x400')


button = tk.Button(root, text='Izračunaj!', command=klik)
# button.pack(pady=30)
button.grid(column=0, row=1, pady=10, padx=(10,30), ipadx=30, ipady=50)

title_label = tk.Label(root, text='Dobrodošli u program za računanje korijena!')
title_label.grid(row=0, columnspan=2)

entry = tk.Entry(root, textvariable=e)
entry.grid(row=1, column=1)

checkbox = tk.Checkbutton(root, text='Zaokruži rezultat na cijeli broj?', variable=round_bool)
checkbox.grid(row=2, columnspan=2)

result_label = tk.Label(root, textvariable=var, font=result_font)
result_label.grid(row=3, columnspan=2)

exit_button = tk.Button(root, text='Izlaz iz programa', command=root.destroy)
exit_button.grid(row=4, columnspan=2, ipadx=10, pady=10, ipady=30)

root.mainloop()