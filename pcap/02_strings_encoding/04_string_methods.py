# COMMON STRING METHODS
# =====================
# Strings are immutable, so EVERY method returns a NEW string (or a value) —
# none of them change the original in place.

s = "Hello, World"

# CASE
print(s.upper())                  # 'HELLO, WORLD'
print(s.lower())                  # 'hello, world'
print(s.swapcase())               # 'hELLO, wORLD'
print("hello world".title())      # 'Hello World'  — capitalize EACH word
print("hello world".capitalize()) # 'Hello world'  — only the FIRST char

# SEARCHING
print(s.find("o"))          # 4    index of first match, or -1 if absent
print(s.find("z"))          # -1   NOT found -> -1 (no error)
print(s.index("o"))         # 4    like find(), but RAISES ValueError if absent
print(s.count("o"))         # 2    non-overlapping occurrences
print(s.startswith("Hell")) # True
print(s.endswith("!"))      # False

# STRIPPING whitespace (or a given set of chars)
print("   spaced   ".strip())     # 'spaced'
print("xxhixx".strip("x"))        # 'hi'
print("   left".lstrip())         # 'left'
print("right   ".rstrip())        # 'right'

# REPLACE (every occurrence)
print("a-b-c".replace("-", "+"))  # 'a+b+c'

# SPLIT / JOIN  (an inverse pair)
print("a,b,c".split(","))         # ['a', 'b', 'c']
print("a b  c".split())           # ['a', 'b', 'c']  no arg -> split on ANY whitespace run
print("-".join(["a", "b", "c"]))  # 'a-b-c'  join() is called on the SEPARATOR

# is* TESTS  -> bool
print("abc123".isalnum())   # True
print("abc".isalpha())      # True
print("123".isdigit())      # True
print("   ".isspace())      # True
print("Hello".islower())    # False
print("HELLO".isupper())    # True

# PADDING
print("5".zfill(3))         # '005'    zero-pad to a width
print("hi".center(6, "*"))  # '**hi**'


# PCAP POINTS:
# - find() returns -1 when absent; index() RAISES ValueError. (Same for rfind/rindex.)
# - split() with NO argument splits on runs of whitespace and drops empty pieces;
#   split(sep) splits on each sep and CAN produce empty strings (e.g. "a,,b".split(",")).
# - join() is called on the separator string, and every item must be a str.
# - The is* methods return False for an EMPTY string.
