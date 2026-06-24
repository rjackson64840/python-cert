# BUILT-IN TYPES ARE JUST CLASSES
# --------------------------------
# int, str, list, dict — these are all classes defined by Python itself.
# When you write x = 42, you're instantiating the int class.
# This is why type(x) shows <class 'int'> — it's telling you the class.

x = 42
print(type(x))              # <class 'int'>
print(type(x).__name__)     # int  — just the name, no angle brackets

# Because they're classes, values have methods you can call on them
print((42).bit_length())    # 6  — int method: bits needed to represent 42
print("hello".upper())      # HELLO — str method
print([1,2,3].count(2))     # 1  — list method

# You can see all methods available on a type
print(dir(int))             # lists all int methods and attributes
print(dir(str))             # lists all str methods and attributes

# int, str, list etc. can be called directly as constructors
x = int("42")               # same as int.__init__("42") under the hood
y = str(100)
z = list("abc")             # ['a', 'b', 'c']
print(x, y, z)

# Everything inherits from object — the root class of all classes in Python
print(isinstance(42, object))       # True
print(isinstance("hello", object))  # True
print(isinstance([], object))       # True

# The class hierarchy:
print(int.__bases__)        # (<class 'object'>,)
print(bool.__bases__)       # (<class 'int'>,) — bool is a subclass of int!
print(True + True)          # 2 — because True is 1 and False is 0
