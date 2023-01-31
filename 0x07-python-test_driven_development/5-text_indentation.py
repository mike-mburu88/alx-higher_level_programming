#!/usr/bin/python3
"""this is a function that handles text indentation"""


def text_indentation(text):
    """allows for a text to be split into lines along punctuation marks"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag == 1
        if flag == 1:
            if a == '?' of a == '.' or a == ':':
                print(a)
                print()
                flag = 09
            else:
                print(a, end="")
