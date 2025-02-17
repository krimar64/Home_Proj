import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

# Skapa ett tkinter-fönster för att välja filer
root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

# Visa en dialogruta för att välja filer
file_paths = filedialog.askopenfilenames(title="Välj CSV-filer", filetypes=[("CSV Files", "*.csv")])

# Skapa en tom DataFrame för att lagra kombinerad data
combined_data = pd.DataFrame()

# Läs in och kombinera data från alla valda filer
for file_path in file_paths:
    data = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, data])

# Konvertera tidsstämplarna till datetime-objekt
combined_data['time'] = pd.to_datetime(combined_data['time'])

# Sortera datan baserat på tidsstämplarna
combined_data = combined_data.sort_values(by='time')

# Plotta temperaturerna från alla sensorer i samma graf
plt.figure(figsize=(10, 6))

for sensor_name, group in combined_data.groupby('sensor'):
    plt.plot(group['time'], group['temp'], label=sensor_name, marker='o')

plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur från olika sensorer")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()