# Zadatak 35.
# GUI login screen - Entry za username + Entry za password + Button za pokretanje + MessageBox
# dobar dan/jutro/večer DONE
# hash lozinke DONE
# root bind Return DONE

import tkinter as tk
from tkinter import messagebox
import hashlib
from datetime import datetime, time
import sqlite3


db_name = 'Baze podataka/accounts_db.db'
query_get_password = 'SELECT pass, name FROM Accounts WHERE username='
noon = time(12, 0)

root = tk.Tk()
root.title('Sigurni sustav')
base_font = ('Helvetica', 16)
username = tk.StringVar()
password = tk.StringVar()

def hash_text(text):
    text = text.encode() 
    return hashlib.md5(text).hexdigest()

def login(event=None):
    now = datetime.now()
    now_time = time(now.hour, now.minute)
    # now = datetime.utcnow().time()    # UTC+2
    success = False
    name = None
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        query = query_get_password + '"{}"'.format(username.get())
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            hash_pass = records[0][0]
            name = records[0][1]
            if hash_pass == hash_text(password.get()):
                success = True
            else:
                succes = False
        else:
            success = False
        cursor.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

    if success:
        greeting = 'Dobar dan' if now_time > noon else 'Dobro jutro'
        message = '{}, {}!'.format(greeting, name)
        messagebox.showinfo(title='Uspješna prijava', message=message)
    else:
        message = 'Nismo uspjeli pronaći korisnika s odgovarajućim credentialsima!'
        messagebox.showerror(title='Neuspješna prijava', message=message)

username_label = tk.Label(root, text='Username: ', font=base_font)
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root, textvariable=username, font=base_font)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text='Password: ', font=base_font)
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, textvariable=password, font=base_font)
password_entry.grid(row=1, column=1)

start_button = tk.Button(root, text='Prijava', command=login, font=base_font)
start_button.grid(row=2, columnspan=2)

exit_button = tk.Button(root, text='Izlaz', command=root.destroy, font=base_font)
exit_button.grid(row=3, columnspan=2)

root.bind('<Return>', login)

root.mainloop()