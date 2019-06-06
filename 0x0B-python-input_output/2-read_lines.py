#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode='r', encoding='UTF8') as MyFile:
        counLines = 0
        for line in range(nb_lines):
            counLines += 1
            print(MyFile.readline(), end='')
        if nb_lines <= 0 or nb_lines >= counLines:
            print(MyFile.read(), end='')
