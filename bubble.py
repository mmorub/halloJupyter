#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:05:38 2022

@author: mmo
"""
# sample list for testing
# aList= [55, 7, 78, 12, 42]
aList= [55, 78, 7, 12, 42]
print(f'before sorting aList= {aList}')

lengthList= len(aList)

positionNextSmallest= 0
while positionNextSmallest< lengthList:
    print(f'for positionNextSmallest= {positionNextSmallest}')
    print(f'  aList= {aList}')
    for i in range(lengthList-1, positionNextSmallest, -1):
        if (aList[i]< aList[i-1]):
            aList[i], aList[i-1]= aList[i-1], aList[i]
        print(f'  {i}')
    positionNextSmallest= positionNextSmallest+ 1

print(f'after sorting aList= {aList}')
        