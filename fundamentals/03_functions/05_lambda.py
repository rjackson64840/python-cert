# LAMBDA — small anonymous (unnamed) functions
# --------------------------------------------
# Syntax:  lambda parameters: expression
# The expression's value is returned automatically (no `return` keyword).
# Limited to a SINGLE expression — no statements, loops, or multiple lines.

# A lambda...
square = lambda x: x ** 2
print(square(5))            # 25

# ...is equivalent to this regular function:
def square_fn(x):
    return x ** 2
print(square_fn(5))         # 25

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 4))            # 7

# No parameters
hello = lambda: "hi"
print(hello())              # hi


# WHERE LAMBDAS SHINE: as throwaway arguments to other functions
# ---------------------------------------------------------------

# sorted() with a key function — sort by the second element
pairs = [(1, "c"), (2, "a"), (3, "b")]
print(sorted(pairs, key=lambda pair: pair[1]))   # sorts by letter
# [(2, 'a'), (3, 'b'), (1, 'c')]

# sort strings by length
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))       # ['kiwi', 'apple', 'banana']


# map() — apply a function to every item, returns an iterator
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)              # [1, 4, 9, 16]

# filter() — keep items where the function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)                # [2, 4]

# NOTE: map/filter return lazy iterators — wrap in list() to see the values.
# These three (lambda, map, filter) plus sorted() are core PCAP material.
