#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maks = my_list[0]
        for i in mylist:
            if i > maks:
                maks = i
        return maks
