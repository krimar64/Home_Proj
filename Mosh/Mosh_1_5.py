#Lists
names= ["John","Bob","Sam"]
print(names[0:3])
names[0]="Sam"
print(names)

#List Methods
numbers=[1,2,3,4,5]
print("First")
print(numbers)
numbers.append(6)
print("after append")
print(numbers)
numbers.insert(6,9)
print("after insert")
print(numbers)
numbers.remove(4)
numbers.remove(5)
print("after remove")
print(numbers)

#Is the number in the list?
print(9 in numbers)
#How many items?
print(len(numbers))
