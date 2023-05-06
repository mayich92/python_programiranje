# Zadatak 32
# napisati GUI koji računa koliko korisnik ima godina
# 3x Label (godina, mjesec, dan)
# 3x Entry (godina, mjesec, dan)
# 1x Button (pokretanje)
# 1x Label (rezultat)
# 1x Button (exit)

import tkinter as tk
import datetime as dt

def process_age():
    y = int(year.get())
    m = int(month.get())
    d = int(day.get())
    dob = dt.date(y, m, d)
    t = dt.date.today()
    diff = t - dob
    diff_days = diff.days
    # diff_year = diff_days // 365
    diff_year = round(diff_days / 365)
    result.set('Imate {} godina.'.format(diff_year))

base_font = ('Helvetica', 14)

root = tk.Tk()
year, month, day = tk.StringVar(), tk.StringVar(), tk.StringVar()
result = tk.StringVar()
result.set('Niste unijeli datum rođenja!')
root.title('Računalo godina')

year_label = tk.Label(root, text='Godina:', font=base_font)
year_label.grid(row=0, column=0, padx=30)

month_label = tk.Label(root, text='Mjesec:', font=base_font)
month_label.grid(row=0, column=1, padx=30)

day_label = tk.Label(root, text='Dan:', font=base_font)
day_label.grid(row=0, column=2, padx=30)

year_entry = tk.Entry(root, textvariable=year, font=base_font)
year_entry.grid(row=1, column=0, padx=30, pady=10)

month_entry = tk.Entry(root, textvariable=month, font=base_font)
month_entry.grid(row=1, column=1, padx=30, pady=10)

day_entry = tk.Entry(root, textvariable=day, font=base_font)
day_entry.grid(row=1, column=2, padx=30, pady=10)

start_button = tk.Button(root, text='Izračunaj', font=base_font, command=process_age)
start_button.grid(row=2, columnspan=3, pady=10)

result_label = tk.Label(root, textvariable=result, font=base_font)
result_label.grid(row=3, columnspan=3, pady=10)

exit_button = tk.Button(root, text='Izlaz', command=root.destroy, font=base_font)
exit_button.grid(row=4, columnspan=3, pady=10)

root.mainloop()