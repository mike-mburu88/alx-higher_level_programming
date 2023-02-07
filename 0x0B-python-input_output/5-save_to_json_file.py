#!/usr/bin/python3
"""create a module to contain a function to save python object in json format"""

def save_to_json_file(my_obj, filename):
    """create a function to convert on 'my_obj' to json string and save filename"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
