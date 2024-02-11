#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """define function"""
    with open(filename, "w") as fd:
        json.dump(my_obj, fd)
    fd.close()
