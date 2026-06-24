# IMPORTING YOUR OWN MODULE
# =========================
# greetings.py sits in this same folder, so we import it by its filename
# (without the .py). Python finds it because the script's own directory is
# on the module search path (sys.path).

import greetings
print(greetings.greet("Alice"))    # Hello, Alice!
print(greetings.GREETING)          # Hello  — module variables are importable too


# Import specific names directly
from greetings import farewell
print(farewell("Bob"))             # Goodbye, Bob.


# Import with an alias
import greetings as g
print(g.greet("Carol"))            # Hello, Carol!


# KEY POINT: when this file runs and imports greetings, the
# `if __name__ == "__main__":` block INSIDE greetings.py does NOT execute.
# That block only runs when greetings.py is the file being run directly.
# Here greetings.__name__ is "greetings", so its test code stays dormant.
print("greetings.__name__ is:", greetings.__name__)

# Inspect what a module contains:
print(dir(greetings))              # lists greetings' names (GREETING, greet, ...)
