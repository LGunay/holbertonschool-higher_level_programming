#!/usr/bin/python3
"""Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        self.__size = size
        super().inreger_validator("size", size)
        super().__init__(size, size)
