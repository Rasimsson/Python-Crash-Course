# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:11:58 2018

@author: Rasimsson
"""

prompt = "\nTell us your age and we will tell you the price of a movie ticket! "
prompt += "\n(Type q to quit when you are done): "

while True:
    age = input(prompt)
    
    if age == 'q':
        break
    else:
        if int(age) < 3:
            print("Your ticket is free!")
        elif int(age) < 12:
            print("Your ticket cost is: $10")
        else:
            print("Your ticket price is $15")

