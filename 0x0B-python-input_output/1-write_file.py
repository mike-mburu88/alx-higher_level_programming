#!/usr/bin/python3
"""create a modlule to write a text into a file"""

def write_file(filename="", text=""):
    """Write text to filename with arguments str"""
    with open(filename, 'w', encoding='utf8') as f:
         return f.write(text)
