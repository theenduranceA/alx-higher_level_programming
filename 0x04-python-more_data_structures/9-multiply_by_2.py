#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    for x in my_dict:
        my_dict[x] *= 2
    return (my_dict)
