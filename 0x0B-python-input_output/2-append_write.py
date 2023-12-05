#!/usr/bin/python3
'''Defining the append_write function'''


def append_write(filename="", text=""):
    '''append file with utf-8'''
    with open(filename, 'a', encoding='utf-8') as files:
        return files.write(text)
