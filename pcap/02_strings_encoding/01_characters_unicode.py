# CHARACTERS, CODE POINTS, AND UNICODE
# ====================================
# A Python string (str) is a sequence of Unicode CODE POINTS — not bytes.
# Each character maps to an integer code point. PCAP tests ord()/chr() and the
# relationship between characters, ASCII, and Unicode.


# ord(): a ONE-character string -> its integer code point
print(ord('A'))        # 65
print(ord('a'))        # 97
print(ord('0'))        # 48   (the DIGIT zero, NOT the integer 0)
print(ord('€'))        # 8364 (a Unicode code point far beyond ASCII)

# chr(): an integer code point -> the character
print(chr(65))         # 'A'
print(chr(97))         # 'a'
print(chr(8364))       # '€'

# ord and chr are inverses:
print(chr(ord('Z')))   # 'Z'


# ASCII vs UNICODE
# ----------------
# ASCII covers code points 0–127 (English letters, digits, punctuation, and
# control chars). Unicode is a superset of ~1.1 million code points covering
# virtually every writing system. In Python 3, str is Unicode by default.
print(ord('A'), ord('B'), ord('C'))   # 65 66 67  — letters are CONSECUTIVE

# Because letters are consecutive, you can do arithmetic via ord()/chr():
print(chr(ord('A') + 1))    # 'B'
print(chr(ord('a') + 25))   # 'z'

# Uppercase and lowercase letters differ by 32 in ASCII:
print(ord('a') - ord('A'))  # 32


# PCAP POINTS:
# - ord() takes a SINGLE-character string; passing "" or "ab" raises TypeError.
# - chr() takes an int; chr(0) is the null character '\x00' (valid, unprintable).
# - Digits '0'..'9' are code points 48..57 — the character '0' is not the int 0.
# - Letters sort by code point, so ALL uppercase (65–90) precede ALL lowercase (97–122).