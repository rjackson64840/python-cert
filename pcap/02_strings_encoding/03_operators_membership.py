# STRING OPERATORS: +, *, in, and comparisons
# ============================================

# CONCATENATION with +  (BOTH operands must be str)
print("Py" + "thon")        # 'Python'
# Mixing str and int with + raises TypeError — caught live (see Module 6):
try:
    print("age: " + 25)     # str + int is not allowed
except TypeError as e:
    print("TypeError:", e)  # can only concatenate str (not "int") to str
print("age: " + str(25))    # 'age: 25'  — convert the int first

# REPLICATION with *  (str * int)
print("ab" * 3)             # 'ababab'
print("-" * 10)             # '----------'
print("x" * 0)              # ''   (zero or a negative int -> empty string, no error)

# MEMBERSHIP: in / not in  -> bool (substring test, case-SENSITIVE)
print("cat" in "concatenate")    # True
print("dog" in "concatenate")    # False
print("Cat" in "concatenate")    # False  — case matters
print("z" not in "abc")          # True
print("" in "abc")               # True   — the empty string is in every string

# COMPARISON — lexicographic, char by char, by Unicode CODE POINT
print("apple" < "banana")   # True   'a'(97) < 'b'(98)
print("Apple" < "apple")    # True   'A'(65) < 'a'(97) — uppercase sorts FIRST
print("abc" < "abd")        # True   first differing char decides
print("abc" < "abcd")       # True   a prefix is "less than" the longer string
print("abc" == "abc")       # True
print("ABC" == "abc")       # False  — case-sensitive

# Iterating a string yields its characters one at a time:
for ch in "hi":
    print(ch)               # 'h' then 'i'


# PCAP POINTS:
# - + needs str + str; mixing str and int raises TypeError — wrap with str().
# - * by 0 or a negative number gives '' (empty), never an error.
# - Comparisons use code points: every uppercase letter (65–90) is LESS than
#   every lowercase letter (97–122), so "Z" < "a" is True.
# - The empty string "" is a substring of any string.
