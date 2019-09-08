# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:04:42 2019

@author: Admin
"""

def rectangle(z):
    count=0;
    a=z[0];
    b=z[1];
    c=z[2];
    d=z[3];
    if((a==b or a==c or a==d)):
        if ((a==b and c==d) or (a==c and b==d) or (a==d and b==c )):
            count=1;
    if (count==1):
        return "YES"
        print("YES");
    else:
        return "NO"
        print("NO");

t=int(input());

for i in range(t):
    l=list(map(int,input().split()));
    rectangle(l);