import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk


# Skapa ett tkinter-fönster för att välja filer
root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

# Visa en dialogruta för att välja filer
file_paths = filedialog.askopenfilenames(title="Välj CSV-filer", filetypes=[("CSV Files", "*.csv")])

# Läs in data från valda CSV-filer
sensor_data = pd.concat([pd.read_csv(file) for file in file_paths])

# Plotta temperaturerna från alla sensorer i samma graf
plt.figure(figsize=(10, 6))

for file_path in file_paths:
    try:
        sensor_name = file_path.split("/")[-1].split(".")[0]
        data = pd.read_csv(file_path)
        plt.plot(data["time"], data["temp"], label=sensor_name, marker='o')
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur från olika sensorer")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()