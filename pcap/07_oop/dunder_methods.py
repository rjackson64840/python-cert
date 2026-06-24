# =============================================================================
# DUNDER / SPECIAL / MAGIC METHODS — PCAP DEPTH
# =============================================================================
# This builds on fundamentals/06_classes_and_objects/05_dunder_methods.py.
# PCAP tests these heavily: it shows a class with one or more dunders and asks
# what an expression evaluates to. Know what each one hooks into and the order
# Python tries them.


# -----------------------------------------------------------------------------
# 1. __init__ vs __new__ vs __del__  (object lifecycle)
# -----------------------------------------------------------------------------
class Lifecycle:
    def __new__(cls):           # 1st: actually CREATES the object (rarely overridden)
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):         # 2nd: INITIALIZES the already-created object
        print("__init__ called")

    def __del__(self):          # called when the object is garbage collected
        print("__del__ called")

obj = Lifecycle()               # prints __new__ then __init__
del obj                         # prints __del__


# -----------------------------------------------------------------------------
# 2. __str__ vs __repr__  (a classic PCAP distinction)
# -----------------------------------------------------------------------------
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):          # str() / print() — end-user friendly
        return f"{self.celsius}°C"

    def __repr__(self):         # repr() / REPL / containers — developer view
        return f"Temperature({self.celsius})"

t = Temperature(20)
print(str(t))    # 20°C
print(repr(t))   # Temperature(20)

# KEY EXAM POINT: containers always use __repr__ of their elements, not __str__
print([t])       # [Temperature(20)]  — NOT [20°C]

# If __str__ is missing, Python falls back to __repr__.
# If __repr__ is missing too, you get the default <__main__.X object at 0x...>.


# -----------------------------------------------------------------------------
# 3. Arithmetic dunders and the REFLECTED (right-hand) variants
# -----------------------------------------------------------------------------
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):       # called for  Money + x
        print("__add__")
        return Money(self.amount + other)

    def __radd__(self, other):      # called for  x + Money  when x doesn't know how
        print("__radd__")
        return Money(self.amount + other)

    def __repr__(self):
        return f"Money({self.amount})"

m = Money(100)
print(m + 50)       # __add__  -> Money(150)
print(50 + m)       # __radd__ -> Money(150)
                    # int.__add__(50, m) returns NotImplemented, so Python
                    # then tries m.__radd__(50). This fallback is why sum()
                    # and 0 + obj work on custom numeric types.


# -----------------------------------------------------------------------------
# 4. Comparison dunders
# -----------------------------------------------------------------------------
class Version:
    def __init__(self, major):
        self.major = major

    def __eq__(self, other):
        return self.major == other.major

    def __lt__(self, other):
        return self.major < other.major

    # Defining __eq__ makes the object UNHASHABLE unless you also define __hash__.
    # (Can't be used as a dict key or set member.) This is a common PCAP trap.
    def __hash__(self):
        return hash(self.major)

print(Version(2) < Version(3))   # True  — __lt__
print(Version(2) == Version(2))  # True  — __eq__
# Python can derive >, <=, >= from < and == automatically only if you use
# the functools.total_ordering decorator; otherwise define each one you need.


# -----------------------------------------------------------------------------
# 5. Container protocol: __len__, __getitem__, __setitem__, __contains__
# -----------------------------------------------------------------------------
class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):                  # len(playlist)
        return len(self.songs)

    def __getitem__(self, index):       # playlist[i]  AND enables iteration!
        return self.songs[index]

    def __setitem__(self, index, value):  # playlist[i] = value
        self.songs[index] = value

    def __contains__(self, item):       # item in playlist
        return item in self.songs

p = Playlist()
p.songs = ["a", "b", "c"]
print(len(p))           # 3
print(p[1])             # b
print("a" in p)         # True
for song in p:          # works via __getitem__ even without __iter__
    print(song)         # a, b, c  — Python calls p[0], p[1], ... until IndexError


# -----------------------------------------------------------------------------
# 6. __call__  — make an instance callable like a function
# -----------------------------------------------------------------------------
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):              # enables  instance(x)
        return x * self.factor

double = Multiplier(2)
print(double(10))       # 20  — the object is called like a function
print(callable(double)) # True


# -----------------------------------------------------------------------------
# 7. NotImplemented vs NotImplementedError  (a subtle PCAP gotcha)
# -----------------------------------------------------------------------------
# NotImplemented      — a special VALUE returned by a dunder to say "I can't
#                       handle this; Python, try the other operand's reflected
#                       method." Do NOT raise it.
# NotImplementedError — an EXCEPTION you raise in an abstract method that a
#                       subclass is required to override.
#
# Mixing these up is a classic trick question.


# -----------------------------------------------------------------------------
# 8. Name mangling: __private (leading dunder, NO trailing)
# -----------------------------------------------------------------------------
# Different feature from special methods. A leading-double-underscore name
# (no trailing) is "mangled" to _ClassName__name to avoid subclass collisions.
class Account:
    def __init__(self):
        self.__balance = 100        # becomes _Account__balance

a = Account()
# print(a.__balance)               # AttributeError
print(a._Account__balance)          # 100 — mangled name (not truly private)
# Trailing dunders (__like_this__) are NEVER mangled — reserved for Python.
