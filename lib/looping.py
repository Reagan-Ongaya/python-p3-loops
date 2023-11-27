#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    
    while countdown > 0:
     print(countdown)
     countdown -= 1
    
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = [num ** 2 for num in int_list]
    return squared_list

input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)

def fizzbuzz(num):
    # code goes here 
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

fizzbuzz_printer()
