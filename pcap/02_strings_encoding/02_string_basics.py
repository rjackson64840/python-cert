# STRING BASICS: IMMUTABILITY, INDEXING, SLICING
# ==============================================
# A str is an IMMUTABLE, ordered sequence of characters. Immutable = once
# created it can never be changed in place; "modifying" it builds a NEW string.

s = "Python"

# len() — number of characters
print(len(s))          # 6

# INDEXING — zero-based; negative indices count from the end
print(s[0])            # 'P'   first char
print(s[5])            # 'n'   last char
print(s[-1])           # 'n'   last char (negative)
print(s[-6])           # 'P'   first char (negative)
# Indexing out of range raises IndexError — caught LIVE here so it prints
# instead of crashing (full try/except coverage is in Module 6):
try:
    print(s[6])        # index 6 is past the end (valid indices are 0–5)
except IndexError as e:
    print("IndexError:", e)        # string index out of range

# IMMUTABILITY — item assignment is not allowed; prove it with try/except:
try:
    s[0] = 'J'                     # attempt to change one character in place
except TypeError as e:
    print("TypeError:", e)         # 'str' object does not support item assignment
# To "change" a string, build a NEW one:
s2 = 'J' + s[1:]
print(s2)              # 'Jython'
print(s)               # 'Python'  — the original is untouched

# SLICING — s[start:stop:step]; stop is EXCLUSIVE (like range)
word = "certification"
print(word[0:4])       # 'cert'       indices 0,1,2,3
print(word[:4])        # 'cert'       start defaults to 0
print(word[4:])        # 'ification'  stop defaults to len(word)
print(word[:])         # 'certification'  full copy
print(word[-4:])       # 'tion'       last 4 chars
print(word[::2])       # 'criiain'    every 2nd char
print(word[::-1])      # 'noitacifitrec'  reversed!

# Slices NEVER raise IndexError — out-of-range bounds are clamped:
print(word[5:999])     # 'fication'   (clamped to the end, no error)
print(word[100:200])   # ''           (empty, still no error)


# PCAP POINTS:
# - Indexing out of range -> IndexError; slicing out of range -> clamped, no error.
# - Strings are immutable: item or slice assignment raises TypeError.
# - s[::-1] is the idiomatic way to reverse a string.
# - A slice always returns a NEW string (even s[:] is a fresh copy).