# Explicit type conversion (casting) using built-in functions
print(int("42"))       # 42   — string to int
print(float("3.14"))   # 3.14 — string to float
print(str(100))        # "100" — int to string
print(bool(1))         # True
print(int(True))       # 1
print(int(False))      # 0

# int() truncates floats — it does not round
print(int(3.9))   # 3

# Conversion failures raise exceptions
# int("hello")   # ValueError: invalid literal for int()
# int("3.14")    # ValueError: int() can't convert a float string directly

# float first, then int:
print(int(float("3.14")))   # 3

# type() tells you what type a value is
x = 42
print(type(x))            # <class 'int'>
print(type(x) == int)     # True

# isinstance() is preferred for type checks — works with inheritance
print(isinstance(x, int))         # True
print(isinstance(x, (int, float))) # True — checks against multiple types
