#!/usr/bin/python3
"""Module for class Basegeometry"""


class BaseGeometry:
    """A basegeometry Class."""
    def area(self):
        """method to compute this area"""
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        '''Method for validating the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
