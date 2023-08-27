#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes function safely.
    Args:
        fct: function to execute.
        args: Arguments.
    Returns:
         None - If an error occurs.
        Otherwise - result of call to fct.
    """
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return None
