#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, mode='r', encoding='UTF8') as MyFile:
        countLines = 0
        for line in MyFile:
            countLines += 1
    return countLines
