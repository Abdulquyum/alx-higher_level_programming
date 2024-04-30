#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    ''' function body: search for peak
    number in an unordered list '''
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    
    list_of_integers.sort()
    return(list_of_integers[-1])
