# shapes/__init__.py
# ==================
# The presence of this file makes the `shapes/` directory a PACKAGE — a
# directory of related modules importable with dotted names (shapes.circle).
#
# __init__.py runs ONCE, the first time the package (or any submodule) is
# imported. It can be empty, or it can set up package-level names.
#
# (Since Python 3.3, "namespace packages" can work without __init__.py, but
#  including it is the standard, explicit, and PCAP-expected approach.)

print("[shapes package initialized]")

# Optional: __all__ controls what `from shapes import *` brings in.
__all__ = ["circle", "rectangle"]
