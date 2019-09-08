# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:13:04 2019

Calculate Q = Square root of [(2 * C * D)/H]

@author: Admin
"""

import math

x=input();

inp_list=list(map(int,x.split(",")));

for i in range(len(inp_list)):
    res=round(math.sqrt((2*50*inp_list[i])/30));
    if(i!=len(inp_list)-1):
        print(res,end=",");
    else:
        print(res,end="");
    
    
