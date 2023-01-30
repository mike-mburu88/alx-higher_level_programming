#!/usr/bin/python3
"""defines the class"""


class Rectangle:
    """Define the class
    attributes:
    __size (int): size of a side of the rectangle"""
    def __init__(self, size):
        """method to initialize a rectangle
        args:
        siz(int): size of a rectagle side
        Returns: None
        """
        self.__size = size
