#!/usr/bin/python3
"""Student class"""


class Student:
    """represents a student."""

    def __init__(self, first_name, last_name, age):
        """initialize new Student.
        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dictionary representation of a Student"""
        return self.__dict__
