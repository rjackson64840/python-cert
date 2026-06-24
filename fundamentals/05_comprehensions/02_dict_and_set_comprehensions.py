# DICT AND SET COMPREHENSIONS
# ---------------------------
# Same idea as list comprehensions, but with {} and different output shapes.

# DICT COMPREHENSION — produces key: value pairs
#   { key_expr: value_expr for item in iterable }
squares = {x: x ** 2 for x in range(5)}
print(squares)             # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Build a dict from two parallel lists with zip()
names = ["alice", "bob", "carol"]
scores = [90, 85, 95]
score_map = {name: score for name, score in zip(names, scores)}
print(score_map)           # {'alice': 90, 'bob': 85, 'carol': 95}

# With a filter
passing = {name: score for name, score in score_map.items() if score >= 90}
print(passing)             # {'alice': 90, 'carol': 95}

# Swap keys and values
inverted = {v: k for k, v in score_map.items()}
print(inverted)            # {90: 'alice', 85: 'bob', 95: 'carol'}


# SET COMPREHENSION — produces a set (unique values, unordered)
#   { expression for item in iterable }
unique_lengths = {len(name) for name in names}
print(unique_lengths)      # {3, 5} — alice/carol=5, bob=3; duplicates dropped

# Note: {} alone is a DICT. A set comprehension needs an expression,
# not a key:value pair. The presence of `:` is what makes it a dict.
set_comp = {x % 3 for x in range(10)}     # set comprehension -> {0, 1, 2}
dict_comp = {x: x % 3 for x in range(10)} # dict comprehension (has the colon)
print(type(set_comp))      # <class 'set'>
print(type(dict_comp))     # <class 'dict'>
