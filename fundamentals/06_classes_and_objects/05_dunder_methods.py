# DUNDER METHODS (DOUBLE UNDERSCORE) — also called "magic" or "special" methods
# -----------------------------------------------------------------------------
# Dunder = "double underscore". Methods named __like_this__.
# They are hooks Python calls FOR you — you rarely call them directly.
# Python's syntax and built-in functions are sugar over dunder methods.
#
# When you write:        Python actually runs:
#   a + b                  a.__add__(b)
#   a == b                 a.__eq__(b)
#   len(a)                 a.__len__()
#   str(a)                 a.__str__()
#   a[i]                   a.__getitem__(i)
#   x in a                 a.__contains__(x)
#   for x in a             a.__iter__()

# Proof: the operator IS the dunder
print(5 + 3)            # 8
print((5).__add__(3))   # 8 — identical

print(len([1, 2, 3]))       # 3
print([1, 2, 3].__len__())  # 3 — identical


# WHY BUILT-IN TYPES HAVE SO MANY DUNDERS
# ----------------------------------------
# Every operation you can do to an int, str, or list is backed by a dunder
# on that class. That's why dir(int) is mostly __names__ — the built-in
# types implement the full set of operations. The few non-dunder names
# (bit_length, to_bytes, ...) are the "ordinary" methods.


# DEFINING DUNDERS MAKES YOUR CLASS BEHAVE LIKE A BUILT-IN
# --------------------------------------------------------
# This is called operator overloading. Define __add__ and + works on your
# objects. Define __len__ and len() works. Define __str__ and print() is readable.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):       # enables  v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):        # enables  v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):              # enables  print(v) / str(v)
        return f"({self.x}, {self.y})"

    def __repr__(self):             # enables  repr(v) / REPL display
        return f"Vector({self.x}, {self.y})"

    def __len__(self):              # enables  len(v)
        return 2


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)          # (4, 6)      — uses __add__ then __str__
print(v1 == Vector(1, 2))  # True     — uses __eq__
print(len(v1))          # 2           — uses __len__
print(repr(v1))         # Vector(1, 2) — uses __repr__


# THE MOST COMMON DUNDERS TO KNOW
# -------------------------------
#   __init__     initializer (runs when object is created)
#   __str__      human-friendly string — used by print() and str()
#   __repr__     unambiguous developer string — used by repr() and the REPL
#   __len__      len(obj)
#   __eq__       obj == other
#   __add__      obj + other
#   __getitem__  obj[key]
#   __contains__ item in obj
#   __iter__     for x in obj
#
# __str__ vs __repr__:
#   __str__  is for end users  ("nice to read")
#   __repr__ is for developers ("unambiguous, ideally reconstructs the object")
#   If you only define one, define __repr__ — it's the fallback for both.
