#!/usr/bin/python3
'''Defining a function that adds attributes to objects'''


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    Args:
        obj (any): the object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        Value (any): The value of att
    Raises:
        TypeError: if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
