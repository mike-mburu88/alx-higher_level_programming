#!/usr/bin/python3
"""a python program to find a peak in a list of
unsorted integers"""

def find_peak(list_of_integers):
    """The function to sort a list of integers
    args: list of integers
    """
    if list_of_integers == []:
        return None
    
    listlen = len(list_of_integers)
    q = int(listlen / 2)
    x = list_of_integers

    if q - 1 < 0 and q + 1 >= listlen:
        return x[q]
    elif q - 1 < 0:
        return x[q] if  x[q] > x[q + 1] else x[q + 1]
    elif q + 1 >= listlen:
        return x[q] if x[q] > x[q - 1] else x[q - 1]
    if x[q - 1] < x[q] > x[q + 1]:
        return x[q]

        if x[q + 1] > x[q - 1]:
            return find_peak(x[q:])
        return find_peak(x[:q])
