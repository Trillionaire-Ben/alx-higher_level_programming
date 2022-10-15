#!/usr/bin/python3
def safe_print_division(a, b):
    ''' fn to print the division of two
    integers'''
    try:
        c = float(a / b)
        return (c)
    except (ValueError, ZeroDivisionError):
        return ("None")
    finally:
        print("Inside result: {}".format(c))
