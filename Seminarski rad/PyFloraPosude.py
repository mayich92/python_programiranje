# Importiranje potrebnih modula
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
    korisnicko_ime = entry_username.get()
    lozinka = entry_password.get()

    if provjeri_korisnika(korisnicko_ime, lozinka):
        messagebox.showinfo("Prijava", "Uspješno ste se prijavili.")
        otvori_aplikaciju()
    else:
        messagebox.showerror("Greška", "Krivo korisničko ime ili lozinka.")

def register():
    korisnicko_ime = entry_username.get()
    lozinka = entry_password.get()

    if korisnicko_ime == "" or lozinka == "":
        messagebox.showerror("Greška", "Molimo unesite korisničko ime i lozinku.")
    elif provjeri_postojanje_korisnika(korisnicko_ime):
        messagebox.showinfo("Greška", "Korisnik već postoji. Molimo odaberite drugo korisničko ime.")
    else:
        messagebox.showinfo("Registrirano", "Uspješno ste se registrirali.")
        dodaj_korisnika(korisnicko_ime, lozinka)

def provjeri_korisnika(korisnicko_ime, lozinka):
    # Spajanje na bazu podataka
    veza = sqlite3.connect('baza_korisnika.db')
    kursor = veza.cursor()

    # Izvršavanje SQL upita za provjeru korisnika
    upit = "SELECT * FROM korisnici WHERE korisnicko_ime = ? AND lozinka = ?"
    parametri = (korisnicko_ime, lozinka)
    kursor.execute(upit, parametri)

    # Dohvaćanje rezultata upita
    rezultat = kursor.fetchone()

    # Zatvaranje veze s bazom podataka
    veza.close()

    # Povratna vrijednost ovisi o rezultatu provjere
    if rezultat:
        return True  # Korisnik pronađen u bazi podataka
    else:
        return False  # Korisnik nije pronađen u bazi podataka

def provjeri_postojanje_korisnika(korisnicko_ime):
    # Spajanje na bazu podataka
    veza = sqlite3.connect('baza_korisnika.db')
    kursor = veza.cursor()

    # Izvršavanje SQL upita za provjeru postojanja korisnika
    upit = "SELECT * FROM korisnici WHERE korisnicko_ime = ?"
    parametri = (korisnicko_ime,)
    kursor.execute(upit, parametri)

    # Dohvaćanje rezultata upita
    rezultat = kursor.fetchone()

    # Zatvaranje veze s bazom podataka
    veza.close()

    # Povratna vrijednost ovisi o rezultatu provjere
    if rezultat:
        return True  # Korisnik s danim korisničkim imenom postoji u bazi podataka
    else:
        return False  # Korisnik s danim korisničkim imenom ne postoji u bazi podataka

def dodaj_korisnika(korisnicko_ime, lozinka):
    # Spajanje na bazu podataka
    veza = sqlite3.connect('baza_korisnika.db')
    kursor = veza.cursor()

    # Izvršavanje SQL upita za stvaranje tablice ako ne postoji
    kursor.execute('''CREATE TABLE IF NOT EXISTS korisnici
                     (korisnicko_ime TEXT PRIMARY KEY, lozinka TEXT)''')

    # Izvršavanje SQL upita za provjeru postojanja korisnika
    kursor.execute('SELECT * FROM korisnici WHERE korisnicko_ime=?', (korisnicko_ime,))
    rezultat = kursor.fetchone()

    if rezultat is None:
        # Ako korisnik ne postoji, izvršavamo SQL upit za dodavanje korisnika
        kursor.execute('INSERT INTO korisnici VALUES (?, ?)', (korisnicko_ime, lozinka))
        veza.commit()  # Potvrđujemo promjene u bazi

        messagebox.showinfo("Registracija", "Uspješno ste se registrirali.")
        otvori_aplikaciju()
    else:
        messagebox.showerror("Greška", "Korisnik već postoji. Molimo odaberite drugo korisničko ime.")

    # Zatvaranje veze s bazom podataka
    kursor.close()
    veza.close()
def otvori_aplikaciju():
    # Stvaranje novog prozora za aplikaciju
    aplikacija_prozor = tk.Toplevel(root)
    aplikacija_prozor.title("Aplikacija")
    aplikacija_prozor.geometry("600x400")

    # Dodajte ostatak koda za vašu aplikaciju ovdje

    # Primjer: Dodavanje oznake u aplikacijski prozor
    lbl_dobrodoslica = tk.Label(aplikacija_prozor, text="Dobrodošli u aplikaciju!")
    lbl_dobrodoslica.pack()

    # Primjer: Dodavanje gumba za odjavu
    btn_odjava = tk.Button(aplikacija_prozor, text="Odjava", command=aplikacija_prozor.destroy)
    btn_odjava.pack()

# root = tk.Tk()
# root.title("Prijava i registracija")
# root.geometry("500x300")

label_username = tk.Label(root, text="Korisničko ime:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Lozinka:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Prijavi me", command=login)
btn_login.pack()

btn_register = tk.Button(root, text="Registriraj se", command=register)
btn_register.pack()

root.mainloop()



def sinkroniziraj_senzore():
    senzori_simulator.generiraj_vrijednosti_senzora()
    vlaznost_zemlje, ph_vrijednost, salinitet_zemlje, razina_svjetla, temperatura_zraka = senzori_simulator.dohvati_vrijednosti_senzora()


    lbl_vlaznost_zemlje.config(text="Vlažnost zemlje: {:.2f}".format(vlaznost_zemlje))
    lbl_ph_vrijednost.config(text="pH vrijednost: {:.2f}".format(ph_vrijednost))
    lbl_salinitet_zemlje.config(text="Salinitet zemlje: {:.2f}".format(salinitet_zemlje))
    lbl_razina_svjetla.config(text="Razina svjetla: {:.2f}".format(razina_svjetla))
    lbl_temperatura_zraka.config(text="Temperatura zraka: {:.2f}".format(temperatura_zraka))

def sync_callback():
    sinkroniziraj_senzore()

prozor = tk.Tk()
prozor.title("Dobrodošli!")
prozor.geometry("600x400")

# Dodavanje gumba "SYNC" u prozor
gumb_sync = tk.Button(prozor, text="SYNC", command=sync_callback)
gumb_sync.pack()

# Dodavanje oznaka za prikaz brojčanih vrijednosti senzora
lbl_vlaznost_zemlje = tk.Label(prozor, text="Vlažnost zemlje: ")
lbl_vlaznost_zemlje.pack()

lbl_ph_vrijednost = tk.Label(prozor, text="pH Vrijednost: ")
lbl_ph_vrijednost.pack()

lbl_salinitet_zemlje = tk.Label(prozor, text="Salinitet zemlje: ")
lbl_salinitet_zemlje.pack()

lbl_razina_svjetla = tk.Label(prozor, text="Razina svjetla: ")
lbl_razina_svjetla.pack()

lbl_temperatura_zraka = tk.Label(prozor, text="Temperatura zraka: ")
lbl_temperatura_zraka.pack()

prozor.mainloop()



