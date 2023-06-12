#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return [not i & 1 for i in range(len(my_list))]
