#!/usr/bin/python3
def best_score(a_dictionary):
    a = a_dictionary
    if type(a) is not dict or len(a) == 0:
        return (None)
    else:
        dict_copy = a_dictionary.copy()
        maxi = max(list(dict_copy.value()))
        return (maxi)
