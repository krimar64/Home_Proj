import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

# Skapa ett tkinter-fönster för att välja filer
root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

# Visa en dialogruta för att välja filer
file_paths = filedialog.askopenfilenames(title="Välj CSV-filer", filetypes=[("CSV Files", "*.csv")])

# Plotta temperaturerna från alla sensorer i samma graf
plt.figure(figsize=(10, 6))

for file in file_paths:
    try:
        # Läs in CSV-filen med semikolon som avgränsare
        data = pd.read_csv(file, sep=';')  # Använd 'sep' för att specificera avgränsare
        
        # Konvertera 'time' kolumnen till datetime
        data['time'] = pd.to_datetime(data['time'])

        # Plotta temperaturerna med linje
        sensor_name = file.split("/")[-1].split(".")[0]
        plt.plot(data["time"], data["temp"], label=sensor_name, marker='o')  # Dra linje mellan punkter

    except Exception as e:
        print(f"Error reading file {file}: {e}")

# Plotta grafen
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur från olika sensorer")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
