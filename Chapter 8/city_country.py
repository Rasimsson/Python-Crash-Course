# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:09:26 2018

@author: Rasimsson
"""

def city_country(city,country):
    formatted = city + ', ' + country
    return formatted.title()

cityandcountry = city_country('london','england')
print(cityandcountry)
cityandcountry = city_country('bergen','norway')
print(cityandcountry)
cityandcountry = city_country('stockholm','sweden')
print(cityandcountry)