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


# ===========================================================================
# DEMO 1: see the module search path (sys.path) for yourself
# ===========================================================================
# Python searches these directories IN ORDER and imports the FIRST match.
# Index 0 is THIS script's own directory — which is exactly why `import
# greetings` (a file sitting right next to this script) succeeds.
import sys
print("\n--- sys.path (search order) ---")
for i, path in enumerate(sys.path):
    print(f"{i}: {path or '(current dir)'}")


# ===========================================================================
# DEMO 2 (CASE A): importing a module from a SUBFOLDER package
# ===========================================================================
# utils/text.py is NOT next to this script — it lives inside the utils/ folder.
# A bare `import text` would FAIL. The folder is importable because it is a
# PACKAGE (it contains __init__.py), so you reach modules THROUGH the package.
#
# Why this works: utils/ sits at sys.path[0] (next to this script). Python finds
# the `utils` package there, then looks INSIDE it for `text`. Only the package's
# PARENT needs to be on sys.path — not the package folder itself.
from utils import text             # import the `text` module out of the `utils` package
print("\n--- utils package demo ---")
print(text.shout("hello"))         # HELLO!
print(text.BANNER)                 # module variable, reached as utils.text.BANNER

import utils.text as t             # the fully-qualified name works too
print(t.shout("world"))            # WORLD!
