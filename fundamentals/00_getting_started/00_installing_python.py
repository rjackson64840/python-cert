# INSTALLING PYTHON
# -----------------
# Download from: https://www.python.org/downloads/
# Always grab the latest stable release.
#
# Windows installer tips:
#   - Check "Add Python to PATH" before clicking Install
#   - Check "Use admin privileges when installing py.exe"
#   - Choose "Customize installation" if you want to change the install location
#
# Verify installation in a new terminal:
#   python --version
#   pip --version


# PYMANAGER — VERSION MANAGEMENT (Python 3.14+ on Windows)
# ---------------------------------------------------------
# Python 3.14 installs PyManager, a dedicated version manager similar to
# nvm (Node) or rustup (Rust). It lives at:
#   C:\Program Files\PyManager\py.exe
#
# Common commands:
#   py list                List all installed Python versions
#   py install 3.14        Download and install a specific version
#   py install --update    Update existing managed installs
#   py uninstall 3.12      Remove a version
#
# PATH NOTE: The old Windows py launcher (C:\Windows\py.exe) may take
# precedence over PyManager in PATH, causing `py list` to fail with a
# "can't open file" error. Fix by moving C:\Program Files\PyManager
# above C:\Windows in System Properties → Environment Variables → Path.
# Open a new terminal after changing PATH for it to take effect.
#
# MANAGED VS UNMANAGED: Versions installed via the traditional python.org
# installer show an asterisk (*) in `py list` — PyManager can see them
# but cannot update or uninstall them. Use PyManager's `py install` for
# all future installs so they are fully managed.
#
# Run a specific version:
#   py -3.14 script.py


# UPDATING PYTHON (pre-3.14 / without PyManager)
# -----------------------------------------------
# Download a new installer from python.org and run it — it replaces the
# old version in place. There is no dedicated update command in older setups.


# CLEANING UP OLD VERSIONS
# ------------------------
# Over time it's easy to accumulate old Python versions. Remove them to
# keep things tidy. `py uninstall` only works for versions PyManager itself
# installed — for everything else use Windows:
#   - PyManager-managed:   py uninstall 3.12
#   - Store versions:      Settings → Apps → search "Python" → Uninstall
#   - Traditional installs: Settings → Apps → search "Python" → Uninstall
#                           (or Control Panel → Programs and Features)


# UPDATING PIP
# ------------
# pip is Python's package manager. Keep it current:
#   python -m pip install --upgrade pip


# Check versions from inside Python:
import sys
print("Python:", sys.version)

import pip
print("pip:", pip.__version__)
