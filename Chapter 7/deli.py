# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:04:38 2018

@author: Rasimsson
"""

sandwich_orders = ['pastrami', 'veggie', 'cheese', 'meatlovers']
finished_sandwiches = []

while sandwich_orders:
    current_sandwhich = sandwich_orders.pop()
    print('Currently preparing a ' + current_sandwhich.title())
    finished_sandwiches.append(current_sandwhich)
print('\nThe following sandwhiches have been prepared:')
for sandwiches in finished_sandwiches:
    print(sandwiches.title())
