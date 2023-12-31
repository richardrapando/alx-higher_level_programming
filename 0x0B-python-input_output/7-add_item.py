#!/usr/bin/python3
"""all arguments"""

from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file
    load_from_json_file = load_json
    filename = "add_item.json"

    try:
        list = load_from_json_file(filename)
    except Exception:
        list = []

    list.extend(argv[1:])
    save_to_json_file(list, "add_item.json")
