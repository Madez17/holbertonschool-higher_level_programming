#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) != int:
        raise TypeError ('a must be an integer')
    elif type(b) != int:
        raise TypeError 
    elif type(a, b) != float:
        raise TypeError
    
    return a + b
    
