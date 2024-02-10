#!/usr/bin/python3
'''Geometry module'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define inherit class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ rectangle description"""
        return ("[Rectangle] {}/{}".format(self.width, self.height))
