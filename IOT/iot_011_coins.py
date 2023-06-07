import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading

url = 'https://coinmarketcap.com/'


class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Crypto Values")
        self.geometry("800x600")

        self.label = tk.Label(self, text="Vrijednosti kriptovaluta:")
        self.label.pack()

        self.dropdown = tk.OptionMenu(self, tk.StringVar(), *range(1, 11), command=self.on_dropdown_select)
        self.dropdown.pack()

        self.value_label = tk.Label(self, text="")
        self.value_label.pack()

        self.exit_button = tk.Button(self, text="Izlaz", command=self.quit)
        self.exit_button.pack()

        self.update_values()  # Pokreni prvo ažuriranje vrijednosti

    def retrieve(self):
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find('tbody')
        table_rows = table.find_all('tr')
        table_rows = table_rows[:5]
        crypto_data = []
        for tr in table_rows:
            cells = tr.find_all('td')
            cells = cells[1:4]
            cells = [i.text for i in cells]
            cells[1] = cells[1].split(cells[0])
            crypto_data.append(cells)
        return crypto_data

    def update_values(self):
        # Dohvati scrape vrijednosti kriptovaluta
        data = self.retrieve()

        # Formatiraj podatke za prikaz
        values_str = ""
        for currency in data:
            ordinal = currency[0]
            name = currency[1][0]
            abb = currency[1][1]
            price = currency[2]
            values_str += f'{ordinal}. {name}:{abb}\t{price}\n'

        # Ažuriraj prikazane vrijednosti
        self.label.config(text="Vrijednosti kriptovaluta:")
        self.value_label.config(text=values_str)

        # Pokreni ponovno ažuriranje nakon 3 sekunde
        self.after(3000, self.update_values)

    def on_dropdown_select(self, value):
        currency_index = int(value) - 1
        currency_data = self.retrieve()
        if currency_index < len(currency_data):
            selected_currency = currency_data[currency_index]
            name = selected_currency[1][0]
            abb = selected_currency[1][1]
            price = selected_currency[2]
            messagebox.showinfo("Odabrana kriptovaluta", f"{name}:{abb}\nVrijednost: {price}")


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()
