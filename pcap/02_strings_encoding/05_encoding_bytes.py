# ENCODING, DECODING, AND BYTES
# =============================
# A str holds Unicode CODE POINTS (abstract characters). To store or transmit
# text you must ENCODE it into BYTES using a codec such as UTF-8; reading it
# back is DECODING. This str <-> bytes boundary is a PCAP favorite.

text = "café"               # 4 CHARACTERS (note the accented é)
print(len(text))            # 4   — length in characters

# ENCODE: str -> bytes
data = text.encode("utf-8")
print(data)                 # b'caf\xc3\xa9'  — é becomes TWO bytes in UTF-8
print(type(data))           # <class 'bytes'>
print(len(data))            # 5   — length in BYTES (é = 2 bytes, so 5 != 4)

# DECODE: bytes -> str
back = data.decode("utf-8")
print(back)                 # 'café'
print(back == text)         # True

# bytes is an IMMUTABLE sequence of ints 0–255:
b = b"ABC"
print(b[0])                 # 65   indexing bytes yields an INT, not a 1-char string
print(list(b))              # [65, 66, 67]

# bytearray is the MUTABLE counterpart of bytes:
ba = bytearray(b"ABC")
ba[0] = 90                  # allowed — bytearray supports item assignment
print(ba)                   # bytearray(b'ZBC')

# ASCII vs UTF-8: pure-ASCII text is 1 byte per char; non-ASCII needs more.
print("ABC".encode("utf-8"))   # b'ABC'           3 chars -> 3 bytes
print("€".encode("utf-8"))     # b'\xe2\x82\xac'  1 char  -> 3 bytes

# Encoding a character the codec cannot represent raises UnicodeEncodeError —
# caught live here so the message prints (full try/except coverage in Module 6):
try:
    "café".encode("ascii")  # ASCII (0–127) cannot represent 'é'
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)


# PCAP POINTS:
# - str.encode() -> bytes;  bytes.decode() -> str.  UTF-8 is the usual codec.
# - len(str) counts CHARACTERS; len(bytes) counts BYTES — they can differ.
# - Indexing a bytes/bytearray yields an INT (0–255), not a one-character string.
# - bytes is immutable; bytearray is mutable (item assignment allowed).
