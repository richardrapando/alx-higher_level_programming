#!/usr/bin/python3


"""Defines a Rectangle class."""


class Rectangle:
    """Defines Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value.

        Args:
            value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height.

        Args:
            value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
