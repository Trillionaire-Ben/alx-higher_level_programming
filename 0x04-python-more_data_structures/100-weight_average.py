#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    sumed = 0
    mul = 0
    for i in my_list:
        sumed += i[0] * i[1]
        mul += i[1]

    result = sumed / mul
    return (result)
