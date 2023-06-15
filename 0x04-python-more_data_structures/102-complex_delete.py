#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_del = []
    for x, y in a_dictionary.items():
        if y == value:
            keys_del.append(x)
    for x in keys_del:
        a_dictionary.pop(x, None)
    return (a_dictionary)
