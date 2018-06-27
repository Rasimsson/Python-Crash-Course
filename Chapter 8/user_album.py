# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:49:03 2018

@author: Rasimsson
"""

def make_album(artist, title, tracks=''):
    album = {'artist':artist, 'title':title}
    if tracks:
        album['tracks'] = tracks
    return album

artist_prompt = "\nInput Artist: "
title_prompt = "Input Albums Title: "
enter_tracks = "Do you want to enter number of tracks too? "
tracks_prompt = "Input Number of Tracks: "


print("Enter q at any time to quit")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break
    
    title = input(title_prompt)
    if title == 'q':
        break
    
    yn_prompt = input(enter_tracks)
    if yn_prompt == 'yes':
        tracks = input(tracks_prompt)
        if tracks == 'q':
            break
        album = make_album(artist,title,tracks)
        print(album)
    else:
        album = make_album(artist,title)
        print(album)

print("Thanks for the input!")