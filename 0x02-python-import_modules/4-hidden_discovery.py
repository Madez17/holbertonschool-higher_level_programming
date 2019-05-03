#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for iter1 in dir(hidden_4):
        if iter1[0] != "_":
            print('{}'.format(iter1))
