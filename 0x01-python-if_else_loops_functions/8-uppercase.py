#!/usr/bin/python3
def uppercase(str):
    for string1 in str:
        if ord(string1) >= 97 and ord(string1) <= 122:
            string1 = chr(ord(string1) - 32)
        print('{}'.format(string1), end='')
    print("")
