#!/usr/bin/python3
def multiple_returns(sentence):
     my_tuple = ()
     my_tuple = (len(sentence), sentence[0] if len(sentence) != 0 else "None")
     return (my_tuple)
