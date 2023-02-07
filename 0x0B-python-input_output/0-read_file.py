#!/usr/bin/python3
"""create a module to read a file"""
def read_file(filename=""):
    """read file with UTF8 encoding and prints as output"""
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end="")
