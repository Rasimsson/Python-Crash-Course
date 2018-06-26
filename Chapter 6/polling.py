# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:31:29 2018

@author: Rasimsson
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['james', 'steve', 'bill', 'albert', 'jen', 'phil']

for name in people:
    if name in favorite_languages.keys():
        print("Thank you " + name.title() + " for taking the poll!")
    else:
        print("Hi " + name.title() + ", please take the poll to let us know what your favorite language is!")
