#!/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        if i != 'C' and i != 'c':
            print("{}".format(i), end='')
