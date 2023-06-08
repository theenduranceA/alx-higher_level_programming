#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    p_args = len(sys.argv) - 1
    if p_args == 0:
        print("{:d} arguments.".format(p_args))
    elif p_args == 1:
        print("{:d} argument:".format(p_args))
        print("{:d}: {}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(p_args))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
