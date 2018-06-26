# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:59:06 2018

@author: Rasimsson
"""

number_of_people = input("How many in your group? ")
number = int(number_of_people)
if number > 8:
    print("You will have to wait for a table!")
else:
    print("Your table is available")