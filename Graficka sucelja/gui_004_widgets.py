
import tkinter as tk

broj_klikova = 0

def klik():
    global broj_klikova
    broj_klikova += 1
    var.set('Kliknuo si me {} puta'.format(broj_klikova))

root = tk.Tk()
var = tk.StringVar()
root.title('Moja prva Tkinter aplikacija!')
# root.geometry('600x400')


button = tk.Button(root, text='Klikni me!', command=klik)
# button.pack(pady=30)
button.grid(column=0, row=1, pady=10, padx=(10,30), ipadx=30, ipady=50)

title_label = tk.Label(root, text='Dobrodošli u kliker!')
title_label.grid(row=0, columnspan=2)

label = tk.Label(root, textvariable=var)
var.set('Kliknuo si me 0 puta')
label.grid(row=1, column=1)

exit_button = tk.Button(root, text='exit', command=root.destroy)
exit_button.grid(row=2, columnspan=2, ipadx=10, pady=10, ipady=30)

root.mainloop()