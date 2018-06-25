# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:01:09 2018

@author: Rasimsson
"""

guests = ["Elon", "Mark", "Bill", "James"]
not_making_it = "James"

for guest in guests:
    print("Dear " + guest + ", please will you join my awesome dinner party?")
print (not_making_it + " Cannot make it!")
  
guests.remove(not_making_it)
guests.append("Dalai")

for guest in guests:
    print("Dear " + guest + ", you are cordially invited to attend my dinner party!")
print("I have found a bigger dinner table!")

guests.insert(0,"Albert")
guests.insert(3,"Steve")
guests.append("Kirk")

for guest in guests:
    print("Dear " + guest + ", you are invited to my awesome dinner party with a bigger table!")