# https://chatgpt.com/c/6746f2e7-5b00-8009-a499-007570343de4

run = 1
if run == 0:
    ###### Step 3: Basic Projects ####### 
    # 1. Mini Calculator
    '''
    Task:

    Create a simple calculator that:
    Asks the user for two numbers.
    Asks the user to choose an operation (+, -, *, /).
    Prints the result of the operation.
    Ensure that the calculator handles division by zero correctly, by showing a message like "Cannot divide by zero."
    Ask if theuser wants to perform another calculation after each one.
    '''

    def calculate():
        while True:
            print("Simple Calculator")
            print("Enter two numbers and an operator (+, -, *, /): ")

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero."
            else:
                result = "Invalid operator."

            print(result)

            choice = input("Do you want to perform another calculation? (y/n): ")
            if choice.lower() != 'y':
                break

    calculate()

if run == 0:
    # 2. Lists and File Handling
    # Task:

    # Ask the user to input five names and store them in a list.
    # Write the list of names to a file named names.txt.
    # Read the contents of names.txt and print each name in uppercase.

    print("Lists and File Handling")
    print("Input five names and store them in a list. ")

    name_list = input("Enter five names: ").split()
    with open("names.txt", "w") as file:
        for name in name_list:
            file.write(name.upper() + "\n")

    with open('names.txt', 'r') as file:
        saved_list = [line.strip() for line in file.readlines()]

    for name in saved_list:
        print(name.upper())


# 3. API Requests with requests
# Task:

# Install the requests library:
#  
#  write this in bash-terminal:
# pip install requests
# Make an API call to a public API (e.g., https://jsonplaceholder.typicode.com/todos/1).
# Extract the title from the JSON response and print it.

# import subprocess

# def install_package(package_name):
#   subprocess.run(['pip', 'install', package_name])

# install_package('requests')

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)



# Fetch data from a website
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print(response.status_code)
    print(response.json())