#!/usr/bin/python3
def uniq_add(my_list=[]):
    save = list(set(my_list))
    suma = 0
    for num in save:
        suma = suma + num
    return suma
