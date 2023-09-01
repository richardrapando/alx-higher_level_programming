#!/usr/bin/python3


"""Prints square with the character #."""


def print_square(size):
    """function to print a square.

    Args:
        size (int): length of square
    Raises:
        TypeError: if size is not an integer
        ValueError: if the size is less than 10
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
