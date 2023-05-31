import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import sqlite3
from vrijednosti_sa_senzora import SenzoriSimulator

senzori_simulator = SenzoriSimulator()

# Definiranje glavnog prozora aplikacije
root = tk.Tk()
root.title("PyFloraPosuda")
root.geometry("1000x800")


def login():
    conn = sqlite3.connect('user_db.db')
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    result = c.fetchone()

    if not result:
        window = tk.Toplevel(root)
        window.title("Error")
        window.geometry("400x300")
        label = tk.Label(window, text="You need to register first!")
        label.pack()
    else:
        username = entry_username.get()
        password = entry_password.get()

        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()

        if result:
            window = tk.Toplevel(root)
            window.title("Application")
            window.geometry("400x300")
            label = tk.Label(window, text="Welcome to the application!")
            label.pack()
        else:
            messagebox.showerror("Error", "Wrong username or password.")

    conn.close()

def register_window():
    window = tk.Toplevel(root)
    window.title("Register")
    window.geometry("400x300")

    label_name = tk.Label(window, text="Name:")
    label_name.pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    label_surname = tk.Label(window, text="Surname:")
    label_surname.pack()
    entry_surname = tk.Entry(window)
    entry_surname.pack()

    label_username = tk.Label(window, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    def register():
        name = entry_name.get()
        surname = entry_surname.get()
        username = entry_username.get()
        password = entry_password.get()

        conn = sqlite3.connect('user_db.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      surname TEXT NOT NULL,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL)''')

        c.execute("INSERT INTO users (name, surname, username, password) VALUES (?, ?, ?, ?)",
                  (name, surname, username, password))

        conn.commit()
        conn.close()

        window.destroy()
        messagebox.showinfo("Success", "Registration successful!")


    btn_register = tk.Button(window, text="Register", command=register)
    btn_register.pack()


label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack()

btn_register = tk.Button(root, text="Register", command=register_window)
btn_register.pack()

root.mainloop()
