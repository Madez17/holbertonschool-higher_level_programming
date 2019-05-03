#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv) - 1
    if arguments == 0:
        print(arguments, 'arguments.')
    elif arguments > 1:
        print(arguments, 'arguments:')
        for iter1 in range(1, arguments + 1):
            print('{}: {}'.format(iter1, argv[iter1]))
    elif arguments == 1:
        print(arguments, 'argument:')
        for iter1 in range(1, arguments + 1):
            print('{}: {}'.format(iter1, argv[iter1]))
