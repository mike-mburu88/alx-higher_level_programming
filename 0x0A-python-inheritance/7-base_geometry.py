#!/usr/bin/python3
"""Contains the class BaseGeometry"""



class BaseGeometry:
    """defines the class with instance methods area and integer validator"""


    def area(self):
        """an exception is raised when this method is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if an integer is > 0"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
