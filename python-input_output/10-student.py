#!/usr/bin/python3
'''Student to JSON'''


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """funtion"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function"""
        if attrs is None:
            return self.__dict__
        else:
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
