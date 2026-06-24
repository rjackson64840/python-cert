# DICTIONARIES — key-value pairs, mutable, keys unique
# ----------------------------------------------------
# Written with curly braces and key: value pairs.
# Since Python 3.7, dicts preserve INSERTION ORDER.

person = {"name": "Alice", "age": 30, "city": "NYC"}

# ACCESSING values
print(person["name"])       # Alice
# print(person["job"])      # KeyError — missing key raises an exception

# .get() avoids KeyError — returns None (or a default) if missing
print(person.get("job"))            # None
print(person.get("job", "unknown")) # unknown — supply a default

# ADDING / UPDATING (same syntax — assignment)
person["job"] = "engineer"  # add a new key
person["age"] = 31          # update an existing key
print(person)

# REMOVING
del person["city"]          # remove by key
job = person.pop("job")     # remove & return the value
print(job)                  # engineer
print(person)

# CHECKING membership — tests KEYS, not values
print("name" in person)     # True
print("Alice" in person)    # False — Alice is a value, not a key

# ITERATING
for key in person:                  # iterates KEYS by default
    print(key, "->", person[key])

for key, value in person.items():   # both at once — common pattern
    print(f"{key}: {value}")

print(list(person.keys()))      # ['name', 'age']
print(list(person.values()))    # ['Alice', 31]


# KEYS must be IMMUTABLE (hashable): str, int, float, tuple, bool
# VALUES can be anything
valid = {1: "int key", "s": "str key", (1, 2): "tuple key"}
# invalid = {[1, 2]: "x"}   # TypeError: unhashable type: 'list'


# USEFUL patterns
scores = {"alice": 90, "bob": 85}

# update() merges another dict in
scores.update({"carol": 95, "bob": 88})
print(scores)   # bob updated to 88, carol added

# setdefault — get a key, inserting a default if absent
scores.setdefault("dave", 0)
print(scores["dave"])   # 0

# Dict from pairs — each item must be a 2-element (key, value) pair
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))      # {'a': 1, 'b': 2}

# RESHAPING data into a dict
# dict() requires EXACTLY 2 elements per item. Longer tuples fail:
trips = [(1, 2, 3), (4, 5, 6)]
# print(dict(trips))    # ValueError: ... element #0 has length 3; 2 is required

# Reshape each 3-tuple into (key, value) where value is the rest:
#   t[0]  -> first element  -> the key
#   t[1:] -> slice from index 1 -> the value (slicing a tuple returns a tuple)
print(dict((t[0], t[1:]) for t in trips))    # {1: (2, 3), 4: (5, 6)}

# Unpacking alternative — but *rest collects into a LIST, not a tuple:
print(dict((first, rest) for first, *rest in trips))  # {1: [2, 3], 4: [5, 6]}
