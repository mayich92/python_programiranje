import tkinter as tk

# # option 1
# class GUI:
#     def __init__(self, master):
#         self.master = master
#         label = tk.Label(self.master, text='Hello world!')
#         label.pack()

# root = tk.Tk()
# gui = GUI(root)
# root.mainloop()


# option 2
class GUI:
    def __init__(self):
        self.master = tk.Tk()
        label = tk.Label(self.master, text='Hello world!')
        label.pack()

gui = GUI()
gui.master.mainloop()


# option 3
# class GUI:
#     def __init__(self):
#         self.master = tk.Tk()
#         label = tk.Label(self.master, text='Hello world!')
#         label.pack()
#         self.master.mainloop()

# gui = GUI()