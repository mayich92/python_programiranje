
import tkinter as tk

broj_klikova = 0

def klik():
    global broj_klikova
    broj_klikova += 1
    var.set('Kliknuo si me {} puta'.format(broj_klikova))

root = tk.Tk()
var = tk.StringVar()
root.title('Moja prva Tkinter aplikacija!')
root.geometry('600x400')


button = tk.Button(root, text='Klikni me!', command=klik)
# button.pack(pady=30)
button.pack(pady=(10, 30), ipadx=30, ipady=50)

label = tk.Label(root, textvariable=var)
var.set('-')
label.pack()

root.mainloop()