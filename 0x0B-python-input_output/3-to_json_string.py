#!/usr/bin/python3
'''Defining the to_json_string function'''


import json


def to_json_string(my_obj):
    '''returns json repesentation of an object'''
    return json.dumps(my_obj)
