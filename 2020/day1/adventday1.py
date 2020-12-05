# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:23:00 2020

@author: Tumtum
"""

from itertools import combinations as c
d=list(map(int,open("input.txt","r").readlines()))
for x,y in c(d,2):
    if x+y==2020:
        print(x)
        print(y)
        # print(z)
        solve = x*y
        print(solve)
        
# print([x*y*z for x,y,z in c(d,3)if x+y+z==2020][0],[x*y*z for x,y,z in c(d,3)if x+y+z==2020][0])
# print([x*(2020-x) for x in d[::2] if 2020-x in d])