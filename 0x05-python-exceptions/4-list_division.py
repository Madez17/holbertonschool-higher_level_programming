#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for x in range(list_length):
        try:
            divTwoList = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError as error:
            divTwoList = 0
            print("division by 0")
        except TypeError as te:
            divTwoList = 0
            print("wrong type")
        except IndexError as idx:
            divTwoList = 0
            print("out of range")
        finally:
            newList.append(divTwoList)
    return newList
