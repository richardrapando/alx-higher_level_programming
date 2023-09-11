#!/usr/bin/python3


"""Defines inherited class checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited-instance of a class.
    Args:
        obj (any): object to be checked.
        a_class (type): class matching the object
    Returns:
        True - if object is an inherited instance of a class
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
