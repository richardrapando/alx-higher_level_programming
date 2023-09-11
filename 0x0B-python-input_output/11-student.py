#!/usr/bin/python3
"""Student class"""


class Student:
    """represents a student."""

    def __init__(self, first_name, last_name, age):
        """initialize a new Student.
        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation of the Student.
        Args:
            attrs (list): (Optional) attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace student attributes .
        Args:
            json (dict): value pairs to be replaced by attributes .
        """
        for k, v in json.items():
            setattr(self, k, v)
