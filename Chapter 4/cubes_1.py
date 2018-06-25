# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:52:12 2018

@author: Rasimsson
"""

cubes = []
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)