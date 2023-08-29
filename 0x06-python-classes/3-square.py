#!/usr/bin/python3


"""Define a Square class."""


class Square:
    """Represent Square."""

    def __init__(self, size=0):
        """Initialize new Square

        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns current square."""
        return (self.__size * self.__size)
