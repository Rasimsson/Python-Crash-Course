# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:31:16 2018

@author: rasimsson
"""


    
current_users = ["Sam","Mela","Nedim","Ema","Sonja"]
new_users = ["Nadia","Semra","Svjetlana","SAM","Mela"]

for new_user in new_users:
    if new_user.title() in current_users:
        print("Please enter a new username!")
    else:
        print("Username available")


