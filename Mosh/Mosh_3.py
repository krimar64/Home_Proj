#import packages or modules
import math
print("pi is ", math.pi)

def greet(first_name,last_name):
    print(f"Hi {first_name}")
    print(f"your last name is {last_name}")

greet("Krister","Martini")

#Working with functions and passing variables to a file

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Krister")
file=open("content.txt","w")
file.write(message)

print()
def increment(number,another,by=2): #always required params first
    return number + by

print(increment(5,5))
print()
print("*args wait, what?")
# *args wait, what?
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number    
        # print(total)
    return total
print(multiply(2,3,4,5))

# **args
print("**args")
def save_user(**user):
    print(user)
    print(user["name"])
# This will get us a dictionary

save_user(id=1, name="Krister",age=22)





