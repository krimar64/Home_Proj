print('Lists')
names = ["Adam", "Bertil", "Caesar"]
print(names[1])
# For-loops is nice to use here, don't need to declare variable and bracket inside loop

print("for loop")
numbers = [1,2,3,4,5]
for item in (numbers):
    print(item)
print("while loop")
i=0
while i<len(numbers):
    print(numbers[i])
    i=i+1
print("range")
more_numbers = range(0,5)
for number in more_numbers:    
    more_numbers.append(6)
    print (numbers)