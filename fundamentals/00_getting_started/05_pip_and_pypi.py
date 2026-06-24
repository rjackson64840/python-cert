# HOW PYTHON PACKAGES WORK
# -------------------------
# Packages are published to PyPI (Python Package Index) at pypi.org —
# the central registry for Python packages, similar to npm (Node) or
# NuGet (.NET). Anyone with a free PyPI account can publish a package.
#
# When you run `pip install requests`:
#   1. pip looks up "requests" on PyPI
#   2. Downloads the package and its dependencies
#   3. Installs everything into the active virtual environment
#
# HOW A PACKAGE GETS ONTO PYPI
# -----------------------------
# A developer:
#   1. Writes the package and adds a pyproject.toml describing it
#      (name, version, dependencies, author, etc.)
#   2. Builds it into a distributable format (.whl or .tar.gz)
#   3. Uploads it to PyPI
#
# The manual way (two steps):
#   python -m build       # produces .whl and .tar.gz in dist/
#   twine upload dist/*   # uploads to PyPI
#
# With Poetry (one command that builds and uploads):
#   poetry publish --build
#
# After that it's publicly available to anyone via pip.
#
# OTHER INSTALL SOURCES
# ---------------------
# pip can install from places other than PyPI:
#
#   GitHub repo:      pip install git+https://github.com/user/repo
#   Local folder:     pip install ./my-package
#   Private registry: companies run their own (Artifactory, AWS CodeArtifact)
#                     pip install --index-url https://my-registry.com/simple pkg
#
# SECURITY RISK: TYPOSQUATTING
# ----------------------------
# PyPI is open — anyone can publish, and package names are first-come-first-served.
# Attackers register packages with names similar to popular ones to trick
# developers into installing malware:
#   requests   → legitimate
#   requets    → could be malicious
#
# Always double-check the package name before installing, and prefer packages
# with high download counts, active maintainers, and a known GitHub repo.


# ARE PACKAGES CROSS-PLATFORM?
# ----------------------------
# Mostly yes, but it depends on what the package contains:
#
# Pure Python packages — fully cross-platform. Just Python code, works everywhere.
#
# Packages with compiled extensions (C/C++) — platform-specific. High-performance
# packages like numpy, pandas, and pillow include compiled C code. PyPI distributes
# these as pre-compiled wheels for each platform so pip picks the right one.
#
# If no wheel exists for your platform, pip falls back to downloading the source
# and compiling locally — which requires a C compiler. Rare on common platforms
# but can happen on unusual architectures.


# WHEELS (.whl)
# -------------
# A wheel is the standard binary package format for Python. It's a ZIP file
# renamed to .whl — pip downloads it and unpacks it directly, no compilation step.
# This makes installs fast and reliable.
#
# Before wheels, Python used .egg files (now obsolete) and source distributions
# (.tar.gz / sdist) that required compilation on the user's machine.
#
# WHEEL FILENAME ANATOMY
# ----------------------
# Wheel filenames encode exactly what they support:
#
#   numpy-2.0.0-cp314-cp314-win_amd64.whl
#   |     |     |     |     |
#   |     |     |     |     Platform (win_amd64 = Windows 64-bit)
#   |     |     |     ABI tag (cp314 = CPython 3.14 ABI)
#   |     |     Python tag (cp314 = CPython 3.14)
#   |     Version
#   Package name
#
# Common Python tags:
#   cp314   CPython 3.14
#   py3     any Python 3 (pure Python, no compiled code)
#
# Common platform tags:
#   win_amd64       Windows 64-bit
#   macosx_14_arm64 macOS 14, Apple Silicon
#   manylinux_*     Linux (broad compatibility)
#   none            any platform (pure Python)
#
# A pure Python wheel looks like:
#   requests-2.31.0-py3-none-any.whl
#   (py3 = Python 3, none = no ABI requirement, any = any platform)
#
# pip automatically selects the correct wheel for your platform.
# You can see which wheel was downloaded with: pip install numpy -v
#
# WHAT IS ABI?
# ------------
# ABI (Application Binary Interface) defines how compiled code communicates
# at the binary level — how functions are called, how data is laid out in
# memory, how parameters are passed.
#
# For Python, the ABI tag means "this compiled extension was built against
# a specific version of CPython's internals." If those internals change
# between versions, an extension built for 3.13 may crash on 3.14.
# That's why cp314-cp314 means: built for CPython 3.14, runs on CPython 3.14.
#
# There's also a stable ABI (abi3) — a subset of CPython internals that
# Python guarantees won't change across versions. Wheels using it look like:
#   numpy-2.0.0-cp3-abi3-win_amd64.whl   (works on Python 3.x and above)
# Package authors opt into this for broader compatibility.
#
# In practice pip handles ABI selection automatically — you never pick manually.
#
# WHY IS IT CALLED A WHEEL?
# -------------------------
# It's a Monty Python joke. PyPI was originally nicknamed the Cheese Shop,
# after a sketch where a customer visits a shop completely out of cheese —
# a dig at early PyPI having many broken or missing packages.
#
# The predecessor format was called .egg (continuing the food theme).
# When wheels replaced eggs in 2012, the name came from the Spanish Inquisition
# sketch: "Our chief weapon is surprise... and the wheel!"
#
# .whl is just "wheel" shortened to a three-letter extension.
#
# Python itself is named after Monty Python's Flying Circus, not the snake —
# so the ecosystem has a long tradition of these references.


# Check what's installed in the current environment:
import subprocess, sys
subprocess.run([sys.executable, "-m", "pip", "list"])
