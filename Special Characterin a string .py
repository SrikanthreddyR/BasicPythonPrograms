# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:44:45 2019

Special Character in a string

@author: Admin
"""

s=input();

s_list=list(s);

c=0;

for i in range(len(s_list)):
    if (((ord(s_list[i])>=65) and (ord(s_list[i])<=90)) or ((ord(s_list[i])>=97) and (ord(s_list[i])<=122)) or ((ord(s_list[i])>=48) and (ord(s_list[i])<=57)) or (ord(s_list[i])==32)):
        c=0;
    else:
        c=1;
        break;

if c==0:
    print("NO");
else:   
    print("YES");
    
        
