#!/usr/bin/python3
'''First Rectangle'''
from models.base import Base


class Rectangle(Base):
    """create class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        if type(value) is int:
            self.__x = value
        else:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        if type(value) is int:
            self.__y = value
        else:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''area of rectangle'''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the Rectangle instance'''
        for g in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print(end="\n")

    def __str__(self):
        '''str method'''
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x,
                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''update rectangle'''
        arguments = ['id', 'width', 'height', 'x', 'y']
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
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return dicti
