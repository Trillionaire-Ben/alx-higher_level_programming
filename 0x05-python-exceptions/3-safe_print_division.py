#!/usr/bin/python3
def safe_print_division(a, b):
    ''' fn to print the division of two
    integers'''
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return (c)
