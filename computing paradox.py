# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:52:23 2019

@author: Admin
"""

n=int(input())

songs_list=input();

songs_list=list(map(int,songs_list.split()))

fav_song_pos=int(input())

fav_song=songs_list[fav_song_pos-1]

#print(fav_song,"fav song")

sorted_list=songs_list.copy()

#print(sorted_list,"cpopied");


sorted_list.sort()

#print(sorted_list, "sorted");

for i in range(n):
    if fav_song==sorted_list[i]:
        print(i+1)
        break;