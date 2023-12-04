#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """look up objects attributes and methods.
    Args:
         obj: object to list.
    return: the list of attributes.
    """
    return dir(obj)
