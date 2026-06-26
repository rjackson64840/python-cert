# The presence of this file makes `utils/` a PACKAGE — a folder you can import
# from. It runs exactly ONCE, the first time anything in the package is imported
# (here, triggered by `from utils import text` in 04_creating_modules.py).
# Packages use __init__.py for initialization or to curate what they expose.
print("[utils/__init__.py ran — package initialized]")
