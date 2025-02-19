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
    # Kontrollera om raden innehåller cellinnehållet "spur_freq_per_10_mhz" och "pow_rf_dbm_per_10_mhz"
    if "spur_freq_per_10_mhz" in row.values and "pow_rf_dbm_per_10_mhz" in row.values:
        # Hitta indexen för kolumnerna med namnen "spur_freq_per_10_mhz" och "pow_rf_dbm_per_10_mhz"
        spur_freq_per_10_mhz_index = row.values.tolist().index("spur_freq_per_10_mhz")
        pow_rf_dbm_per_10_mhz_index = row.values.tolist().index("pow_rf_dbm_per_10_mhz")

        # Hämta data från kolumnerna "spur_freq_per_10_mhz" och "pow_rf_dbm_per_10_mhz"
        spur_freq_per_10_mhz = df.iloc[index+1:, spur_freq_per_10_mhz_index]
        pow_rf_dbm_per_10_mhz = df.iloc[index+1:, pow_rf_dbm_per_10_mhz_index]

        # Print the size of the two columns
        print("Size of spur_freq_per_10_mhz column:", len(spur_freq_per_10_mhz))
        print("Size of pow_rf_dbm_per_10_mhz column:", len(pow_rf_dbm_per_10_mhz))

        # Check if the two columns have the same size
        if len(spur_freq_per_10_mhz) != len(pow_rf_dbm_per_10_mhz):
            print("Error: The two columns have different sizes.")
        else:

            # Create the plot
            plt.figure(figsize=(10, 5))

            # Plot 1
            plt.subplot(1, 2, 1)
            plt.plot(spur_freq_per_10_mhz, pow_rf_dbm_per_10_mhz)
            plt.xlabel('spur_freq_per_10_mhz')
            plt.ylabel('pow_rf_dbm_per_10_mhz')
            plt.title('Spur Frequency vs. Spur Power')

            # Plot 2
            plt.subplot(1, 2, 2)
            plt.scatter(spur_freq_per_10_mhz, pow_rf_dbm_per_10_mhz)
            plt.xlabel('spur_freq_per_10_mhz')
            plt.ylabel('pow_rf_dbm_per_10_mhz')
            plt.title('Spur Frequency vs. Spur Power')

            # Show the plot
            plt.tight_layout()
            plt.show()

        break
else:
    print("Error: Could not find the 'spur_freq_per_10_mhz' and 'pow_rf_dbm_per_10_mhz' columns.")