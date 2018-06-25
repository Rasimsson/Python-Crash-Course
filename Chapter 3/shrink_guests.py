# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:02:34 2018

@author: Rasimsson
"""

guests = ["Albert", "Elon", "Mark", "Steve", "Bill", "Dalai", "Kirk"]

for guest in guests:
    print("Dear " + guest + ", sadly I can only invite two guests to my dinner!")

popped_guest = guests.pop()
print ("Dear " + popped_guest + ", you are no longer invited")
popped_guest = guests.pop()
print ("Dear " + popped_guest + ", you are no longer invited")
popped_guest = guests.pop()
print ("Dear " + popped_guest + ", you are no longer invited")
popped_guest = guests.pop()
print ("Dear " + popped_guest + ", you are no longer invited")
popped_guest = guests.pop()
print ("Dear " + popped_guest + ", you are no longer invited")

for guest in guests:
    print("Dear " + guest + ", you are still invitited and I look forward to it!")

del guests[1]
del guests[0]

print(guests)