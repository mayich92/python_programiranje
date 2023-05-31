import random
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

class SenzoriSimulator:
    def __init__(self):
        # Inicijalizacija vrijednosti senzora
        self.vlaznost_zemlje = 0
        self.ph_vrijednost = 0
        self.salinitet_zemlje = 0
        self.razina_svjetla = 0
        self.temperatura_zraka = 0


    def generiraj_vrijednosti_senzora(self):
        # Simulacija generiranja očitanih vrijednosti senzora
        self.vlaznost_zemlje = random.uniform(0, 100)
        self.ph_vrijednost = random.uniform(0, 14)
        self.salinitet_zemlje = random.uniform(0, 10)
        self.razina_svjetla = random.uniform(0, 100)
        self.temperatura_zraka = random.uniform(0, 30)


    def dohvati_vrijednosti_senzora(self):
        # Vraćanje trenutnih vrijednosti senzora
        return self.vlaznost_zemlje, self.ph_vrijednost, self.salinitet_zemlje, self.razina_svjetla, self.temperatura_zraka

    def dohvati_temperaturu_zraka(self):
        try:
            # Slanje zahtjeva za dobivanje HTML-a stranice
            response = requests.get("https://www.vrijeme.net/")

            if response.status_code == 200:
                # Parsiranje HTML-a
                soup = BeautifulSoup(response.text, "html.parser")
                temperatura_element = soup.find(class_="temperature_now")
                temperatura_zraka = temperatura_element.text.strip()
                return temperatura_zraka
            else:
                # Ako ne uspijemo dobiti HTML, generiramo zamjenske podatke
                temperatura_zraka = SenzoriSimulator.generiraj_temperaturu_zraka()
                return temperatura_zraka
        except:
            # Ako dođe do greške prilikom pristupa stranici, generiramo zamjenske podatke
            temperatura_zraka =SenzoriSimulator.generiraj_temperaturu_zraka()
            return temperatura_zraka

    def generiraj_temperaturu_zraka(self):
        # Generiranje zamjenske temperature zraka
        temperatura_zraka = random.uniform(0, 30)
        return temperatura_zraka
