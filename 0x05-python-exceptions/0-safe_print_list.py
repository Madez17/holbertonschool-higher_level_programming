#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for iter1 in range(x):
        try:
            if iter1 < x:
                print('{}'.format(my_list[iter1]), end='')
                count += 1
        except Exception as ex:
            print()
            return count
    print()
    return count
