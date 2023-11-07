#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght < 0:
        first_char = None
    tuple_s = lenght, sentence[0]
    return(tuple_s)
