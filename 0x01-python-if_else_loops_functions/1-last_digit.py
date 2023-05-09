#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = 0
if number >= 0:
    LastDigit = number % 10
else:
    LastDigit = (-number % 10) * -1

msg = f"Last digit of {number} is {LastDigit }"

if LastDigit == 0:
    print(f"{msg} and is 0")
elif LastDigit < 6 and LastDigit != 0:
    print(f"{msg} and is less than 6 and not 0")
elif LastDigit > 5:
    print(f"{msg} and is greater than 5")
