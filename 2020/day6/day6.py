# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:10:31 2020

@author: Tumtum
"""

import re
with open('day6', 'r') as file:
    groups = file.read().split("\n\n")
total = 0
hivemind = 0
# Day6 A
for group in groups:
    pattern=r"\s+"
    temp = re.sub(pattern, "", group)
    letters = set(list(map(str.strip,temp)))
    cnt = len(letters)
    total += cnt
    peep = group.splitlines()
    numpeeps = len(peep)
    for letter in letters:
        lettercnt = 0
        for answer in peep:
            lettercnt += answer.count(letter)
        if lettercnt == numpeeps:
            hivemind += 1   
print("sum of all yeses across groups:",total)
print("sum of all common yeses across groups:",hivemind)

    