# WHY IS IT CALLED A "COMPREHENSION"?
# ===================================
# This trips people up because the word feels abstract. Here's the plain version.
#
# A comprehension describes a collection by the RULE its members follow,
# instead of BUILDING it up step by step. That describe-vs-build shift is
# the entire idea.


# Two ways to make the SAME list:

# 1. IMPERATIVE — describes HOW to build it (a process, step by step)
squares = []
for x in range(5):
    squares.append(x ** 2)
# "Start with an empty list. For each number 0 to 4, square it, and append it."

# 2. COMPREHENSION — describes WHAT it is (the result, by a rule)
squares = [x ** 2 for x in range(5)]
# "The squares of the numbers 0 to 4."

# You state what's IN the list, not HOW to assemble it.


# WHERE THE WORD COMES FROM
# -------------------------
# "comprehension" shares a root with "comprise" (Latin com- "together" +
# prehendere "to grasp") — meaning to include or contain together.
# So a comprehension is ONE expression that comprises all the items
# matching the rule. "A list comprehension" = "a list comprising everything
# that fits this description."
#
# (It also mirrors math's set-builder notation: { x² | x in 0..4 } reads
#  almost exactly like the Python. But you don't need the math to get it.)


# HOW TO EXPLAIN IT TO SOMEONE ELSE (the real test of understanding):
#
#   "A list comprehension is Python's way of DESCRIBING a list by a rule
#    instead of BUILDING it with a loop. Instead of 'make an empty list,
#    loop, and append each squared value,' you just write 'the squares of
#    0 through 4.' The word comes from the same root as 'comprise' — the
#    one expression contains all the items that fit the rule."

print(squares)   # [0, 1, 4, 9, 16]
