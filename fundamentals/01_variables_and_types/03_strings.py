# Strings are sequences of characters, enclosed in single or double quotes
name = "Alice"
greeting = 'Hello'

# Triple quotes for multi-line strings
message = """This spans
multiple lines."""

# f-strings — the preferred way to embed values in strings (Python 3.6+)
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")

# STRING PREFIXES
# ---------------
# The f in f"..." is a STRING PREFIX — part of the literal syntax, NOT a
# function or variable. It must be typed directly against the opening quote.
# It changes how Python READS the literal, before any value exists.
#
#   f"..."   formatted string — enables {} interpolation
#   r"..."   raw string — backslashes stay literal:  r"\n" is 2 chars, not a newline
#   b"..."   bytes literal — a bytes object, not a str
#   rb"..."  raw bytes (prefixes can combine)
#
print(r"C:\new\table")   # C:\new\table  — raw: \n and \t are NOT special
print("C:\new\table")    # \n and \t ARE interpreted (newline + tab) — messy!
print(b"hello")          # b'hello'  — a bytes object
#
# Because the prefix is syntax (not a name), defining your own variable named
# f, r, or b does NOT affect string literals — they never collide. And you
# cannot store a prefix in a variable: prefix"text" is a SyntaxError.

# Common string operations
print(len(name))          # 5 — length
print(name.upper())       # ALICE
print(name.lower())       # alice
print("  hello  ".strip())  # "hello" — removes whitespace
print("hello".replace("l", "r"))  # herro
print("a,b,c".split(","))  # ['a', 'b', 'c']
print(",".join(["a", "b", "c"]))  # a,b,c

# join() is a string method, not a list method — the separator is in control.
# This feels backwards coming from other languages (e.g. JavaScript's array.join(","))
# but the design holds: join works on any iterable, not just lists:
print(",".join(("a", "b", "c")))          # tuple
print(",".join("abc"))                     # string → a,b,c
print(",".join(x for x in ["a","b","c"])) # generator

# Indexing and slicing — strings are zero-indexed
s = "Python"
print(s[0])    # P — first character
print(s[-1])   # n — last character
print(s[0:3])  # Pyt — characters 0, 1, 2
print(s[::2])  # Pto — every other character

# Strings are immutable — you can't change a character in place
# s[0] = "J"  # TypeError!
