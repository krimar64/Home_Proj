'''create function that take two columns as input.
sort both columns from smallest to largest value
take the difference between each line incolumn 2 - column1  and finally sum all differences '''

def get_sum_difference(col1, col2):
    return sum([abs(col2[i] - col1[i]) for i in range(len(col1))])

import webbrowser

def open_webpage(url):
    # Open the webpage in the default web browser
    webbrowser.open(url)

# Example usage
url = "https://adventofcode.com/2024/day/1/input"
open_webpage(url)

import requests
from bs4 import BeautifulSoup

def extract_two_columns(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Create a BeautifulSoup object from the file content
    soup = BeautifulSoup(file_content, 'html.parser')

    # Find the element containing the two columns
    column_element = soup.find('div', class_='column-container')

    # Extract the two columns
    column1 = column_element.find('div', class_='column1').text.strip()
    column2 = column_element.find('div', class_='column2').text.strip()

    return column1, column2

# Example usage
file_path = "C:\Users\ekrrmai\OneDrive - Ericsson\Ericsson\Python_Home\Advent\1\data.txt"
column1, column2 = extract_two_columns(file_path)

print("Column 1:", column1)
print("Column 2:", column2)