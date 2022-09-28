#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    dic = {"+": add, "*": mul, "-": sub, "/": div}
    if sys.argv[2] not in list(dic.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, dic[sys.argv[2]](a, b)))
