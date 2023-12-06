#!/usr/bin/python3
'''Defining the append_after function'''


def append_after(filename="", search_string="", new_string=""):
    '''append "new_string" after a line containing
    "search_string" in "filename".'''
    with open(filename, 'r', encoding='utf-8') as files:
        list_of_line = []
        while True:
            line = files.readline()
            if line == "":
                break
            list_of_line.append(line)
            if search_string in line:
                list_of_line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as files:
        files.writelines(list_of_line)
