import tkinter as tk
# https://docs.python.org/3/library/tkinter.messagebox.html
from tkinter import messagebox    # showinfo, showwarning, showerror (title=, message=)
# https://docs.python.org/3/library/dialog.html#module-tkinter.filedialog
from tkinter import filedialog    # askopen...
from PIL import Image

root = tk.Tk()
label = tk.Label(root, text='Image viewer')
label.pack()

messagebox.showinfo(title='Image viewer', message='Odaberite sliku!')    # showwarning, showerror
# messagebox.showerror(title='naslov errora', message='Error!')

name = filedialog.askopenfilename()
print(name)
img = Image.open(name)
img.show()
root.mainloop()