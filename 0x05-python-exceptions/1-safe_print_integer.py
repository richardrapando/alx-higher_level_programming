#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()
    Args:
        value: the integer to print

    Returns:
        True if value has been printed correctly
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
