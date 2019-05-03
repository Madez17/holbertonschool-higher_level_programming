#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv)
    result = 0
    if arguments == 0:
        print(arguments)
    for iter1 in range(1, arguments):
        result += int(argv[iter1])
    print('{}'.format(result))
