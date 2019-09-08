# -*- coding: utf-8 -*-
"""

Upper Traingular square matrix

Created on Thu Mar 21 18:00:55 2019

@author: Admin
"""


def UpTrgMatrix(matrix,num):
    for  i in range(num):
        for j in range (num):
            if (i>j):
                matrix[i][j]=0;
    return matrix;

num=int(input())
mat=[]

for i in range (num):
    x=input().split();
    mat.append(x);

mat=UpTrgMatrix(mat,num);

for i in range(num):
    for j in range(num):
        if (j==num-1):
            print(mat[i][j], end="")
        else:
            print(mat[i][j], end=" ");
        
    if(i<num-1):
        print();