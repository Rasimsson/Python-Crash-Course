# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:58:20 2018

@author: Rasimsson
"""

def describe_city(city_name,country="Norway"):
    print(city_name + " is in " + country)

describe_city(city_name="Bergen")
describe_city(city_name="Oslo")
describe_city(city_name="Reykjavik", country="Iceland")