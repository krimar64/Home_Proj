#Mosh2

#For / While
print("for")
numbers=[1,2,3,4,5]
for item in numbers:
    print(item)

print("while")

i=0
while i < len(numbers):
    print(numbers[i])
    i=i+1

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for d in days:
    if(d=="Thursday"):break #also works with 'continue' 
    print(d)
print()

#range
print("numbers2")
numbers2 = range(5)
for number in numbers2:
    print(number)
print("range with start stop and no variable, and with step")

for number in range(5,10,2):
    print(number)

#Tuples
# immutable = 'does not support item assignment'
#Lists = square bracket
#Tuples = parenthesies
#Methods does not exist *.append ...
#only count and index
tuple_list =(1,2,3,4,5)
#tuple_list[0]=2


