#!/usr/bin/python3
"""First, define the class"""
class Square:
    """ list all probable attributes"""
    def __init__(self, size=0):
        """set the instants for the attributes"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
    def area(self):
        """returns an area of a square"""
        return self.__size ** 2
