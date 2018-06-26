# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:31:38 2018

@author: rasimsson
"""
    
current_users = ["Sam","Mela","Nedim","Ema","Sonja"]
new_users = ["Nadia","Semra","Svjetlana","SAM","MEla"]

for new_user in new_users:
    if new_user.title() in current_users:
        print("Please enter a new username!")
    else:
        print("Username available")