# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:14:26 2018

@author: Rasimsson
"""

glossary = {'slice': 'The slice object is used to slice a given sequence',
            'string': 'Data type in Python that stores text',
            'tuple': 'An immutable ordered sequence of values',
            'attribute': 'Values associated with an individual object',
            'integer': 'Date type in Python that stores whole numbers',
            'loop': 'iteration over the members of a sequence in order, executing each block',
            'value': 'items associated with keys in dictionary'}

for word, description in glossary.items():
    print("\n" + word.title() + ": " + description)
