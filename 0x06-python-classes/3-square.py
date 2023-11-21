#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
