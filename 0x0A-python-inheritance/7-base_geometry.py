#!/usr/bin/python3


"""Defines base geometry class BaseGeometry."""


class BaseGeometry:
    """reprsent the base geometry."""

    def area(self):
        """not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer.
        Args:
            name (str): name of parameter.
            value (int): parameter to be validated.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
