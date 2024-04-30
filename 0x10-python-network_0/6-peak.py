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

    peak = list_of_integers[0]
    a = 1
    while (a < len(list_of_integers)):
        if peak < list_of_integers[a]:
            peak = list_of_integers[a]
            a += 1
        return peak
