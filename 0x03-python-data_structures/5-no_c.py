#!/usr/bin/python3

def no_c(my_string):

    my_new_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            my_new_str = my_new_str + i
    return (my_new_str)
