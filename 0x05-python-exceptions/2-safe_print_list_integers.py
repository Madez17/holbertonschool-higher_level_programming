#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for iter1 in range(x):
        try:
            if iter1 < x:
                print('{:d}'.format(my_list[iter1]), end='')
                count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
