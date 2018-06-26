# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:04:51 2018

@author: Rasimsson
"""

prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\n(Type q to quit when you are done): "

while True:
    toppings = input(prompt)
    
    if toppings == 'q':
        break
    else:
        print("Adding your pizza topping: " + toppings.title())