#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater_than_5 = "Last digit of {} is {} and is greater than 5"
less_6_not_0 = "Last digit of {} is {} and is less than 6 and not 0"
if (number >= 0):
    if (number % 10 > 5):
        print(greater_than_5.format(number, number % 10))
    if (number % 10 == 0):
        print("Last digit of {} is {} and is 0".format(number, number % 10))
    elif(number % 10 < 6 and number % 10 != 0):
        print(less_6_not_0.format(number, number % 10))
else:
    if (number % -10 == 0):
        print("Last digit of {} is {} and is 0".format(number, number % 10))
    else:
        print(less_6_not_0.format(number, number % -10))
