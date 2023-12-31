"""Module for class of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''method for area of square'''
        return self.__size ** 2

    def __str__(self):
        '''Returns string representation of the square'''
        return "[square] " + str(self.__size) + "/" + str(self.__size)
