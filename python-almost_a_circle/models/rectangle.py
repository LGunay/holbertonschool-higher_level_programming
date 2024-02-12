#!/usr/bin/python3
'''First Rectangle'''
from models.base import Base


class Rectangle(Base):
    """create class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.__x = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.__y = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
