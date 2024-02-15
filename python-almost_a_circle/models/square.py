#!/usr/bin/python3
'''First square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update square'''
        arguments = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
     def to_dictionary(self):
        '''dictionary rectangle'''
        dicti = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dicti
