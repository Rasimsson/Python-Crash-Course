# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:16:04 2018

@author: Rasimsson
"""

locations = ['Kyoto', 'Beijing', 'Seoul', 'Ontario', 'Sydney']
print("This is the unsorted list:")
print(locations)

print("\nThis is the sorted list:")
print(sorted(locations))

print("\nAs you can see the original remains:")
print(locations)

locations.reverse()
print("\nThe list is now reversed:")
print(locations)

locations.reverse()
print("\nReversed once more:")
print(locations)

locations.sort()
print("\nSorted:")
print(locations)

locations.sort(reverse=True)
print("\nSorted again in reverse")
print(locations)