#!/usr/bin/python3


"""Defines class together with inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited-instance of a class.
    Args:
        obj (any): object to be checked.
        a_class (type): class matching  the object.
    Returns:
        True - -if object is an instance or inherited instance of a_class
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
