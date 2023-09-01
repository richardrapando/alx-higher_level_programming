#!/usr/bin/python3


"""Unittests for max_integer([...])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([...])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [11, 12, 13, 14]
        self.assertEqual(max_integer(ordered), 14)

    def test_unordered_list(self):
        """Tests an unordered list of integers."""
        unordered = [11, 14, 13, 12]
        self.assertEqual(max_integer(unordered), 14)

    def test_max_at_beginning(self):
        """Tests a list beginning with a max value."""
        max_at_beginning = [14, 13, 12, 11]
        self.assertEqual(max_integer(max_at_beginning), 14)

    def test_empty_list(self):
        """Tests an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Tests a list with a single element."""
        one_element = [17]
        self.assertEqual(max_integer(one_element), 17)

    def test_floats(self):
        """Tests a list of floating point numbers."""
        floats = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.assertEqual(max_integer(floats), 0.5)

    def test_ints_and_floats(self):
        """Tests a list of integers and floating point numbers."""
        ints_and_floats = [1, 2, 3, 4, 5.5]
        self.assertEqual(max_integer(ints_and_floats), 5.5)

if __name__ == '__main__':
    unittest.main()
