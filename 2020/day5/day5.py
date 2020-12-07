# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:58:02 2020

@author: Tumtum
"""
from collections import OrderedDict
def splitter(i):
    global rows
    global cols
    if i == "F" or "B":
        if i == "F":
            rows = list(rows[:len(rows)//2])
        elif i == "B":
            rows = list(rows[len(rows)//2:])
    if i == "R" or "L":
        if i == "L":
            cols = list(cols[:len(cols)//2])
        elif i == "R":
            cols = list(cols[len(cols)//2:])
            
inp = [line.rstrip() for line in open('day5')]
stid = OrderedDict()
idns =[]
for seat in inp:
    rows = range(0,128)
    cols = range(0,8)
    for letter in seat:
        splitter(letter)
    idn = (rows[0]*8)+cols[0]
    idns.append(idn)
    stid.update({seat:idn})  
print(max(idns))
idns.sort()
for i, seat in enumerate(idns):
  if i > 0 and idns[i-1]+1 != seat:
    print("Missing:", seat-1)
