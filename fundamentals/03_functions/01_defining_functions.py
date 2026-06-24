# DEFINING FUNCTIONS
# ------------------
# A function is a reusable, named block of code. Define with `def`.

def greet():
    print("Hello!")

greet()         # call the function — prints Hello!
greet()         # reusable — call as many times as you like


# PARAMETERS AND ARGUMENTS
# parameter = the variable in the definition (name)
# argument  = the actual value passed in the call ("Alice")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")       # argument "Alice" binds to parameter name


# RETURN VALUES
# `return` sends a value back to the caller and ends the function immediately.
def add(a, b):
    return a + b

result = add(3, 4)
print(result)               # 7

# A function with no return statement returns None automatically
def no_return():
    x = 5                   # computes but returns nothing

print(no_return())          # None

# return with no value also gives None, and exits the function early
def check(n):
    if n < 0:
        return              # early exit, returns None
    print("positive")

check(-1)                   # prints nothing
check(5)                    # positive


# A function can return multiple values (actually returns one tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5])
print(low, high)            # 1 5
print(min_max([3, 1, 4]))   # (1, 4) — it's a tuple
