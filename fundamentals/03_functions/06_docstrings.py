# DOCSTRINGS — documentation built into a function
# ------------------------------------------------
# A string literal as the FIRST line of a function body becomes its docstring.
# Accessible at runtime via the __doc__ attribute and the help() function.

def calculate_area(width, height):
    """Return the area of a rectangle.

    Args:
        width:  the rectangle's width
        height: the rectangle's height

    Returns:
        The area (width * height).
    """
    return width * height


# Access the docstring
print(calculate_area.__doc__)

# help() formats it nicely (great in the REPL)
help(calculate_area)


# Single-line docstrings are fine for simple functions
def double(x):
    """Return x multiplied by 2."""
    return x * 2

print(double.__doc__)       # Return x multiplied by 2.


# Docstrings vs comments:
#   # comment      — for developers reading the source; ignored at runtime
#   """docstring""" — part of the object; available at runtime via __doc__
#
# Docstrings also work on modules (first line of a .py file) and classes
# (first line after the class statement) — same mechanism, same __doc__.
