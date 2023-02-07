#!/usr/bin/python3
"""Module to implement a class with the serialize itself"""

class Student:
    """ a class to represent a student's atttrbutes"""
    def __init__(self, first_name, last_name, age):
        """"create a new instance of a student with name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """create a copy of all attributes in the json string"""
        return self.__dict__.copy()
    
