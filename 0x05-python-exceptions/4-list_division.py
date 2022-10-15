#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Write a function that divides element by element 2 lists.
    newlist = []
    for i in range(0, list_length):
        try:
            divd = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divd = 0
        except ZeroDivisionError:
            print("division by 0")
            divd = 0
        except IndexError:
            print("out of range")
            divd = 0
        finally:
            newlist.append(divd)
    return (newlist)
