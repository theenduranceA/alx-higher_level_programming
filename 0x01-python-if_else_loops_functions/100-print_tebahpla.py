#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2 == 1:
        c = c - ord(" ")
    print("{}".format(chr(c)), end="")
