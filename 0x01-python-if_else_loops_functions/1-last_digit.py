#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = int(repr(number)[-1])

if(number < 0):
    lastdig = -lastdig
print(f"Last digit of {number:d} is {lastdig:d} and is ", end="")
if(lastdig > 5):
    print("greater than 5")
elif(lastdig == 0):
    print("0")
elif(lastdig < 6 and not 0):
     print("less than 6 and not 0")
