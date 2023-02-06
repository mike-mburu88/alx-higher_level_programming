#!/usr/bin/python3
"""a module that contains the function is_same_class"""



def is_same_class(obj, a_class):
    """returns true if the object is same as class a_class"""

    return (type(obj) == a_class)
