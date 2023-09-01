#!/usr/bin/python3


"""Defines integer addition function."""
def add_integer(a, b=98):
    """Return integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: Id either a or b is a non-integer and non-float.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
