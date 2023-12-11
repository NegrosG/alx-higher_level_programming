#!/usr/bin/python3
'''Module for Subclass Rectangle'''
from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        '''A class constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        """method for valdating the value"""
        if type(value) != int:
            raise TypeError("() must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("() must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("() must be > 0".format(name))

    def area(self):
        '''computes area of this rectangle'''
        return self.width * self.height

    def display(self):
        '''prints strings rep of the rectangle'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')