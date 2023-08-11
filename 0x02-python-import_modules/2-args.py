#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    if (size == 2):
        print ("{:d} argument:".format(size - 1))
    elif (size == 1):
        print ("{:d} arguments.".format(size - 1))
    else:
        print ("{:d} arguments:".format(size - 1))
    for i in range(size):
        if (i != 0):
            print("{:d}: {:s}".format(i, sys.argv[i]))

    
