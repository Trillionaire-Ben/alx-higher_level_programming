#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = int(repr(number)[-1])

if(lastdig > 5):
    print("Last digits of {0} is {1} and is greater than 5".format(number, lastdig))
elif(lastdig == 0):
    print("Last digits of {0} is {1} and is zero".format(number, lastdig))
elif(lastdig < 6 and not 0):
    print("Last digits of {0} is {1} and is less than 6 and not 0".format(number, lastdig))
