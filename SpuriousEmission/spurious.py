'''
Create a function that opens an xlsx-file
Row 43 is the header row.  
Find the colum with name spur_freq_per_10_mhz and pow_rf_dbm_per_10_mhz
create a plot with frequency on the x-axis and pow_rf_dbm on the y-axis
'''

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# open dialog for open excel file

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx")])
    return list(files)

#


def plot_selected_files():
    selected_files = select_files()
    if selected_files:
        fig, ax = plt.subplots()
        for file in selected_files:
            df = pd.read_csv(file, sep=';')
            # Kolla om 'time' kolumnen finns och använd ett annat namn om det behövs
            time_column = 'time' if 'time' in df.columns else 'timestamp'
            df[time_column] = pd.to_datetime(df[time_column])
            ax.plot(df[time_column], df['temp'], label=file)
        plt.xticks(rotation=45, ha='right')
        ax.set_xlabel('Tid')
        ax.set_ylabel('Temperatur (°C)')
        ax.legend()
        plt.show()

root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

plot_selected_files()
