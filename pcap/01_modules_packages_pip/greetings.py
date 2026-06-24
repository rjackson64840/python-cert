# greetings.py — A CUSTOM MODULE
# ==============================
# This is just a plain .py file with reusable code. Because its name is a
# valid identifier (starts with a letter), other files can import it with
# `import greetings`. See 04_creating_modules.py for the importing side.

GREETING = "Hello"      # a module-level variable (importable)


def greet(name):
    return f"{GREETING}, {name}!"


def farewell(name):
    return f"Goodbye, {name}."


# This block runs ONLY if greetings.py is executed directly
# (python greetings.py). It does NOT run when greetings is imported,
# because then __name__ is "greetings", not "__main__".
if __name__ == "__main__":
    print("Testing the greetings module directly")
    print(greet("World"))
    print(farewell("World"))
