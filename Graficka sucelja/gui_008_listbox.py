import tkinter as tk

base_font = ('Helvetica', 12)

def print_choice():
    print(var.get())



root = tk.Tk()
var = tk.StringVar()
root.title('Listbox primjer')

listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Perl")
listbox.insert(3, "C")
listbox.pack()

# listbox.curselection()

button = tk.Button(root, text='Gumb', command=print_choice, font=base_font)
button.pack()

exit_button = tk.Button(root, text='Izlaz iz programa', command=root.destroy, font=base_font)
exit_button.pack()

root.mainloop()