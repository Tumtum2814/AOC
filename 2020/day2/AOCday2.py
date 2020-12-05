# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:49:55 2020

@author: Tumtum
"""
import pandas
n = 0
d=list(map(str,open("day2.txt","r").readlines()))
print(d[1])
numlow = [None]*len(d)
numhigh = [None]*len(d)
letter = [None]*len(d)
pw = [None]*len(d)
correct = 0
for i in d:
      cnt = 0
      print(n)
      print(d[n])
      temp = d[n]
      templist = str.split(temp)
      templist[1] = templist[1].rstrip(":")
      print(templist)
      num= templist[0]
      num = num.split('-')
      numlow[n] = int(num[0])
      print(numlow[n])
      numhigh[n] =  int(num[1])
      print(numhigh[n])
      letter[n] = templist[1]
      pw[n] = templist[2]
      for i in pw[n]:
          if i == letter[n]:
              cnt += 1
      print(cnt)
      if  numlow[n] <= cnt <= numhigh[n]:
            correct += 1 
            print(correct)
            
      n += 1
      
print(correct)
