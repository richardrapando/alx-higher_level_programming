#!/usr/bin/python3
"""object from JSON"""

import json


def from_json_string(my_str):
    """return an object (Python data structure) represented by a JSON string."""
    return json.loads(my_str)
