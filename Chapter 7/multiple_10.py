# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:01:33 2018

@author: Rasimsson
"""

your_number = input("Tell me a number, any number: ")
number = int(your_number)

if number % 10 == 0:
    print("Your number: " + str(number) + " is a multiple of 10")
else:
    print("Your number: " + str(number) + " is NOT a multiple of 10")