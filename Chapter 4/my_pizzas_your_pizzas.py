# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:06:54 2018

@author: Rasimsson
"""

my_pizzas = ['Pepperoni', 'Mozarella', 'Naepolitana', 'Funghi', 'Hawaiian']
friends_pizzas = my_pizzas[:]

my_pizzas.append('BBQ')
friends_pizzas.append('Seafood')

print("My favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)