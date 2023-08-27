#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides integers and prints their result
    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        result of division, otherwise none
    """
    try:
        man = a / b
    except ZeroDivisionError:
        man = None
    finally:
        print("Inside result: {}".format(man))
    return (man)
