# A module that lives INSIDE the utils package (a subfolder). Because it is not
# directly on sys.path, you reach it as `utils.text` — never a bare `text`.

BANNER = "*** from utils.text ***"


def shout(message):
    """Return the message in all caps with an exclamation mark."""
    return message.upper() + "!"