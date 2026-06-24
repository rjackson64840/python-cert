# TUPLES — ordered, IMMUTABLE, allow duplicates
# ---------------------------------------------
# Like lists, but cannot be changed after creation. Written with parentheses.

point = (3, 4)
print(point[0])     # 3 — indexing works like lists
print(len(point))   # 2

# Immutable — these all raise TypeError:
# point[0] = 5        # TypeError
# point.append(5)     # AttributeError — no append method

# Why use tuples?
#  - Signals "this shouldn't change" (coordinates, RGB colors, records)
#  - Slightly faster and smaller than lists
#  - Can be used as DICT KEYS and SET MEMBERS (lists cannot — they're mutable)

coords = {(0, 0): "origin", (1, 2): "point A"}   # tuple keys — valid
print(coords[(0, 0)])   # origin


# CREATING TUPLES — the comma makes the tuple, not the parentheses!
t1 = (1, 2, 3)
t2 = 1, 2, 3            # also a tuple — parentheses optional
print(t2)               # (1, 2, 3)

# A SINGLE-element tuple REQUIRES a trailing comma (classic PCAP trap)
not_a_tuple = (5)       # this is just the int 5
real_tuple = (5,)       # THIS is a one-element tuple
print(type(not_a_tuple))  # <class 'int'>
print(type(real_tuple))   # <class 'tuple'>

# Empty tuple
empty = ()
print(type(empty))      # <class 'tuple'>


# TUPLE UNPACKING — assign elements to variables in one step
x, y = (3, 4)
print(x, y)             # 3 4

# Used everywhere — e.g. swapping (it's really tuple packing/unpacking)
a, b = 1, 2
a, b = b, a
print(a, b)             # 2 1

# Extended unpacking with * (collects the rest into a list)
first, *rest = (1, 2, 3, 4)
print(first, rest)      # 1 [2, 3, 4]
*init, last = (1, 2, 3, 4)
print(init, last)       # [1, 2, 3] 4


# NOTE: a tuple is immutable, but if it CONTAINS a mutable object,
# that object can still change (the tuple's references are fixed, not the data)
nested = (1, [2, 3])
nested[1].append(4)     # allowed — modifying the inner list
print(nested)           # (1, [2, 3, 4])
