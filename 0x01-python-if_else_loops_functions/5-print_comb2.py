#!/usr/bin/python3
for number in range(0, 100):
    if number <= 9:
        print("0{}, ".format(number), end='')
    else:
        print("{}, ".format(number), end='')
