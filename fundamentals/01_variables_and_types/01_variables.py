# Variables are created by assignment — no declaration or type keyword needed
name = "Alice"
age = 30
height = 5.7
is_student = True

print(name, age, height, is_student)

# Variables are dynamically typed — the type is determined by the value
x = 10
print(type(x))   # <class 'int'>
x = "hello"
print(type(x))   # <class 'str'>

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

# Swap without a temp variable
a, b = b, a
print(a, b)

# Constants — Python has no true constants, but ALL_CAPS signals "don't change this"
MAX_RETRIES = 3
PI = 3.14159
