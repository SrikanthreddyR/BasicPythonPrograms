# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:26:00 2019

Maximum Numeric in a string;

@author: Admin
"""

in_str=input();
x=[];
num=[];
z=[];

for i in range(len(in_str)):
        if(in_str[i]=='0' or in_str[i]=='1' or in_str[i]=='2' or in_str[i]=='3' or in_str[i]=='4' or in_str[i]=='5' or in_str[i]=='6' or in_str[i]=='7' or in_str[i]=='8' or in_str[i]=='9'):
            x.append(in_str[i]);
        else:
            x.append('-');

print(x);

i=0;
while(i<len(x)-1):
    c=0
    while(x[i]!='-'):
        z.append(x[i]);
        if(i<len(x)):
            i=i+1;
            print(i)
        c=1
        
    if(c==1):
        st=''.join(z);
        num.append(st);
    if(x[i]=='-'):
        i=i+1;
    print("i=",i);

print("num=",num)
        
    
    