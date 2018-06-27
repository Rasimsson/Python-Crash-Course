# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:28:40 2018

@author: Rasimsson
"""

def make_album(artist, title, tracks=''):
    album = {'artist':artist, 'title':title}
    if tracks:
        album['tracks'] = tracks
    return album

album = make_album('metallica','death magnetic')
print(album)
album = make_album('children of bodom','follow the reaper', '9')
print(album)
album = make_album('slipknot','iowa')
print(album)

