import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    return list(files)

def plot_selected_files():
    selected_files = select_files()
    if selected_files:
        fig, ax = plt.subplots()
        labels = []
        for file in selected_files:
            df = pd.read_csv(file, sep=';')
            # Försök använda 'time' eller 'timestamp' som tidskolumn, annars ge ett felmeddelande
            try:
                df['time'] = pd.to_datetime(df['time'])
            except KeyError:
                try:
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                except KeyError:
                    print(f"Tidskolumnen 'time' eller 'timestamp' saknas i filen {file}.")
                    continue
            print(df.head())  # Skriv ut de första raderna i DataFrame för felsökning
            ax.plot(df['time'], df['temp'], label=file)
            labels.append(file)
        plt.xticks(rotation=45, ha='right')
        ax.set_xlabel('Tid')
        ax.set_ylabel('Temperatur (°C)')
        if labels:
            ax.legend(labels)
        plt.show()

root = tk.Tk()
root.withdraw()  # Gömmer huvudfönstret

plot_selected_files()