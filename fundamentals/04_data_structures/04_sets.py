# SETS — unordered, mutable, NO duplicates
# ----------------------------------------
# Written with curly braces (like dicts, but no key:value pairs).

colors = {"red", "green", "blue"}
print(len(colors))      # 3

# Duplicates are automatically removed
nums = {1, 2, 2, 3, 3, 3}
print(nums)             # {1, 2, 3}

# A common use: remove duplicates from a list
items = [1, 1, 2, 3, 3, 3, 4]
print(set(items))       # {1, 2, 3, 4}
print(list(set(items))) # back to a list (order not guaranteed)

# CREATING AN EMPTY SET — must use set(), NOT {} (that's an empty dict!)
empty_set = set()
empty_dict = {}
print(type(empty_set))  # <class 'set'>
print(type(empty_dict)) # <class 'dict'>  <-- classic PCAP trap

# ADDING / REMOVING
colors.add("yellow")
colors.discard("red")   # remove if present — no error if missing
colors.remove("blue")   # remove — raises KeyError if missing
print(colors)

# MEMBERSHIP — sets are very fast for "is x in here?" checks
print("green" in colors)    # True

# Sets are UNORDERED — no indexing
# colors[0]   # TypeError: 'set' object is not subscriptable


# SET OPERATIONS (math set theory — a PCAP favorite)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union — all elements: {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection — in both: {3, 4}
print(a - b)    # difference — in a but not b: {1, 2}
print(a ^ b)    # symmetric difference — in one but not both: {1, 2, 5, 6}

# Method forms do the same thing
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Subset / superset
print({1, 2}.issubset(a))     # True
print(a.issuperset({1, 2}))   # True


# FROZENSET — an immutable set (can be a dict key or set member)
fs = frozenset([1, 2, 3])
# fs.add(4)    # AttributeError — immutable
print(fs)       # frozenset({1, 2, 3})
