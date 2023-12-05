#!/usr/bin/python3
'''Defining the a class "student".'''


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        '''initiliaze student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dictionary representation of student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        otherwise, all attrs must be retieved
        '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        mydict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                mydict[key] = value
        return mydict

    def reload_from_json(self, json):
        '''that replaces all attributes of the Student instance
        with the ones in json arg
        '''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
