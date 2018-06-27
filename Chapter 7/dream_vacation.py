# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:26:44 2018

@author: Rasimsson
"""

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("\nIf you could go anywhere in the world, where would it be? " )
    responses[name] = response
    
    repeat = input("Would you like more people to respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ----")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response + ".")
    