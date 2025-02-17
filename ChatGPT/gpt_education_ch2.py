# Step 2
# Grundläggande Python prograamming

run = 1

if run == 0:
    # 1.Hello World
    # Write a program that prints your name, your favorite color and today's date.
    name = input('What is your name? ')
    color = input('What is your favorite color? ')
    todays_date = input('What is today\'s date? ')

    print(f'Hello {name}, your favorite color is {color} and today\'s date is {todays_date}')

if run == 0:
    # 2. Basic syntax and datatypes
    # Create 3 variables, one integer, one float and one string.
    # Write a prpogram that calculates the sum of two input numbers and prints the result in a string.
    # example: The sum of 5 and 3.5 is 8.5.
    var1 = input('Enter first number: ')
    var2 = input('Enter second number: ')
    print('The sum of ' + var1 + ' and ' + var2 + ' is ' + str(float(var1) + float(var2)))

if run == 0:
    ''' 
    3. Control Structures (Loops and Conditionals)

    1. Create a program that asks the user for their age and prints:
        "You are an adult." if the age is 18 or older.
        You are not an adult." otherwise.
    2. Use a for loop to print all even numbers between 1 and 20.
    3. Use a while loop to count down from 10 to 1, printing each number.
        '''
    age = input ('What is your age? ')
    print('You are an adult.' if int(age) >= 18 else 'You are not an adult.')

if run == 0:
    print('Even numbers between 1 and 20 with a for loop:')
    for i in range(2, 21, 2):
        print(i)
    print('Even numbers between 20 and 1 with a while loop:')
    i = 20
    while i > 0:
        print(i)
        i = i - 2

#4. Functions
if run == 0:
    ''' 
    Task:
    Write a function that takes two numbers as arguments and returns their product.
    Write a function that takes a string as an argument and returns the string reversed.
    Write a function that asks the user for their name and prints a greeting: "Hello, [name]!"
    '''
    def multiply(num1, num2):
        '''Returns num1 multiplied with num2'''
        return num1 * num2

    def string_reverse(string):
        '''Returns string reversed'''
        return string[::-1]

    def greeting():
        '''Prints a greeting: "Hello, [name]!"'''
        name = input('What is your name? ')
        print(f'Hello, {name}!')

    result = multiply(5, 6)
    print ('Result: ',result)    

    print('Reversed string: ', string_reverse('Hello there!')) # string_reverse()

    greeting()
