#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """function reads a text file (UTF8) and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
