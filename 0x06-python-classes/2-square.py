#!/usr/bin/python3
"""create the class Square"""
class Square:
    """provide the attribute for the class"""
    def __init__(self, size=0):
        """initialize the arguments"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self:__size = size
        else:
            raise TypeError('size must be an integer')
