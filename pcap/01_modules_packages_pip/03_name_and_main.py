# __name__ AND THE __main__ IDIOM
# ===============================
# Every module has a built-in variable called __name__. Its value depends
# on HOW the file is being used:
#
#   Run directly (python 03_name_and_main.py):  __name__ == "__main__"
#   Imported by another file:                    __name__ == the module name
#
# This is one of the most important and most-tested ideas in this topic.

print("This module's __name__ is:", __name__)


def main():
    print("Running as a script")


# THE GUARD IDIOM:
# Run script logic ONLY when executed directly, not when imported.
# This lets a single file be BOTH an importable module AND a runnable script.
if __name__ == "__main__":
    main()

# WHY IT MATTERS:
# If another file does `import this_module`, you usually want its functions
# and classes available WITHOUT auto-executing the script body. The guard
# prevents those side effects on import.


# __pycache__ and .pyc FILES
# --------------------------
# The first time a module is IMPORTED, Python compiles it to bytecode and
# caches it in a __pycache__/ folder as a .pyc file (e.g. greetings.cpython-314.pyc).
# Future imports load the cached bytecode, skipping recompilation — faster startup.
# It's auto-generated: don't edit it, and add __pycache__/ to .gitignore.
# (Note: a file run DIRECTLY as a script is not cached this way — only imports are.)


# GOTCHA — leading digits in filenames:
# Our study files are named like 03_name_and_main.py. You CANNOT import these
# with `import 03_name_and_main` because identifiers can't start with a digit
# (it's a SyntaxError). That's fine for runnable scripts, but real importable
# modules should have identifier-safe names (letters/underscore first), like
# greetings.py in this same folder.
