#!/usr/bin/python3
"""convert object to JSON"""

import json


def to_json_string(my_obj):
    """return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
