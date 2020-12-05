# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:09:15 2020

@author: Tumtum
"""



inp = [line.rstrip() for line in open('day3')]
def gps(inp, lat, long):
  x, y, cnt = 0, 0, 0
  for i in inp[::long]:
    if inp[y][x % len(inp[0])] == '#':
      cnt +=1
    x += lat 
    y += long
  return cnt
print(inp)
print("part1:", gps(inp,3,1))
print("part2:", gps(inp,1,1)*gps(inp,3,1)*gps(inp,5,1)*gps(inp,7,1)*gps(inp,1,2))