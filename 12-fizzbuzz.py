#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz".format(), end=' ')
        elif num % 5 == 0:
            print ("Buzz".format(), end=' ')
        elif num % 3 == 0:
            print("Fizz".format(), end=' ')
        else:
            print(num, end=' ')
