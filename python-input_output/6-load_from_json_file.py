#!/usr/bin/python3
'''Create object from a JSON file'''
import json


def load_from_json_file(filename):
    """Function defined"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
    f.close()
