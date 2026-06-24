# PACKAGES — directories of related modules
# =========================================
# A package is a folder containing an __init__.py plus one or more module
# files. You import submodules with DOTTED names: package.module
#
# Folder layout (in this directory):
#   shapes/
#     __init__.py     <- makes 'shapes' a package
#     circle.py       <- submodule
#     rectangle.py    <- submodule
#
# Watch the console: "[shapes package initialized]" prints exactly ONCE,
# the first time anything from shapes is imported — that's __init__.py running.


# Import a whole submodule — refer to members as package.module.name
import shapes.circle
print(shapes.circle.area(5))            # 78.539...  (qualified name)


# Import specific names FROM a submodule
from shapes.rectangle import area, perimeter
print(area(3, 4))                       # 12
print(perimeter(3, 4))                  # 14


# Import a submodule with an alias
import shapes.circle as circ
print(circ.circumference(1))            # 6.283...


# THE TWO `area` FUNCTIONS:
# shapes.circle.area and shapes.rectangle.area are DIFFERENT functions in
# different modules. The dotted namespace keeps them cleanly separated, so
# there's no collision even though they share a name. This is exactly the
# point of packages/namespaces — recall the Zen of Python:
#   "Namespaces are one honking great idea -- let's do more of those!"
print(shapes.circle.area(2))            # circle area  -> 12.566...
print(area(2, 3))                       # rectangle area (imported above) -> 6
