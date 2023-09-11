#!/usr/bin/python3
"""append string to a file."""


def append_write(filename="", text=""):
    """appends a string to the end of a text file (UTF8) 

    Args:
        filename (str): name of file to append to.
        text (str): string to append to file.
    Returns:
        number of characters appended.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
