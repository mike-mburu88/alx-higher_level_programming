#!/usr/bin/python3
"""contains the class MyList"""


class MyList(list):
    """define the subclass of list"""
    def __init__(self):
        """Initialize the object of the class"""

        super().__init__()


    def print_sorted(self):
        """function to print a sorted list"""

        print(sorted(self))
        
