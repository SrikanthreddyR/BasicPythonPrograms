# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:58:38 2019



@author: Admin
"""


num=int(input())
mat=[]

for i in range (num):
    x=input().split();
    mat.append(x);

result="True";

for i in range (num):
    for j in range (num):
        if (i!=j) and (mat[i][j]!=mat[j][i]):
            result="False"
            break;
if result=="True":
    print("YES");
else :
    print("NO");
    