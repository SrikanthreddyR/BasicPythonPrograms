# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:59:58 2019

@author: Admin
"""


import random

n=int(input());
given_list=[]

for i in range (n):
    given_list.append(int(input()))
    
sorted_list=given_list.copy()
sorted_list.sort()

while(1):
    i=random.randint(0,n-1);
    j=random.randint(0,n-1);
    
    x=given_list[i];
    given_list[i]=given_list[j];
    given_list[j]=x;
    
    if(given_list==sorted_list):
        for i in given_list:
            print(i,end=" ")
        break;
        
    


