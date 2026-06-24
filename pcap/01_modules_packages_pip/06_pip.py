# PIP — INSTALLING THIRD-PARTY PACKAGES (PCAP context)
# ====================================================
# pip installs packages from PyPI (the Python Package Index, pypi.org) into
# your environment. Full background is in fundamentals/00_getting_started/
# 05_pip_and_pypi.py — this file is the PCAP-focused recap.
#
# These are TERMINAL commands (run in the shell, not inside Python):
#
#   pip install requests              install the latest version
#   pip install requests==2.31.0      install a specific version
#   pip install "requests>=2.30"      install with a version constraint
#   pip install --upgrade requests    upgrade to the newest version
#   pip uninstall requests            remove a package
#   pip list                          list all installed packages
#   pip show requests                 show details about one package
#   pip freeze > requirements.txt     snapshot installed packages to a file
#   pip install -r requirements.txt   install everything from a snapshot
#
#
# PCAP EXAM POINTS:
#   - pip is the standard installer; packages come from PyPI (pypi.org).
#   - pip is NOT part of the Python language — it's a separate tool that
#     ships bundled with Python.
#   - `python -m pip ...` is the safest form: it runs the pip belonging to
#     THIS interpreter, avoiding "which pip?" confusion when several Python
#     versions are installed.
#   - Packages install into the ACTIVE environment (e.g. your .venv), keeping
#     project dependencies isolated.


import sys

# The robust, environment-correct way to invoke pip programmatically:
print("Invoke pip for this interpreter via:")
print(f"  {sys.executable} -m pip install <package>")
