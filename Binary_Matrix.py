# -*- coding: utf-8 -*-
"""

Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix.
A binary matrix is a matrix in which all the elements are either 0 or 1

Created on Thu Mar 21 19:21:14 2019

@author: Admin
"""

N, M=input().split();
mat=[];

N=int(N);
M=int(M);

for i in range (N):
    x=list(map(int,input().split()));
    mat.append(x);
    
result="True";

for i in range (N):
    for j in range (M):
        if (mat[i][j]!=0) and (mat[i][j]!=1):
            result="False"
            break;
            
if result=="True":
    print("YES",end="");
else :
    print("NO",end=""); 