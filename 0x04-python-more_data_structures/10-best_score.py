#!/usr/bin/python3
def best_score(a_dictionary):
    a = a_dictionary
    if type(a) is not dict or len(a) == 0:
        return (None)
    else:
        maxi = max(list(a.values()))

    for key in a_dictionary:
        if a_dictionary[key] == maxi:
            return (key)
