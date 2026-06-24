# VARIABLE SCOPE — where a variable is visible
# --------------------------------------------
# PCAP tests this with the LEGB rule:
#   Local     — names assigned inside the current function
#   Enclosing — names in any enclosing function (nested functions)
#   Global    — names at the top level of the module
#   Built-in  — names preloaded by Python (print, len, range, ...)
# Python searches in that order: L -> E -> G -> B

x = "global"

def show():
    print(x)        # no local x, so Python finds the global one

show()              # global


# Assigning inside a function creates a NEW local variable by default
def local_assign():
    x = "local"     # creates a local x, does NOT change the global
    print(x)        # local

local_assign()
print(x)            # global — unchanged


# READING a global is fine; REASSIGNING needs the `global` keyword
counter = 0

def increment():
    global counter  # declares we mean the module-level counter
    counter += 1

increment()
increment()
print(counter)      # 2


# A common trap: reading then assigning the same name without `global`
def broken():
    # print(counter)   # UnboundLocalError! Python sees the assignment below
    counter = 5         # and treats counter as local for the WHOLE function
    print(counter)

broken()                # 5 (the local one)


# ENCLOSING scope and `nonlocal` (for nested functions)
def outer():
    msg = "outer"
    def inner():
        nonlocal msg    # refers to outer's msg, not a new local
        msg = "changed by inner"
    inner()
    print(msg)          # changed by inner

outer()

# global   -> reach the module level
# nonlocal -> reach the nearest enclosing function (not the global)
