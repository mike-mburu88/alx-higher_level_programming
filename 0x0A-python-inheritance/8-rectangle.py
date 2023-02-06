#!/usr/bin/python3
"""Contains the class BaseGeometry with Rectangle subclass"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents the attributes of a rectange"""

    def __init__(self, width, height):
        """create an instance of a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
