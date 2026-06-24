# *args AND **kwargs — variable numbers of arguments
# ---------------------------------------------------

# *args — collects extra POSITIONAL arguments into a TUPLE
def total(*args):
    print(args)             # args is a tuple
    return sum(args)

print(total(1, 2, 3))       # (1, 2, 3) then 6
print(total(1, 2, 3, 4, 5)) # (1, 2, 3, 4, 5) then 15
print(total())              # () then 0


# **kwargs — collects extra KEYWORD arguments into a DICT
def show_info(**kwargs):
    print(kwargs)           # kwargs is a dict
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

show_info(name="Alice", age=30)
# {'name': 'Alice', 'age': 30}


# COMBINING — order must be: normal, *args, **kwargs
def kitchen_sink(first, *args, **kwargs):
    print("first:", first)
    print("args:", args)
    print("kwargs:", kwargs)

kitchen_sink(1, 2, 3, x=10, y=20)
# first: 1
# args: (2, 3)
# kwargs: {'x': 10, 'y': 20}


# UNPACKING — the * and ** also work at the CALL site (reverse direction)
def point(x, y, z):
    print(x, y, z)

coords = [1, 2, 3]
point(*coords)              # unpacks list into positional args -> 1 2 3

data = {"x": 1, "y": 2, "z": 3}
point(**data)               # unpacks dict into keyword args -> 1 2 3

# The names *args / **kwargs are convention only — the * and ** are what matter.
# You could write *items / **options, but stick to args/kwargs for readability.
