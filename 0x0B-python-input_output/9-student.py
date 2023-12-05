#!/usr/bin/python3
'''Defining the a class "student".'''


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        '''initiliaze student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns a dictionary representation of student instance'''
        return self.__dict__
