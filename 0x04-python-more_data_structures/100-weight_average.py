#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return ("0")

    sumed = 0
    mul = 0
    for i in my_list:
        new_i = my_list[i[0]] * my_list[i[1]]
        sumed += new_i
        mul += my_list[i[1]]

    result = sumed / mul
    return (result)
