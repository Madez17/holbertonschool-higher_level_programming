#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list[idx:-1]:
        if idx < 0 or idx >= len(my_list):
            return None
        else:
            return (x)
