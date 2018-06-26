# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:48:24 2018

@author: Rasimsson
"""

people = []

person = {'first_name': 'James', 
          'last_name': 'bond',
          'age': '32', 
          'city': 'london'}
people.append(person)

person = {'first_name': 'elbert', 
          'last_name': 'beumstein',
          'age': '64', 
          'city': 'berlin'}
people.append(person)

person = {'first_name': 'jill', 
          'last_name': 'gaste',
          'age': '45', 
          'city': 'silicon valley'}
people.append(person)

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print("\nName: " + full_name)
    print("\nAge: " + age)
    print("\nCity: " + city)