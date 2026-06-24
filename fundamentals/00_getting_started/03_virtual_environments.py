# A virtual environment is an isolated Python installation for a project.
# It keeps your project's dependencies separate from other projects.
# This solves the version conflict problem: Project A needs requests==2.28,
# Project B needs requests==2.31 — they can't coexist in the global install.
#
# This project already has one set up in the .venv folder.


# COMMON TERMINAL COMMANDS
# ------------------------
# These are shell commands — run in the terminal, not in Python.
#
#   Create:   python -m venv .venv
#   Activate: .venv\Scripts\activate          (Windows)
#             source .venv/bin/activate        (Mac/Linux)
#   Install:  pip install package-name
#   List:     pip list
#   Freeze:   pip freeze > requirements.txt    (snapshot installed packages)
#   Exit:     deactivate


# PYCHARM / INTELLIJ
# ------------------
# PyCharm detects .venv automatically and uses it as the Project Interpreter —
# the Python runtime for running scripts, resolving imports, and code completion.
#
# PyCharm doesn't "activate" the venv like a terminal does. Instead it points
# directly at .venv\Scripts\python.exe, which achieves the same isolation.
# The built-in terminal does auto-activate the venv for you.
#
# To verify or change the interpreter:
#   Settings → Project: <name> → Python Interpreter
#   Should show: Python 3.14.x pointing to .venv\Scripts\python.exe
#
# If the interpreter is broken (red imports, "No Python at..." errors):
#   Settings → Project → Python Interpreter → gear icon →
#   Add Interpreter → Add Local Interpreter → Existing →
#   browse to .venv\Scripts\python.exe
#
# After recreating .venv (e.g. after a Python upgrade), PyCharm usually
# detects the change automatically — accept the prompt if it appears.


# GIT / SOURCE CONTROL
# --------------------
# .venv should NOT be committed to git — it's large, platform-specific,
# and easily recreated. Two layers of protection exist in this project:
#
#   1. .venv/.gitignore contains `*` — ignores all files inside .venv
#      (created automatically by `python -m venv`)
#   2. Root .gitignore explicitly excludes .venv/
#
# Instead, commit requirements.txt so others can recreate the environment:
#   pip freeze > requirements.txt        (save)
#   pip install -r requirements.txt      (restore)
#
# KEEPING requirements.txt UP TO DATE
# ------------------------------------
# requirements.txt does not update automatically — it's a manual step:
#   1. pip install requests              (install a package)
#   2. pip freeze > requirements.txt     (update the file)
#   3. commit both together
#
# Modern alternatives that handle this automatically:
#   - Poetry:  `poetry add requests` installs and updates pyproject.toml + lockfile
#   - uv:      `uv add requests`     same idea, much faster (Rust-based)
#   - pip-tools: maintain requirements.in manually, run `pip-compile` to pin
#
# For a learning project, manual pip freeze is fine.
# For production work, Poetry or uv are the current community standards.


import sys
print("Active environment:", sys.prefix)
print("Python version:", sys.version)
