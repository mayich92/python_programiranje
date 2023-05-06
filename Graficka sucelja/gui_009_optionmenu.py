
import tkinter as tk

root = tk.Tk()
base_font = ('Helvetica', 12)

def print_choice():
    print(var.get())


var = tk.StringVar()
var.set('nedefinirano')
root.title('Optionmenu primjer')

options = ['Python', 'C', 'Java']
option_menu = tk.OptionMenu(root, var, *options)
option_menu.pack()

button = tk.Button(root, text='Gumb', command=print_choice, font=base_font)
button.pack()

exit_button = tk.Button(root, text='Izlaz iz programa', command=root.destroy, font=base_font)
exit_button.pack()

root.mainloop()