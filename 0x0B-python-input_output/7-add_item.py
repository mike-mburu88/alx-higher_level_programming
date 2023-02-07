#!/usr/bin/python3
"""creates a module that adds a list of arguments and saves their JSON encoding to a file"""
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        save_to_json_file(load_from_json_file(FILENAME) + argv[1:], FILENAME)
    except (FileNotFoundError, ValueError):
        save_to_json_file(argv[1:], FILENAME)
