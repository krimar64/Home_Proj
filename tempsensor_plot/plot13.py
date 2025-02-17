import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk
from datetime import datetime
import csv

# Skapa ett tkinter-fönster för att välja filer
root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

# Visa en dialogruta för att välja filer
file_paths = filedialog.askopenfilenames(title="Välj CSV-filer", filetypes=[("CSV Files", "*.csv")])

# Plotta temperaturerna från alla sensorer i samma graf
plt.figure(figsize=(10, 6))

def detect_delimiter(file_path):
    """Upptäcker vilket avgränsartecken som används i filen."""
    with open(file_path, 'r') as file:
        sniffer = csv.Sniffer()
        first_line = file.readline()
        delimiter = sniffer.sniff(first_line).delimiter
    return delimiter

for file in file_paths:
    try:
        # Upptäck avgränsaren
        delimiter = detect_delimiter(file)
        
        # Läs in CSV-filen med den identifierade avgränsaren
        data = pd.read_csv(file, delimiter=delimiter)
        
        # Konvertera 'time' kolumnen till datetime
        data['time'] = pd.to_datetime(data['time'])

        # Plotta temperaturerna med linje utan punkter
        sensor_name = file.split("/")[-1].split(".")[0]
        plt.plot(data["time"], data["temp"], label=sensor_name)

    except Exception as e:
        print(f"Error reading file {file}: {e}")

# Definiera det tidsintervall som ska visas
start_time = datetime(2024, 1, 1, 1, 30)  # Startpunkt: År, månad, dag, timme, minut
end_time = datetime(2024, 4, 1, 3, 0)    # Slutpunkt: År, månad, dag, timme, minut

# Begränsa x-axeln till detta tidsintervall
plt.xlim([start_time, end_time])

# Plotta grafen
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur från olika sensorer")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
