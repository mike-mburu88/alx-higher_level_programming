#!/usr/bin/python3
"""contains the class MyList"""


class MyList(list):
    """define the subclass of list"""
    def  print_sorted(self):
        print(sorted(self))
        
