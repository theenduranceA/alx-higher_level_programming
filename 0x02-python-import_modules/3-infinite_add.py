#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    agg = 0
    for i in range(1, len(sys.argv)):
        agg = agg + int(sys.argv[i])
    print("{:d}".format(agg))
