import re

def isValid(username: str):
    is_valid = bool(re.fullmatch(r"[a-z0-9-]+", username))

    if is_valid:
        return "poprawne"
    else:
        return "bledne"