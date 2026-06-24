# GENERATOR EXPRESSIONS — lazy comprehensions
# -------------------------------------------
# Same syntax as a list comprehension but with PARENTHESES instead of brackets.
# Produces a GENERATOR: values are computed ONE AT A TIME, on demand,
# instead of building the whole list in memory at once.

# List comprehension — builds the entire list immediately
list_comp = [x ** 2 for x in range(5)]
print(list_comp)           # [0, 1, 4, 9, 16]

# Generator expression — produces a generator object, nothing computed yet
gen = (x ** 2 for x in range(5))
print(gen)                 # <generator object ...>

# Consume it by iterating
for value in gen:
    print(value)           # 0 1 4 9 16 (one at a time)

# A generator is EXHAUSTED after one pass — iterating again yields nothing
print(list(gen))           # [] — already consumed above


# WHY USE GENERATORS? Memory efficiency for large/infinite sequences.
# This never builds a billion-element list — it streams values:
total = sum(x for x in range(1_000_000))   # low memory
print(total)               # 499999500000

# When a generator expression is the SOLE argument to a function,
# you can drop the extra parentheses:
print(sum(x ** 2 for x in range(5)))       # 30  — no double parens needed
print(max(len(w) for w in ["a", "bb", "ccc"]))  # 3


# LIST vs GENERATOR — when to use which:
#   list comprehension []  -> you need the whole list (indexing, reuse, len)
#   generator () -> you iterate once, want low memory, or feed sum/max/any/all

# any() / all() pair beautifully with generators (short-circuit evaluation)
nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))   # True  — all even
print(any(n > 5 for n in nums))        # True  — at least one > 5
