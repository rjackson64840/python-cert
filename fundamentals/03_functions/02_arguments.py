# WAYS TO PASS ARGUMENTS — a heavily-tested PCAP topic
# ----------------------------------------------------

def describe(name, age, city):
    print(f"{name}, {age}, from {city}")


# 1. POSITIONAL arguments — matched by position, in order
describe("Alice", 30, "NYC")


# 2. KEYWORD arguments — matched by name, order doesn't matter
describe(age=30, city="NYC", name="Alice")


# 3. MIXED — positional must come BEFORE keyword arguments
describe("Alice", city="NYC", age=30)
# describe(name="Alice", 30, "NYC")   # SyntaxError! positional after keyword


# DEFAULT PARAMETER VALUES
# Parameters can have defaults, used when no argument is given.
def power(base, exp=2):         # exp defaults to 2
    return base ** exp

print(power(5))                 # 25 — uses default exp=2
print(power(5, 3))              # 125 — overrides default

# Parameters WITH defaults must come AFTER parameters without them
# def bad(a=1, b):   # SyntaxError: non-default argument follows default


# THE MUTABLE DEFAULT ARGUMENT TRAP (classic PCAP / interview gotcha)
# Default values are evaluated ONCE when the function is defined,
# not each time it's called. A mutable default (list/dict) is SHARED
# across all calls.
def add_item(item, basket=[]):      # DON'T do this
    basket.append(item)
    return basket

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['a', 'b']  — surprise! same list reused

# The correct pattern: use None as the default, create inside
def add_item_safe(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

basket = add_item_safe("a")
print(basket)               # ['a']
print(add_item_safe("b"))   # ['b']  — fresh list each call

print(add_item_safe("c", basket))
