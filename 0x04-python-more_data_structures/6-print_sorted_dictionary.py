#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listdic_keys = list(a_dictionary.keys())
    listdic_keys.sort()
    for i in listdic_keys:
        print("{} : {}".format(i, a_dictionary.get(i)))
