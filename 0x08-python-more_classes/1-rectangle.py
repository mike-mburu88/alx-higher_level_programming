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
        self.height = height
        self.width = width

        
        @property
        def width(self):
            """a getter for the private instance attribute width"""
            return self.__width


        @width.setter
        def width(self, value):
            """private instance attribute width setter"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value


        @property
        def height(self):
            """private instance attribute height getter"""
            return self.__height
        @height.setter
        def height(self, value)
            """private instance attribute height getter"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
