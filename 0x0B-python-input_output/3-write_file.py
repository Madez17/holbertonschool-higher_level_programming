#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename,  mode='w', encoding='UTF8') as MyFile:
        return MyFile.write(text)
