import matplotlib.pyplot as plt
import pandas as pd

# Läs in data från CSV-filen med korrekt separator
sovrum = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\sovrum.csv", sep=';')

# Konvertera tid till datetime-format
sovrum['time'] = pd.to_datetime(sovrum['time'])

# Skapa en figur och axelobjekt
fig, ax = plt.subplots()

# Plotta temperatur från givaren i sovrummet
ax.plot(sovrum['time'], sovrum['temp'], label='Sovrum')

# Justera x-axelns formatering för att visa tid
plt.xticks(rotation=45, ha='right')

# Lägg till axellabels och en legend
ax.set_xlabel('Tid')
ax.set_ylabel('Temperatur (°C)')
ax.legend()

# Visa plotten
plt.show()