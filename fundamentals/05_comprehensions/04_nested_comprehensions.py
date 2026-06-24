# NESTED COMPREHENSIONS — comprehensions with multiple loops
# ----------------------------------------------------------
# Read the `for` clauses LEFT TO RIGHT, the same order you'd write nested loops.

# Two for-clauses = nested loop. Order matters!
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)
# [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]
# Equivalent to:
#   for x in range(3):
#       for y in range(2):
#           pairs.append((x, y))


# FLATTENING a list of lists — a very common use
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)                # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Read left-to-right: "for each row in matrix, for each num in row"


# BUILDING a 2D structure — a comprehension INSIDE a comprehension
grid = [[col for col in range(3)] for row in range(2)]
print(grid)                # [[0, 1, 2], [0, 1, 2]]

# Multiplication table
table = [[r * c for c in range(1, 4)] for r in range(1, 4)]
print(table)               # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# WITH A CONDITION in a nested comprehension
# Keep only even numbers while flattening
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)               # [2, 4, 6, 8]


# READABILITY WARNING:
# Nested comprehensions get hard to read quickly. If you have to pause to
# parse one, a plain nested loop is clearer. PEP 8 / Pythonic style favors
# readability over cleverness — comprehensions are a tool, not a goal.
#
# Rule of thumb: one or two for-clauses is fine; three is usually too many.
