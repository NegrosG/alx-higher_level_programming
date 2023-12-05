#!/usr/bin/python3
'''Defining the write_fie function'''


def write_file(filename="", text=""):
    '''read file with utf-8'''
    with open(filename, "w", encoding='utf-8') as files:
        return files.write(text)
