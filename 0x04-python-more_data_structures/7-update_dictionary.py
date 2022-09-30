#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in list(a_dictionary.keys()):
        a_dictionary[key] = "{}".format(value)
    else:
        a_dictionary.update({"{}".format(key): value})
    return (a_dictionary)
