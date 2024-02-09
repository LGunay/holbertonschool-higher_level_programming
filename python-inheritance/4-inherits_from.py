#!/usr/bin/python3
'''Only sub class of'''


def inherits_from(obj, a_class):
    '''define function'''
    if issubclass(type(obj), a_class):
        return True
    return False
