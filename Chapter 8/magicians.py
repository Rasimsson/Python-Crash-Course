# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:52:58 2018

@author: Rasimsson
"""

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ['david','sam','harry']

show_magicians(magicians)