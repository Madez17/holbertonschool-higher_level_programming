#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF8') as MyFile:
        print(MyFile.read(), end='')
