# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 12:34:11 2018

@author: sam
"""

users = ["Sam","Mela","Nedim","admin","Sonja"]

for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see the status report?")
    else:
        print("Hello " + user + ", thank you for logging in again")