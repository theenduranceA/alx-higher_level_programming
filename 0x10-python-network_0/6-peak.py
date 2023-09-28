#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak and Return: Peak"""

    list_length = len(list_of_integers)
    mid_val = list_length
    _val = list_length // 2

    if _val == 0:
        return None

    while True:
        mid_val = mid_val // 2
        if _val > 0 and list_of_integers[_val] < list_of_integers[_val - 1]:
            if mid_val // 2 == 0:
                mid_val = 2
            _val = _val - mid_val//2
        elif _val + 1 < list_length and list_of_integers[_val] < \
                list_of_integers[_val + 1]:
            if mid_val // 2 == 0:
                mid_val = 2
            _val = _val + mid_val//2
        else:
            return list_of_integers[_val]
