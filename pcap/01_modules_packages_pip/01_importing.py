# IMPORTING MODULES
# =================
# A module is just a .py file containing reusable code. Python ships with a
# large standard library of modules; you bring one in with `import`.
# PCAP tests the different import FORMS and how names are qualified.


# FORM 1: import the whole module — access members as module.name
import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0
# Names stay behind the `math.` prefix — clear where they came from.


# FORM 2: from-import specific names — use them directly, no prefix
from math import pi, sqrt
print(pi)               # 3.141592653589793
print(sqrt(25))         # 5.0
# Shorter, but the names now live in YOUR namespace.


# FORM 3: import with an alias — rename on import (handy for long names)
import math as m
print(m.factorial(5))   # 120

from math import factorial as fact
print(fact(5))          # 120


# FORM 4: star import — from module import *  (DISCOURAGED)
from math import *
print(cos(0))           # 1.0
# This dumps ALL of the module's public names into your namespace at once.
# Risks: name collisions (a later import silently overwrites earlier names)
# and unclear code (where did `cos` come from?). PCAP expects you to KNOW
# this form, but real code should prefer explicit imports.


# QUALIFIED vs UNQUALIFIED names:
#   math.pi   -> qualified   (module.name)  — explicit, collision-proof
#   pi        -> unqualified (after from-import) — shorter, less traceable
#
# An import binds a name in the CURRENT module. `import math` binds `math`;
# `from math import pi` binds `pi`. Either way, the module is only loaded
# (executed) ONCE — repeat imports reuse the cached module.
