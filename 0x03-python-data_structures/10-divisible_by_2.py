#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # it runs with a list as input
    # create new list to store bool value of output
    new_list = []
    # check if element in input is divisble by 2
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append("True")
        else:
            new_list.append(False)
    return new_list
