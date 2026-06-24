# LIST COMPREHENSIONS — build a list in a single expression
# ---------------------------------------------------------
# A compact way to create a list from an iterable. Heavily used in Python.
#
# Syntax:  [ expression  for item in iterable ]
#
# This is one place where Python is INDENTATION-FREE — the whole thing is
# a single expression, no block/colon needed.

# The long way (loop + append)
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)              # [0, 1, 4, 9, 16]

# The comprehension way — same result, one line
squares = [x ** 2 for x in range(5)]
print(squares)              # [0, 1, 4, 9, 16]


# WITH A CONDITION (filter) — append `if` at the end
#   [ expression for item in iterable if condition ]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)               # [0, 2, 4, 6, 8]

# The expression can transform AND the condition can filter, together
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)        # [0, 4, 16, 36, 64]


# WORKS ON ANY ITERABLE, not just range
words = ["hello", "world", "python"]
lengths = [len(w) for w in words]
print(lengths)             # [5, 5, 6]

uppercased = [w.upper() for w in words]
print(uppercased)          # ['HELLO', 'WORLD', 'PYTHON']

# Filter a list of strings
long_words = [w for w in words if len(w) > 5]
print(long_words)          # ['python']


# CONDITIONAL EXPRESSION inside the output (ternary) — DIFFERENT from filtering
# Here the if/else comes BEFORE the for (it chooses the value, not filters)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)              # ['even', 'odd', 'even', 'odd', 'even']

# KEY DISTINCTION (common confusion):
#   [x for x in data if cond]            -> if at END = FILTER (drops items)
#   [a if cond else b for x in data]     -> if/else at FRONT = CHOOSE value (keeps all)
