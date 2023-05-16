import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, borderwidth=2, relief="solid")
label = tk.Label(frame, text="This is a label inside a sunken frame.")

frame.pack(padx=10, pady=10)
label.pack(padx=10, pady=10)

root.mainloop()
