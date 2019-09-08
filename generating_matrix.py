# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:56:09 2019

@author: Admin
"""

x,y=input().split();

x=int(x);
y=int(y);
n=x*y;

matrix=[]
for i in range(1,n+1):
    matrix.append(i)

n=len(matrix)
for i in range(n):
    if((i+1)%y!=0):
        print(matrix[i], end=" ")
    else :
       if((i+1)%y==0):
           print(matrix[i], end=" ")
           print();