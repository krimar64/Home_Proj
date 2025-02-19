import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Load the Excel file into a DataFrame
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

# read excel file
df = pd.read_excel(file_path)
selected_sheet = 'Data'
df = pd.read_excel(file_path, sheet_name=selected_sheet)

# Iterera över alla rader i DataFrame
for index, row in df.iterrows():
    # Kontrollera om raden innehåller cellinnehållet "spur_freq" och "spur_power"
    if "spur_freq" in row.values and "spur_power" in row.values:
        # Hitta indexen för kolumnerna med namnen "spur_freq" och "spur_power"
        spur_freq_index = row.values.tolist().index("spur_freq")
        spur_power_index = row.values.tolist().index("spur_power")

        # Hämta data från kolumnerna "spur_freq" och "spur_power"
        spur_freq = df.iloc[index+1:, spur_freq_index]
        spur_power = df.iloc[index+1:, spur_power_index]

        # Print the size of the two columns
        print("Size of spur_freq column:", len(spur_freq))
        print("Size of spur_power column:", len(spur_power))

        # Check if the two columns have the same size
        if len(spur_freq) != len(spur_power):
            print("Error: The two columns have different sizes.")
        else:

            # Create the plot
            plt.figure(figsize=(10, 5))

            # Plot 1
            plt.subplot(1, 2, 1)
            plt.plot(spur_freq, spur_power)
            plt.xlabel('spur_freq')
            plt.ylabel('spur_power')
            plt.title('Spur Frequency vs. Spur Power')

            # Plot 2
            plt.subplot(1, 2, 2)
            plt.scatter(spur_freq, spur_power)
            plt.xlabel('spur_freq')
            plt.ylabel('spur_power')
            plt.title('Spur Frequency vs. Spur Power')

            # Show the plot
            plt.tight_layout()
            plt.show()

        break
else:
    print("Error: Could not find the 'spur_freq' and 'spur_power' columns.")