#!/usr/bin/python3
"""
Defines a Class rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the instance attribute of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for instance attribute of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the instance attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the instance attribute of height"""
        if type(value) is not int:
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return(self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """this returns printable string representation of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """this prints message for every deletion of rectangle"""
        print("Bye rectangle...")
