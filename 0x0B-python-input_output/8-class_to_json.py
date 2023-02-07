#!/usr/bin/python3
""" a module to return the dictionary description from JSON"""

def class_to_json(obj):
    """classes to json"""
    return (obj.__dict__)
