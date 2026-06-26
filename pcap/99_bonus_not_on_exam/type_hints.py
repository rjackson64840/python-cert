# TYPE HINTS (TYPE ANNOTATIONS) — BONUS, *NOT* ON THE PCAP EXAM
# =============================================================
# PCAP-31-03 tests plain, UNTYPED Python. Type hints are a separate real-world
# skill used in production code (like your APT project). This file explains
# them so you can READ and WRITE typed code — but none of it is on the exam.
# File it under "professional Python," not "exam material."
#
# KEY IDEA: annotations are OPTIONAL METADATA. Python does NOT enforce them at
# runtime — they exist for humans, IDEs, and static checkers (mypy, Pyright,
# PyCharm). The interpreter ignores the declared types when the code runs.


# ---------------------------------------------------------------------------
# 1. VARIABLE ANNOTATIONS:  name: type  (optionally = value)
# ---------------------------------------------------------------------------
count: int = 0
title: str = "PCAP"
ratio: float = 1.5
done: bool = False
# The annotation is just a label; the assigned value is what matters at runtime.


# ---------------------------------------------------------------------------
# 2. FUNCTION ANNOTATIONS:  parameter types and a return type
# ---------------------------------------------------------------------------
def greet(name: str, excited: bool = False) -> str:
    #         ^^^ param types            ^^^ return type (after the arrow)
    mark = "!" if excited else "."
    return f"Hello, {name}{mark}"

print(greet("Alice"))             # Hello, Alice.
print(greet("Bob", excited=True)) # Hello, Bob!


# ---------------------------------------------------------------------------
# 3. NOT ENFORCED AT RUNTIME — the big surprise
# ---------------------------------------------------------------------------
# `name: str` is only a HINT. Passing an int still runs with NO error:
print(greet(123))                 # Hello, 123.  — no TypeError!
# A static checker (mypy/Pyright) WOULD flag greet(123), but Python itself runs
# it happily. Annotations document intent; they do not validate data.


# ---------------------------------------------------------------------------
# 4. CONTAINER (GENERIC) TYPES — describe what is INSIDE a collection
# ---------------------------------------------------------------------------
scores: list[int] = [90, 85, 100]          # a list of ints
counts: dict[str, int] = {"a": 1, "b": 2}  # dict: str keys -> int values
point: tuple[int, int] = (3, 4)            # a 2-tuple of ints
tags: set[str] = {"py", "cert"}
# (Python 3.9+ uses the built-in list/dict/tuple/set here. Older code imported
#  List, Dict, Tuple from the `typing` module — same meaning, older syntax.)


# ---------------------------------------------------------------------------
# 5. OPTIONAL / UNION — "this OR that", and "maybe None"
# ---------------------------------------------------------------------------
def find_user(uid: int) -> str | None:     # returns a str OR None
    return "admin" if uid == 1 else None
# `X | None` (Python 3.10+) is the modern spelling of "X or None".
# Older code wrote Optional[str] or Union[str, None] from `typing`.
print(find_user(1))    # admin
print(find_user(2))    # None


# ---------------------------------------------------------------------------
# 6. CUSTOM CLASSES AS TYPES — exactly what your APT code did
# ---------------------------------------------------------------------------
class Finding:
    def __init__(self, area: str, severity: str) -> None:
        self.area = area
        self.severity = severity

def collect() -> list[Finding]:            # returns a list of Finding objects
    out: list[Finding] = []                # variable annotation, like your APT line
    out.append(Finding("Frontmatter", "major"))
    return out

print([f.severity for f in collect()])     # ['major']


# ---------------------------------------------------------------------------
# 7. WHERE ANNOTATIONS LIVE: the __annotations__ dict
# ---------------------------------------------------------------------------
# Python stores annotations in a dict so tools can read them back:
print(greet.__annotations__)   # {'name': <class 'str'>, 'excited': <class 'bool'>, 'return': <class 'str'>}


# ---------------------------------------------------------------------------
# 8. WHY BOTHER? (when types earn their keep)
# ---------------------------------------------------------------------------
# - Static checking: mypy/Pyright catch type mismatches BEFORE you run.
# - Editor help: autocomplete and inline warnings (PyCharm leans on these).
# - Documentation: the signature tells a reader the expected shapes.
# They pay off as a codebase GROWS and is shared — which is precisely why your
# production APT project uses them and these single-file exam lessons do not.
#
# Optional things to explore later (NONE on PCAP):
#   pip install mypy    ->  mypy yourfile.py        (static type checking)
#   the `typing` module ->  Any, Callable, Optional, Union, TypeAlias, ...
#   from __future__ import annotations  ->  treat all annotations as strings
#       (forward references without quotes; close to the 3.14 default behavior).
