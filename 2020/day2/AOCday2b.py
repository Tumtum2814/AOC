# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:49:55 2020

@author: Tumtum
"""
n = 0
d=list(map(str,open("day2.txt","r").readlines()))
#print(d[1])
numlow = [None]*len(d)
numhigh = [None]*len(d)
letter = [None]*len(d)
pw = [None]*len(d)
correct = 0
for i in d:
      cnt = 0
      temp = d[n]
      templist = str.split(temp)
      templist[1] = templist[1].rstrip(":")
      num= templist[0].split('-')
      nl = numlow[n] = int(num[0])
      nh = numhigh[n] =  int(num[1])
      lt = letter[n] = templist[1]
      passwd = pw[n] = templist[2]
      m=1
      for i in passwd:
         if i == lt and m == nl:
          cnt += 1 
         elif i == lt and m == nh:
          cnt += 1
         m += 1
      if  0< cnt <2:
            correct += 1 
      n += 1
      
print(correct)
