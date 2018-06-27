# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:05:01 2018

@author: Rasimsson
"""

def make_album(artist, title, tracks=''):
    album = {'artist':artist, 'title':title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter an Album:")
    print("(Enter q at any time to quit)")
    
    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    al_name = input("Album name: ")
    if al_name == 'q':
        break    
album = make_album(a_name,al_name)
print(album)    