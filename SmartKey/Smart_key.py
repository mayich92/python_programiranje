import tkinter as tk
import sqlite3


class SmartKey:
    def __init__(self, master):
        self.master = master
        master.title("Korisnicko sucelje")
        master.geometry("800x600")

        #Super unsafe, I know
        self.admin_pin = '0000'

        # Variables used in program
        self.original_name = None
        self.original_surname = None
        self.pin_frame = None

        self.welcome_panel = tk.Frame(self.master)
        self.welcome_panel.grid()

        # added buttons for saving, canceling, and deleting user data in the admin panel
        self.ring_button = tk.Button(self.welcome_panel, text="Pozvoniti", command=self.on_ring)
        self.ring_button.grid(row=1, column=0)
        self.unlock_button = tk.Button(self.welcome_panel, text="Otključati", command=self.on_unlock)
        self.unlock_button.grid(row=1, column=1)

    def disable_frame(self, frame):
        for child in frame.winfo_children():
            child.config(state="disabled")

    def enable_frame(self, frame):
        for child in frame.winfo_children():
            child.config(state="normal")

    def on_click(self, value):
        if value == 'C':
            for entry in self.pin_entries:
                entry.delete(0, 'end')
            self.message_box.delete('1.0', 'end')
        else:
            for entry in self.pin_entries:
                if not entry.get():
                    entry.insert(0, value)
                    break

        pin = ''.join([entry.get() for entry in self.pin_entries])
        if pin == self.admin_pin and value == 'E':
            admin_window = tk.Toplevel(self.master)
            admin_window.title("Administracija sustava")
            tk.Label(admin_window, text="Zelis li pokrenuti administraciju sustava?").grid()
            tk.Button(admin_window, text="Da", command=lambda: [admin_window.destroy(), self.open_admin_panel()]).grid()
            tk.Button(admin_window, text="Ne", command=admin_window.destroy).grid()
        else:
            self.pin_frame.grid()
        if len(pin) == 4 and value == 'E':
            conn = sqlite3.connect('users.db')
            c = conn.cursor()

            c.execute('SELECT * FROM users WHERE pin=?', (pin,))
            row = c.fetchone()

            if row is not None:
                name, surname, pin, active = row

                ime_text = name
                prezime_text = surname
                pin_text = str(pin)
                aktivan_text = 'Aktivan' if active else 'Neaktivan'

                # clear message box before inserting new value
                self.message_box.delete('1.0', 'end')

                # insert success message and user name and surname into message box if user is active
                if active:
                    success_message = f"Uspjesno unesen PIN\nDobro došao {ime_text} {prezime_text}"
                    self.message_box.insert(tk.END, success_message)
                else:
                    # insert error message into message box if user is inactive
                    error_message = f"{ime_text} {prezime_text}, ne mozete vise uci u zgradu!"
                    self.message_box.insert(tk.END, error_message)

            conn.close()

    def on_select_user(self, event):
        # check if an item is selected in the listbox
        if event.widget.curselection():
            # get the index of the selected item in the listbox
            index = int(event.widget.curselection()[0])
            # get the value of the selected item in the listbox
            value = event.widget.get(index)
            # split value into variables
            fullname, pin_value, active = value.split(" - ")
            name, surname = fullname.split(' ')
            pin_value = pin_value.split(": ")[1]
            # populate textboxes and checkbox with values from selected user in listbox
            self.ime_textbox.delete(0, 'end')  # clear Ime textbox before inserting new value
            self.ime_textbox.insert(0, name)  # populate Ime textbox with name from selected user in listbox
            self.prezime_textbox.delete(0, 'end')  # clear Prezime textbox before inserting new value
            self.prezime_textbox.insert(0,
                                        surname)  # populate Prezime textbox with surname from selected user in listbox
            self.pin_textbox.delete(0, 'end')  # clear PIN textbox before inserting new value
            self.pin_textbox.insert(0, pin_value)  # populate PIN textbox with pin from selected user in listbox
            if active == 'Aktivan':
                self.aktivan_checkbox.select()
            else:
                self.aktivan_checkbox.deselect()

            # store original name and surname of selected user
            self.original_name = name
            self.original_surname = surname

    def on_ring(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")
        label = tk.Label(new_window, text="Zvono je aktivirano, uskoro ce netko doci otvoriti vrata")
        label.pack()

    def on_unlock(self):
        if not self.pin_frame:

            self.pin_frame = tk.Frame(self.master)
            self.pin_frame.grid(row=1, column=0)

            self.message_frame = tk.Frame(self.master)
            self.message_frame.grid(row=1, column=1)

            self.pin_entries = []
            for i in range(4):
                entry = tk.Entry(self.pin_frame, width=2)
                entry.grid(row=0, column=i, pady=25)
                self.pin_entries.append(entry)

            buttons = [
                '1', '2', '3',
                '4', '5', '6',
                '7', '8', '9',
                'C', '0', 'E'
            ]

            row = 1
            col = 0
            for button in buttons:
                cmd = lambda x=button: self.on_click(x)
                tk.Button(self.pin_frame, text=button, command=cmd).grid(row=row, column=col)
                col += 1
                if col > 2:
                    col = 0
                    row += 1

            # added a message box for displaying success message and user name and surname
            self.message_box = tk.Text(self.message_frame, height=12, width=50)
            self.message_box.grid()

            pin = ''.join(entry.get() for entry in self.pin_entries)
            if pin == self.admin_pin:
                admin_window = tk.Toplevel(self.master)
                admin_window.title("Administracija sustava")
                tk.Label(admin_window, text="Zelis li pokrenuti administraciju sustava?").grid()
                tk.Button(admin_window, text="Da", command=lambda: [admin_window.destroy(), self.open_admin_panel()]).grid()
                tk.Button(admin_window, text="Ne", command=admin_window.destroy).grid()
            else:
                self.pin_frame.grid()
                self.message_frame.grid()

    def open_admin_panel(self):
        self.disable_frame(self.welcome_panel)
        self.disable_frame(self.pin_frame)

        self.admin_panel = tk.Frame(self.master)
        self.admin_panel.grid(row=2, column=0, pady=25, columnspan=3)

        # added a listbox with a scrollbar
        self.user_listbox = tk.Listbox(self.admin_panel, width=30)
        self.user_listbox.grid(row=4, column=0, rowspan=5)


        # bind the listbox selection event to a handler function
        self.user_listbox.bind('<<ListboxSelect>>', self.on_select_user)

        tk.Label(self.admin_panel, text="Ime").grid(row=4, column=1)
        self.ime_textbox = tk.Entry(self.admin_panel)  # added textbox for Ime
        self.ime_textbox.grid(row=4, column=2)

        tk.Label(self.admin_panel, text="Prezime").grid(row=5, column=1)
        self.prezime_textbox = tk.Entry(self.admin_panel)  # added textbox for Prezime
        self.prezime_textbox.grid(row=5, column=2)

        tk.Label(self.admin_panel, text="PIN(4 broja)").grid(row=6, column=1)
        self.pin_textbox = tk.Entry(self.admin_panel)  # added textbox for PIN
        self.pin_textbox.grid(row=6, column=2)

        tk.Label(self.admin_panel, text="Aktivan").grid(row=7, column=1)  # added label for Aktivan
        self.aktivan_var = tk.BooleanVar()
        self.aktivan_checkbox = tk.Checkbutton(self.admin_panel, variable=self.aktivan_var)  # added checkbox for Aktivan
        self.aktivan_checkbox.grid(row=7, column=2)

        # added buttons for saving, canceling, and deleting user data in the admin panel
        tk.Button(self.admin_panel, text="Spremi", command=self.on_save).grid(row=8, column=1)  # added Spremi button
        tk.Button(self.admin_panel, text="Odustani", command=self.on_cancel).grid(row=8,column=2)  # added Odustani button
        tk.Button(self.admin_panel, text="Izbriši", command=self.on_delete).grid(row=8, column=3)  # added Izbriši button

        self.admin_panel.grid()
        # populate user_listbox with data from database
        self.refresh_user_list()

    def on_save(self):
        # get the values entered by the user
        name = self.ime_textbox.get()
        surname = self.prezime_textbox.get()
        pin_value = self.pin_textbox.get()
        active = self.aktivan_var.get()

        # update the database with the new values
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("UPDATE users SET ime=?, prezime=?, pin=?, aktivan=? WHERE ime=? AND prezime=?",
                  (name, surname, pin_value, active, self.original_name, self.original_surname))

        # check if any rows were affected by the UPDATE statement
        if c.rowcount == 0:
            # no rows were affected, so create a new user
            c.execute("INSERT INTO users (ime, prezime, pin, aktivan) VALUES (?, ?, ?, ?)",
                      (name, surname, pin_value, active))
            # update label text
            #self.message_label.config(text=f"Korisnik {name} {surname} je kreiran")
            self.message_box.insert(tk.END, f"Korisnik {name} {surname} je kreiran.\n")
        else:
            # one or more rows were affected by the UPDATE statement
            self.message_box.insert(tk.END, f"Korisnik {self.original_name} {self.original_surname} je ažuriran.\n")

        conn.commit()
        conn.close()

        # refresh user_listbox
        self.refresh_user_list()

        # clear textboxes and reset Checkbutton
        self.ime_textbox.delete(0, 'end')
        self.prezime_textbox.delete(0, 'end')
        self.pin_textbox.delete(0, 'end')
        self.aktivan_var.set(False)
    def on_cancel(self):
        # check if any textbox has an entry
        if self.ime_textbox.get() or self.prezime_textbox.get() or self.pin_textbox.get():
            # clear textboxes and reset Checkbutton
            self.ime_textbox.delete(0, 'end')
            self.prezime_textbox.delete(0, 'end')
            self.pin_textbox.delete(0, 'end')
            self.aktivan_var.set(False)
        else:
            # open new window with Izlaz iz aplikacije and Odustani buttons
            self.new_window = tk.Toplevel(self.master)
            tk.Button(self.new_window, text="Izlaz iz aplikacije", command=self.on_exit).grid()
            tk.Button(self.new_window, text="Odustani", command=self.on_cancel_new_window).grid()

    def on_exit(self):
        # terminate the program
        self.master.destroy()

    def on_cancel_new_window(self):
        # close new window
        self.new_window.destroy()

    def on_delete(self):
        # get the values entered by the user
        name = self.ime_textbox.get()
        surname = self.prezime_textbox.get()

        # delete user from database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE ime=? AND prezime=?", (name, surname))
        conn.commit()
        conn.close()

        # refresh user_listbox
        self.refresh_user_list()

        # clear textboxes and reset Checkbutton
        self.ime_textbox.delete(0, 'end')
        self.prezime_textbox.delete(0, 'end')
        self.pin_textbox.delete(0, 'end')
        self.aktivan_var.set(False)

        # update label text
        delete_message = f"Korisnik {name} {surname} je izbrisan\n"
        self.message_box.insert(tk.END, delete_message)

    def refresh_user_list(self):
        # clear user_listbox
        self.user_listbox.delete(0, 'end')

        # populate user_listbox with data from database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM users'):
            name, surname, pin_value, active = row
            active_text = 'Aktivan' if active else 'Neaktivan'
            list_item = f"{name} {surname} - PIN: {pin_value} - {active_text}"
            if not list_item in [self.user_listbox.get(i) for i in range(self.user_listbox.size())]:
                self.user_listbox.insert('end', list_item)
        conn.close()


root = tk.Tk()
smart_key = SmartKey(root)
root.mainloop()