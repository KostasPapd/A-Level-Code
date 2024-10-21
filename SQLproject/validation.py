def validatePassword(pas):
    if len(pas) < 8:
        return False
    else:
        return True


def validateUsername(username):
    import re

    if re.fullmatch(r'[A-Za-z0-9!_*#+]{3,}', username):  # Sets what characters are allowed in the username
        # The {5,} sets the minimum length of the username
        return True
    else:
        return False
