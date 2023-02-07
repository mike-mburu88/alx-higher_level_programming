#!/usr/bin/python3
"""A modult to convert a json string to an object in python"""

import json

def from_json_string(my_str):
    """function to convert a string into a python object; arguments my_str"""
    return json.loads(my_str)
