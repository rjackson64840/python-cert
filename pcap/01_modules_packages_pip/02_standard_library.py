# SELECTED STANDARD LIBRARY MODULES
# =================================
# PCAP focuses on a handful of stdlib modules. Know their common functions.


# math — mathematical functions and constants
import math
print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
print(math.sqrt(81))      # 9.0
print(math.factorial(5))  # 120
print(math.floor(3.7))    # 3  — round DOWN
print(math.ceil(3.2))     # 4  — round UP
print(math.gcd(12, 18))   # 6  — greatest common divisor
print(math.hypot(3, 4))   # 5.0 — sqrt(3**2 + 4**2)
print(math.pow(2, 10))    # 1024.0  — NOTE: returns a float; 2 ** 10 is int


# random — pseudo-random numbers
import random
print(random.random())            # float in [0.0, 1.0)
print(random.randint(1, 6))        # int in [1, 6] INCLUSIVE on both ends
print(random.randrange(0, 10, 2))  # like range(): 0,2,4,6,8
print(random.choice(["a", "b", "c"]))  # one random element

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)               # shuffles the list IN PLACE (returns None)
print(nums)
print(random.sample(range(100), 3))  # 3 UNIQUE random picks

# Seeding makes results reproducible — same seed => same sequence
random.seed(42)
print(random.randint(1, 100))      # identical every run with seed 42


# platform — information about the host machine / interpreter
import platform
print(platform.system())          # 'Windows', 'Linux', or 'Darwin' (macOS)
print(platform.python_version())  # e.g. '3.14.6'
print(platform.machine())         # e.g. 'AMD64'


# sys — interpreter state and interaction
import sys
print(sys.platform)               # 'win32', 'linux', 'darwin'
print(sys.version)                # full version string
print(sys.executable)             # path to THIS python.exe
print(sys.path[:2])               # the module search path (list of dirs)
