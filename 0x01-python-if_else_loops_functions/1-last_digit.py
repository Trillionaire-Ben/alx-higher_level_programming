#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = int(repr(number)[-1])

if(lastdig > 5):
    print(f"Last digits of {number} is {lastdig} and is greater than 5")
elif(lastdig == 0):
    print(f"Last digits of {number} is {lastdig} and is zero")
elif(lastdig < 6 and not 0):
    print(f"Last digits of {number} is {lastdig} and is less than 6 and not 0")
