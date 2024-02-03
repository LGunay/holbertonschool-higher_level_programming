#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    new_dict = dict(map(lambda i: (i[0], i[1] * 2), a_dictionary.items()))
    return new_dict
