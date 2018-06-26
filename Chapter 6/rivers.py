# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:22:51 2018

@author: sam
"""

rivers = {'tigris': 'iraq',
          'chao praya': 'thailand',
          'danube': 'serbia'}

for river, country in rivers.items():
    print("\nThe River " + river.title() + " runs through " + country.title())

print("\nRivers:")
for river in rivers.keys():
    print("\n - " + river.title())

print("\nCountries:")
for country in rivers.values():
    print("\n - " + country.title())
    