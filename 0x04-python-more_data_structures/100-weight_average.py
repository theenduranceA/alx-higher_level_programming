#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum(score * weight for score, weight in my_list) / sum(weight for x, weight in my_list)

