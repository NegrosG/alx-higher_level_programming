#!/usr/bin/python3
'''Defines an MyInt class that inherit from int.'''


class MyInt(int):
    '''Invert int operators == and !=.'''

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        '''Override != operator with == behavior.'''
        return self.real == value
