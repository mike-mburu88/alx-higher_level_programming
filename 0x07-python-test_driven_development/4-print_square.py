#!/usr/bin/python3
"""This file prints a function from square properties"""


def print_square(size):
    """prints a square length as an integer"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
        
