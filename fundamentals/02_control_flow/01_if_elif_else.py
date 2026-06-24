# if / elif / else — conditional execution
# Python uses indentation (4 spaces) to define blocks, not braces

age = 20

if age < 13:
    print("child")
elif age < 18:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("senior")

# Conditions can use: ==  !=  <  >  <=  >=  and  or  not  in  is
x = 10
if x > 5 and x < 20:
    print("x is between 5 and 20")

# Python allows chained comparisons (unlike most languages)
if 5 < x < 20:
    print("same result, more readable")

# in operator — check membership
name = "Alice"
if name in ["Alice", "Bob", "Carol"]:
    print("known user")

# One-liner (ternary) — use sparingly, only when it's genuinely clearer
label = "even" if x % 2 == 0 else "odd"
print(label)
