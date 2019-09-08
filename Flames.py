# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:16:43 2019.

FLAMES

@author: Admin
"""

Name1=list(input("Enter 1st Name: "));

Name2=list(input("Enter 2nd Name: "));

count=0;
del_count=0;
for i in range(len(Name1)):
    for j in range(len(Name2)):
        if (Name1[i]==Name2[j]):
            Name1[i]="+"
            Name2[j]="*";
            del_count=del_count+1;
            break;

count=len(Name1)+len(Name2)-del_count*2;

print(Name1," ",Name2," ","count=",count);


flames_list=['f','l','a','m','e','s'];

for n in range (5):
    z=[];
    flames_list[(count-1)%len(flames_list)]='-';
    i=(count-1)%len(flames_list);
    for j in range(i+1,len(flames_list)):
        z.append(flames_list[j]);
    for k in range(i):
        z.append(flames_list[k]);
    flames_list=list(z);

print(flames_list);
            
        

