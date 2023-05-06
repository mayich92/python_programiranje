import tkinter as tk

base_font = ('Helvetica', 12)

root = tk.Tk()
root.title('Neka aplikacija')

def print_choice():
    print(var.get())

var = tk.StringVar()

choices = {
    'Option 1': 'prva',
    'Option 2': 'druga',
    'Option 3': 'treća',
    'Option 4': 'četvrta'
}

for key in choices.keys():
    r = tk.Radiobutton(root, text=key, variable=var, value=choices[key], font=base_font, command=print_choice)
    r.pack()

var.set(None)

button = tk.Button(root, text='Gumb', command=print_choice, font=base_font)
button.pack()

exit_button = tk.Button(root, text='Izlaz iz programa', command=root.destroy, font=base_font)
exit_button.pack()

root.mainloop()