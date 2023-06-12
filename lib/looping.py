#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num = num -1
    if num == 0:
        print("Happy New Year!")


def square_integers(int_list):
    results_list = []
    for i in int_list:
       results_list.append(i * i)
    return results_list


def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 ==0:
            print("FizzBuzz")
        elif num % 3 ==0:
            print("Fizz")
        elif num % 5 ==0:
            print("Buzz")
        else:
            print(num) 
        num+=1
