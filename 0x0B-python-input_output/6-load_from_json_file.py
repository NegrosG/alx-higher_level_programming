#!/usr/bin/python3
'''Defining the load_from_json_file function'''


import json


def load_from_json_file(filename):
    '''creates an object from a Json file'''
    with open(filename, 'r', encoding="utf-8") as files:
        return json.load(files)
