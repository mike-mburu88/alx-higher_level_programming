#!/usr/bin/python3
"""create a module to convert objects to json"""

import json

def to_json_string(my_obj):
    """Convert serializable objects in a json string"""

    return json.dumps(my_obj)
