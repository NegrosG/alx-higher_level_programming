#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    c_int = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        c_int = False
    return c_int
