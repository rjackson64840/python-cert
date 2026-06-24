# METHODS THAT RETURN VALUES
# --------------------------
# So far our methods just printed output. More often, a method computes
# something and RETURNS it with the `return` keyword, so the caller can
# use the result.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Returns a number — the caller decides what to do with it
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # Returns a bool
    def is_square(self):
        return self.width == self.height

    # A method can use the result of another method
    def describe(self):
        return f"{self.width}x{self.height}, area={self.area()}"


rect = Rectangle(4, 6)

# The returned values can be stored, printed, or used in expressions
a = rect.area()
print(a)                    # 24
print(rect.perimeter())     # 20
print(rect.is_square())     # False
print(rect.describe())      # 4x6, area=24

# Because area() returns a value, you can use it directly in math
total = rect.area() + 10
print(total)                # 34

# A method with no explicit return gives back None
class Example:
    def do_nothing(self):
        pass                # no return statement

print(Example().do_nothing())   # None


# OPTIONAL — TYPE HINTS FOR "VALUE OR NONE"
# -----------------------------------------
# Type hints document what types a function expects and returns. They are
# optional in Python (not enforced at runtime) but improve readability and
# let IDEs/tools catch mistakes.
#
# Optional[X] means "either an X or None" — perfect for methods that may
# not find/return a value. It comes from the typing module.

from typing import Optional

class Inventory:
    def __init__(self):
        self.items = {"apple": 3, "banana": 5}

    # Return type hint: Optional[int] — returns the count, or None if missing
    def get_count(self, name: str) -> Optional[int]:
        if name in self.items:
            return self.items[name]
        return None     # explicitly returns None when not found


inv = Inventory()
print(inv.get_count("apple"))   # 3
print(inv.get_count("cherry"))  # None

# The caller should handle the None case
count = inv.get_count("cherry")
if count is None:
    print("Item not in inventory")
else:
    print(f"We have {count}")

# NOTE: In Python 3.10+ you can write `int | None` instead of Optional[int]:
#   def get_count(self, name: str) -> int | None:
# Both mean the same thing. Optional is the older, still-common style.
