#!/usr/bin/python3
def no_c(my_string):
    # Write a function that removes all characters c and C from a string.
    for x in my_string:
        i = "cC"
        map_i = my_string.maketrans(x, x, i)
        return (my_string.translate(map_i))
