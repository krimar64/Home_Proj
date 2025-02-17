import time

# For-loop
start_time = time.time()
squares = []
for i in range(1000000):
    squares.append(i ** 2)
print("For-loop time:", time.time() - start_time)

# List comprehension
start_time = time.time()
squares = [i ** 2 for i in range(1000000)]
print("List comprehension time:", time.time() - start_time)