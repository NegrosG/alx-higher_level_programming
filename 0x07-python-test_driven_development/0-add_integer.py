#!/usr/bin/python3
"""Module for the add_integer method"""


def add_integer(a, b=98):
    """Adds 2 integers
    Args:
        a: the first integer
        b: the second integer, default is 98

    Raise: TypeError if not int or floats

    Return: addition of the 2 integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
