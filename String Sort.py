# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:37:34 2019

String Sort

@author: Admin
"""
inp_list=list(map(int,input().split()));

for i in range(len(inp_list)):
    if(inp_list[i]==0):
        del inp_list[i];
        inp_list.append(0);


for i in range(len(inp_list)):
    if (i!=len(inp_list)-1):
        print(inp_list[i],end=" ");
    else:
        print(inp_list[i],end="");