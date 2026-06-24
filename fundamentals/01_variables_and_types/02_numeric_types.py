# Python has three numeric types: int, float, complex

# int — whole numbers, no size limit
x = 42
big = 1_000_000    # underscores allowed for readability
negative = -7

# float — decimal numbers (64-bit double precision)
pi = 3.14159
scientific = 1.5e3   # 1500.0

# complex — real + imaginary (rarely needed outside math/science)
z = 3 + 4j
print(z.real, z.imag)   # 3.0  4.0

# Arithmetic operators
print(10 + 3)   # 13  — addition
print(10 - 3)   # 7   — subtraction
print(10 * 3)   # 30  — multiplication
print(10 / 3)   # 3.333... — true division (always returns float)
print(10 // 3)  # 3   — floor division (integer result)
print(10 % 3)   # 1   — modulus (remainder)
print(10 ** 3)  # 1000 — exponentiation

# int / int always produces a float in Python 3
print(type(10 / 2))   # <class 'float'>  — result is 5.0, not 5

# Useful built-in functions
print(abs(-5))       # 5
print(round(3.7))    # 4
print(round(3.14159, 2))  # 3.14
print(max(1, 5, 3))  # 5
print(min(1, 5, 3))  # 1
