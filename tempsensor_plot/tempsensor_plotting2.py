import matplotlib.pyplot as plt
import pandas as pd

# Läs in data från CSV-filen (ersätt "din_fil.csv" med rätt filväg)
#sovrum = pd.read_csv(r"C:\Users\krist\OneDrive\Rudebok\Krister\Python_Home\Education\tempsensor_plot\sovrum.csv")
#vardagsrum = pd.read_csv(r"C:\Users\krist\OneDrive\Rudebok\Krister\Python_Home\Education\tempsensor_plot\vardagsrum.csv")
# sovrum     = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\sovrum.csv")
# vardagsrum = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\vardagsrum.csv")
# Läs in data från CSV-filerna med korrekt separator
sovrum = pd.read_csv("C:\\Users\\krist\\OneDrive\\Rudebok\\Krister\\Python_Home\\Education\\tempsensor_plot\\sovrum.csv", sep=';')
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