# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:34:13 2019

Jumps

@author: Admin
"""

num=int(input());

val=0;

ans=0;

mod=num%6;

if (mod==1 or mod==3 or mod==0):
    print("YES")
else:
    print("NO")

'''
while(val<num):
    val=val+1;
    if (val==num):
        ans=1;
        break;
        
    val=val+2;
    if (val==num):
        ans=1;
        break;
        
    val=val+3;
    if (val==num):
        ans=1;
        break;
        
    print(val)

if (ans==1):
    print("YES");
else:
    print("NO");
    
'''