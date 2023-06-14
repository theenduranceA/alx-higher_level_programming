#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    my_sorted_keys = sorted(a_dictionary.keys())
    for x in my_sorted_keys:
        print(x, ":", a_dictionary[x])
