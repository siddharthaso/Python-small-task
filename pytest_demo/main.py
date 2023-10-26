"""all function are here of project"""
from uuid import UUID
import re

def is_password_valid(password: str) -> bool:
    """check if password is valid or not (strong)
    The password must be at least 8 characters long.
    It must contain at least one uppercase letter.
    It must contain at least one lowercase letter.
    It must contain at least one digit.
    It must contain at least one special character (e.g., !@#$%^&*(),.?":{}|<>).")

    Args:
        password (str): string of password
    """

    # Password must be at least 8 characters long
    if len(password) < 8:
        return False

    # Password must contain at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Password must contain at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Password must contain at least one digit
    if not re.search(r'\d', password):
        return False

    # Password must contain at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True



def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
