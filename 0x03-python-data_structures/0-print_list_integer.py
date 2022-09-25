#!/usr/bin/python3
def print_list_integer(my_list=[]):
    ''' This fn should print each integer
    of a list on a new line '''
    for i in my_list:
        print("{:d}".format(my_list[i - 1]))
