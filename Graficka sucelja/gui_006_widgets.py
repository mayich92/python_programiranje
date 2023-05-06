import tkinter as tk

base_font = ('Helvetica', 12)

root = tk.Tk()
root.title('Neka aplikacija')

def print_choice():
    print(var.get())

var = tk.StringVar()

r1 = tk.Radiobutton(root, text="Option 1", variable=var, value='prva', font=base_font, command=print_choice)
r1.pack()

r2 = tk.Radiobutton(root, text="Option 2", variable=var, value='druga', font=base_font, command=print_choice)
r2.pack()

r3 = tk.Radiobutton(root, text="Option 3", variable=var, value='treća', font=base_font, command=print_choice)
r3.pack()

var.set(None)

button = tk.Button(root, text='Gumb', command=print_choice, font=base_font)
button.pack()

exit_button = tk.Button(root, text='Izlaz iz programa', command=root.destroy, font=base_font)
exit_button.pack()

root.mainloop()