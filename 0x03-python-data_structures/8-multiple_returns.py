#!/usr/bin/python3
def multiple_returns(sentence):
    tup = (0, 'None')
    tuple_a = (len(sentence), sentence[0] if len(sentence) != 0 else tup)
    return (tuple_a)
