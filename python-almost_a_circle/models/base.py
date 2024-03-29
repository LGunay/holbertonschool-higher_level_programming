#!/usr/bin/python3
'''Base class'''

import json


class Base:
    '''Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''update Base'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        dicti_list = []
        filename = cls.__name__ + ".json"
        if list_objs is None:
            f = open(filename, "w")
            f.write('[]')
            f.close()
        else:
            for i in list_objs:
                dicti_list.append(i.to_dictionary())
            f = open(filename, "w")
            f.write(Base.to_json_string(dicti_list))
            f.close()

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        r = []
        try:
            with open(filename, "r") as f:
                text = f.read()
            obj_list = Base.from_json_string(text)
            for obj in obj_list:
                r.append(cls.create(**obj))
        except Exception as _:
            pass
        return r
