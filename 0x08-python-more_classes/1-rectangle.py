#!/usr/bin/python3
"""defines a Rectangle CLass"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

            Args:
                 width (int): The width of the new rectangle.
                 height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter fr the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value < 0:
            raise valueError("height must be >= 0")
        self.__height = value
