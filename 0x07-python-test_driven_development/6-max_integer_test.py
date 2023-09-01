#!/usr/bin/python3
"""Module to find maximum integer in a list
"""


def max_integer(list=[]):
    """Function to find and return maximum integer in a list of integers
        The function returns None if the list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
