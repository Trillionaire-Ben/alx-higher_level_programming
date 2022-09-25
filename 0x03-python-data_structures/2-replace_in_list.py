#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ''' Write a function that replaces an element of
    a list at a specific position (like in C).'''
    if idx < 0:
        return (my_list)
    elif idx > (len(my_list) - 1):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
