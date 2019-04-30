#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numero = (number % (10 * -1))
else:
    numero = number % 10
if numero > 5:
    print("Last digit of {} is {} and is greater than 5".
          format(number, numero))
elif numero == 0:
    print("Last digit of {} is {} and is 0".
          format(number, numero))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".
          format(number, numero))
