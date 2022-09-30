#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sums = 0

    for i in uniq_list:
        sums += i

    return (sums)
