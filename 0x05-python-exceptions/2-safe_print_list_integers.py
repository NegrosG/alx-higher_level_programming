#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num, count = 0, 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end='')
            num += 1
        except (ValueError, TypeError):
            pass
        count += 1
    print()
    return count
