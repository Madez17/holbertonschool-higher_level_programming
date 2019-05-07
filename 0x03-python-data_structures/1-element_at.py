#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list[idx:-1]:
        if idx < 0:
            return None
        elif len(my_list) <= idx:
            return None
        return (x)
