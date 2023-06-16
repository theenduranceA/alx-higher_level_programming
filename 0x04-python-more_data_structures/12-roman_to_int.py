#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    sum = 0
    val2 = 0

    for x in roman_string:
        value = rom_num[x]
        sum += value
        if value > val2:
            sum -= 2 * val2
        val2 = value

    return (sum)
