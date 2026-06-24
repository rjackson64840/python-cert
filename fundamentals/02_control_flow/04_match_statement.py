# match / case — Python's pattern matching, added in Python 3.10
# Similar to switch/case in other languages but more powerful
#
# NO FALL-THROUGH: Unlike Java/C switch statements, Python's cases do NOT
# fall through into the next case. Once a case matches and its block runs,
# the entire match exits automatically — there is no `break` keyword and
# none is needed. (In C/Java, omitting `break` makes execution continue
# into the following case, a frequent source of bugs Python avoids.)
# To run the same block for multiple values, use the | pattern (see below).

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:             # _ is the wildcard — matches anything (like default)
        print("Unknown status")

# Matching strings
command = "quit"
match command:
    case "quit" | "exit" | "q":   # | matches multiple values
        print("Goodbye")
    case "help":
        print("Showing help...")
    case _:
        print(f"Unknown command: {command}")

# Matching with a guard (if condition)
point = (3, 0)
match point:
    case (0, 0):
        print("origin")
    case (x, 0):
        print(f"on x-axis at {x}")
    case (0, y):
        print(f"on y-axis at {y}")
    case (x, y):
        print(f"point at {x}, {y}")
