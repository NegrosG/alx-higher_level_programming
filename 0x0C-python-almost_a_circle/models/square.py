#!/usr/bin/python3
'''Module for a square subclass'''
from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string information about this square'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
