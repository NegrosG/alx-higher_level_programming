#!/usr/bin/python3
'''Defining the read_fie function'''


def read_file(filename=""):
    '''read file with utf-8'''
    with open(filename, encoding='utf-8') as files:
        print(files.read(), end="")
