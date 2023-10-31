#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_no = number % 10
elif number < 0:
    last_no = number % -10
if last_no > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_no))
elif last_no == 0:
    print("Last digit of {} is {} and is 0".format(number, last_no))
else:
    print(f"Last digit of {number} is {last_no} and is less than 6 and not 0")
