# bool — only two values: True and False (capitalized)
is_active = True
is_done = False

# Boolean operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Comparison operators return booleans
print(5 > 3)    # True
print(5 == 5)   # True  — equality (== not =)
print(5 != 3)   # True  — not equal
print(5 >= 5)   # True

# Truthiness — every value has a boolean interpretation
# Falsy values: 0, 0.0, "", [], {}, None, False
# Everything else is truthy
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(42))     # True
print(bool("hi"))   # True

# None — represents the absence of a value (like null in other languages)
result = None
print(result)           # None
print(type(result))     # <class 'NoneType'>

# Check for None with `is`, not ==
if result is None:
    print("No result yet")
