#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(map(lambda val: replace if val == search else val, my_list))
