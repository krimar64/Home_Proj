import pandas as pd
import matplotlib.pyplot as plt

# Läs in data från CSV-filer med korrekt separator
#sovrum_data = pd.read_csv('sovrum.csv')
#vardagsrum_data = pd.read_csv("vardagsrum.csv")
sovrum     = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\sovrum.csv", sep=';')
vardagsrum = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\vardagsrum.csv", sep=';')

# Konvertera tid till datetime-format för båda DataFrames
sovrum['time'] = pd.to_datetime(sovrum['time'])
vardagsrum['time'] = pd.to_datetime(vardagsrum['time'])

# Ställ in 'time' som index för båda DataFrames
sovrum.set_index('time', inplace=True)
vardagsrum.set_index('time', inplace=True)

# Interpolera värden för vardagsrumsgivaren för att passa tidsserien för sovrumsgivaren
vardagsrum_interpolated = vardagsrum.interpolate(method='time')

# Återställ 'time' tillbaka som en kolumn (om du vill)
sovrum.reset_index(inplace=True)
vardagsrum_interpolated.reset_index(inplace=True)

# Skapa en figur och axelobjekt
fig, ax = plt.subplots()

# Plotta temperatur från de två givarna
ax.plot(sovrum['time'], sovrum['temp'], label='Sovrum')
ax.plot(vardagsrum_interpolated['time'], vardagsrum_interpolated['temp'], label='Vardagsrum')

# Justera x-axelns formatering för att visa tid
plt.xticks(rotation=45, ha='right')

# Lägg till axellabels och en legend
ax.set_xlabel('Tid')
ax.set_ylabel('Temperatur (°C)')
ax.legend()

# Visa plotten
plt.show()