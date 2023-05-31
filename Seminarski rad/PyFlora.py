import tkinter as tk
from vrijednosti_sa_senzora import SenzoriSimulator
from login_register import login, register_window

senzori_simulator = SenzoriSimulator()

class PyFloraPosuda(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("PyFloraPosuda")
        self.master.geometry("1000x800")

        self.create_widgets()

    def create_widgets(self):
        entry_width = 18
        self.label_login = tk.Label(self.master, text="Login", font=("Helvetica", 24))
        self.label_login.pack()
        self.label_login.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.label_username = tk.Label(self.master, text="Username:")
        self.label_username.pack()
        self.label_username.place(relx=0.44, rely=0.4, anchor=tk.CENTER)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()
        self.entry_username.place(relx=0.5, rely=0.44, anchor=tk.CENTER)

        self.label_password = tk.Label(self.master, text="Password:")
        self.label_password.pack()
        self.label_password.place(relx=0.44, rely=0.48, anchor=tk.CENTER)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()
        self.entry_password.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        self.btn_login = tk.Button(self.master, text="Login", width=entry_width, command=lambda: login(self.master,self.entry_username, self.entry_password, self))
        self.btn_login.pack()
        self.btn_login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.btn_register = tk.Button(self.master, text="Register", width=entry_width, command=lambda: register_window(self.master))
        self.btn_register.pack()
        self.btn_register.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    def create_header(self):
        self.header_frame = tk.Frame(self.master)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_pyflorapot = tk.Button(self.header_frame, text="PyFloraPot")
        self.btn_pyflorapot.pack(side=tk.LEFT, padx=75)

        self.btn_plants = tk.Button(self.header_frame, text="Plants")
        self.btn_plants.pack(side=tk.LEFT, padx=75)

        self.btn_myprofil = tk.Button(self.header_frame, text="My Profil")
        self.btn_myprofil.pack(side=tk.LEFT, padx=75)

        self.btn_sync = tk.Button(self.header_frame, text="Sync")
        self.btn_sync.pack(side=tk.LEFT, padx=75)
    def pyfloralist_widgets(self):
        for widget in root.winfo_children():
            widget.destroy()
        self.create_header()






root = tk.Tk()
app = PyFloraPosuda(master=root)
app.mainloop()
