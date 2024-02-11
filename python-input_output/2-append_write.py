#!/usr/bin/python3

'''Append to a file'''


def append_write(filename="", text=""):
    '''define function'''
    with open(filename, "a", encoding="utf-8") as f:
        result = f.write(text)
    f.close()
    return result
