#!/usr/bin/python3
"""create an object retrieving modult from the json file"""
import json

def load_from_json_file(filename):
    """a functions that takes the filename as an argument and loads a python object"""

    with open(filename, 'r') as f:
         return json.load(f)
