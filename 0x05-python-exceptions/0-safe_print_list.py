#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for iter1 in range(x):
            if iter1 < x:
                print('{:d}'.format(my_list[iter1]), end='')
    except Exception as ex:
        print()
        return iter1
    print()
    return iter1 + 1
        
