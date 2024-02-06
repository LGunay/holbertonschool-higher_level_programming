#!/usr/bin/python3
"""empty class for rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width = 0, height = 0):
        """defined Rectangle"""
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """private value of width"""
        return self.__width
    @width.setter
    def width(self, value):
        #set width
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """private value of height"""
        return self.__height
    @height.setter
    def height(self, value):
        #set height
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
