#!/usr/bin/python3
"""Write the class"""
class Square:
    """Represent square attributes for sides"""
    def __init__(self, size=0):
        """square arguments to return None"""
        self.size = size
    def area(self):
        """method calculates area of a square"""
        return (self.__size) ** 2
    def size(self):
        """The gettter of size returns square size"""
        return self.__size
    def size(self, value):
        """setter of size from square size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                 self.__size = value
