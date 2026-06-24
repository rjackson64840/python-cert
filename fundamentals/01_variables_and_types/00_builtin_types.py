# EVERYTHING IN PYTHON IS AN OBJECT
# ----------------------------------
# When you call type(x), you see output like <class 'int'>.
# The word "class" is the key — in Python, every type is a class,
# and every value is an instance (object) of that class.
#
# This is different from languages like C or Java where int, float, etc.
# are primitive types separate from objects. In Python there are no
# primitives — even the number 42 is a full object with methods.
#
# You can verify this:
print(type(42))         # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>


# BUILT-IN TYPES
# --------------
# Python comes with these types out of the box — no imports needed.

# NUMERIC
x_int   = 42            # int   — whole numbers, unlimited size
x_float = 3.14          # float — decimal numbers (64-bit double precision)
x_complex = 3 + 4j      # complex — real + imaginary (scientific/math use)
x_bool  = True          # bool  — True or False (subclass of int: True==1, False==0)

# TEXT
x_str   = "hello"       # str   — immutable sequence of Unicode characters

# SEQUENCES (ordered collections)
x_list  = [1, 2, 3]     # list  — mutable, ordered, allows duplicates
x_tuple = (1, 2, 3)     # tuple — immutable, ordered, allows duplicates
x_range = range(5)      # range — immutable sequence of numbers, memory efficient

# MAPPINGS (key-value pairs)
x_dict  = {"a": 1}      # dict  — mutable, keys must be unique

# SETS (unordered, no duplicates)
x_set       = {1, 2, 3} # set       — mutable, unordered, no duplicates
x_frozenset = frozenset({1, 2, 3})  # frozenset — immutable version of set

# BINARY
x_bytes     = b"hello"  # bytes     — immutable sequence of bytes
x_bytearray = bytearray(b"hello")  # bytearray — mutable sequence of bytes

# NULL
x_none  = None           # NoneType — represents absence of a value

# Print them all
types = [x_int, x_float, x_complex, x_bool, x_str, x_list, x_tuple,
         x_range, x_dict, x_set, x_frozenset, x_bytes, x_bytearray, x_none]
for val in types:
    print(f"{str(type(val)):<25} {repr(val)}")


# WHAT DOES <class 'int'> MEAN?
# -----------------------------
# The angle brackets < > indicate this is Python's string representation
# of a type object. `type(x)` doesn't return a string — it returns the
# actual class itself. You can use it directly:
print(type(42) == int)        # True
print(type(42) is int)        # True — `is` checks identity, preferred for types
print(isinstance(42, int))    # True — preferred way to check type (works with
                               #        inheritance, covered in the OOP section)
