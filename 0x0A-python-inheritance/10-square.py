#!/usr/bin/python3


"""defines rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent square."""

    def __init__(self, size):
        """initialize a new square.
        Args:
            size (int): size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
