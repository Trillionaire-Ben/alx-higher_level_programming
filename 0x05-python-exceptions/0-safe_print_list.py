#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret_value = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret_value++
        except IndexError:
            break
    print("")
    return (ret_value)
