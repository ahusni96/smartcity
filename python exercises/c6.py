import random

# FizzBuzzMeow appear at 105
for num in range(1, 106):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print("FizzBuzzMeow")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 7 == 0:
        print("Meow")
    else:
        print(num)
