# for — iterates over any sequence (list, string, range, etc.)

# Iterating a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating a string
for char in "Python":
    print(char)

# range() — generates a sequence of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (step of 2)
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1  (counting down)
    print(i)

# enumerate() — get index and value together
for index, fruit in enumerate(fruits):
    print(index, fruit)     # 0 apple, 1 banana, 2 cherry

# zip() — iterate two sequences in parallel
names = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# break and continue work the same as in while loops
for i in range(10):
    if i == 5:
        break           # stop at 5
    if i % 2 == 0:
        continue        # skip even numbers
    print(i)            # prints 1, 3

# for / else — else runs only if no break occurred
for i in range(5):
    if i == 10:
        break
else:
    print("no break occurred")
