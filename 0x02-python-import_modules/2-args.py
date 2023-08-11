#!/usr/bin/python3
import sys
size = len(sys.argv)
if (size == 1):
    print ("{:d} argument.".format(size - 1))
else:
    print ("{:d} argument:".format(size - 1))
for i in range(size):
    if (i != 0):
        print("{:d}: {:s}".format(i, sys.argv[i]))

    
