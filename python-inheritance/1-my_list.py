#!/usr/bin/python3
'''MyList class'''


class MyList(list):
    """define class"""
    def print_sorted(self):
        '''print and sorted'''
        print(sorted(self))
