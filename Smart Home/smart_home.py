import tkinter as tk
from tkinter import ttk
from sense_emu import SenseHat
import requests
import xml.etree.ElementTree as ET
import sqlite3
from datetime import datetime


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a Sense HAT Emulator instance
        self.sense_hat = SenseHat()

        # Create the weather module
        self.weather_module = WeatherModule(self, self.sense_hat)

        # Schedule the initial weather data update
        self.weather_module.update_weather_data()

        # Set up the main window
        self.title("My Smart Home")
        self.geometry("400x300")

        # Create tabs for different modules
        self.tab_control = tk.ttk.Notebook(self)



class WeatherModule(tk.Frame):
    def __init__(self, master, sense_hat):
        super().__init__(master)
        self.master = master
        self.sense_hat = sense_hat

        # Create labels for displaying weather data
        self.current_temperature_indoor = tk.StringVar()
        self.current_temperature_outdoor = tk.StringVar()
        self.humidity_indoor = tk.StringVar()
        self.humidity_outdoor = tk.StringVar()
        self.air_pressure_indoor = tk.StringVar()
        self.air_pressure_outdoor = tk.StringVar()

        temperature_label_indoor = tk.Label(self, text="Indoor Temperature:")
        temperature_label_indoor.grid(row=0, column=0, sticky="e")
        temperature_value_indoor = tk.Label(self, textvariable=self.current_temperature_indoor)
        temperature_value_indoor.grid(row=0, column=1, sticky="w")

        temperature_label_outdoor = tk.Label(self, text="Outdoor Temperature:")
        temperature_label_outdoor.grid(row=1, column=0, sticky="e")
        temperature_value_outdoor = tk.Label(self, textvariable=self.current_temperature_outdoor)
        temperature_value_outdoor.grid(row=1, column=1, sticky="w")

        humidity_label_indoor = tk.Label(self, text="Indoor Humidity:")
        humidity_label_indoor.grid(row=3, column=0, sticky="e")
        humidity_value_indoor = tk.Label(self, textvariable=self.humidity_indoor)
        humidity_value_indoor.grid(row=3, column=1, sticky="w")

        humidity_label_outdoor = tk.Label(self, text="Outdoor Humidity:")
        humidity_label_outdoor.grid(row=4, column=0, sticky="e")
        humidity_value_outdoor = tk.Label(self, textvariable=self.humidity_outdoor)
        humidity_value_outdoor.grid(row=4, column=1, sticky="w")

        air_pressure_label_indoor = tk.Label(self, text="Indoor Air Pressure:")
        air_pressure_label_indoor.grid(row=5, column=0, sticky="e")
        air_pressure_value_indoor = tk.Label(self, textvariable=self.air_pressure_indoor)
        air_pressure_value_indoor.grid(row=5, column=1, sticky="w")

        air_pressure_label_outdoor = tk.Label(self, text="Outdoor Air Pressure:")
        air_pressure_label_outdoor.grid(row=6, column=0, sticky="e")
        air_pressure_value_outdoor = tk.Label(self, textvariable=self.air_pressure_outdoor)
        air_pressure_value_outdoor.grid(row=6, column=1, sticky="w")

        # Create a label for displaying the temperature message
        self.temperature_message = tk.StringVar()
        temperature_message_label = tk.Label(self, textvariable=self.temperature_message)
        temperature_message_label.grid(row=7, column=0, columnspan=2)

    def update_temperature_message(self):
        # Get the current outdoor temperature
        temperature = float(self.current_temperature_outdoor.get().replace("°C", ""))

        # Determine the temperature message based on the current outdoor temperature
        if temperature > 22:
            message = "Vrijeme je za kratke rukave"
        elif 12 < temperature <= 22:
            message = "Vrijeme je za laganu jaknu"
        elif 0 < temperature <= 12:
            message = "Vrijeme je za zimsku jaknu"
        else:
            message = "Vrijeme je za kapu, šal i zimsku jaknu"

        # Update the temperature message label
        self.temperature_message.set(message)

        self.pack()

    def update_weather_data(self):
        # Update indoor temperature, humidity, and air pressure from Sense HAT Emulator
        temperature_indoor = self.sense_hat.get_temperature()
        humidity_indoor = self.sense_hat.get_humidity()
        air_pressure_indoor = self.sense_hat.get_pressure()

        # Get outdoor weather data by making a request to the provided URL
        response = requests.get("https://vrijeme.hr/hrvatska_n.xml")
        root = ET.fromstring(response.content)

        # Find the weather data for Varaždin
        for grad in root.findall("Grad"):
            grad_ime = grad.find("GradIme").text
            if grad_ime == "Varaždin":
                podatci = grad.find("Podatci")
                temperature_outdoor = podatci.find("Temp").text
                humidity_outdoor = podatci.find("Vlaga").text
                air_pressure_outdoor = podatci.find("Tlak").text
                break

        # Update the GUI labels with the new weather data
        self.current_temperature_indoor.set(f"{int(temperature_indoor)}°C")
        self.humidity_indoor.set(f"{int(humidity_indoor)}%")
        self.air_pressure_indoor.set(f"{round(air_pressure_indoor, 2)} hPa")

        self.current_temperature_outdoor.set(f"{temperature_outdoor}°C")
        self.humidity_outdoor.set(f"{humidity_outdoor}%")
        self.air_pressure_outdoor.set(f"{air_pressure_outdoor} hPa")

        # Save the weather data to the SQLite database
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect("/home/maja/Desktop/weather_data.db")
        c = conn.cursor()
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Temperature Indoor", temperature_indoor))
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Humidity Indoor", humidity_indoor))
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Air Pressure Indoor", air_pressure_indoor))
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Temperature Outdoor", temperature_outdoor))
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Humidity Outdoor", humidity_outdoor))
        c.execute("INSERT INTO weather_data (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                  (timestamp, "Air Pressure Outdoor", air_pressure_outdoor))
        conn.commit()
        conn.close()

        # Update the GUI labels with the new weather data
        self.current_temperature_indoor.set(f"{int(temperature_indoor)}°C")
        self.humidity_indoor.set(f"{int(humidity_indoor)}%")
        self.air_pressure_indoor.set(f"{round(air_pressure_indoor, 2)} hPa")

        self.current_temperature_outdoor.set(f"{temperature_outdoor}°C")
        self.humidity_outdoor.set(f"{humidity_outdoor}%")
        self.air_pressure_outdoor.set(f"{air_pressure_outdoor} hPa")

        # Update the temperature message
        self.update_temperature_message()

        # Schedule the next weather data update after 5 seconds
        self.master.after(5000, self.update_weather_data)


# Run the Smart Home application
app = SmartHomeApp()
app.mainloop()
