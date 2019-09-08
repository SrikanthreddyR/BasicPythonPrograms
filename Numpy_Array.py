# -*- coding: utf-8 -*-
"""



Created on Tue Mar 19 17:32:50 2019

@author: Admin
"""



import numpy


magic_square=numpy.array([[1,2,3],[4,5,6],[7,8,9]])

for i in range(3):
    for j in range(3):
        print(magic_square[i][j], end=" ");
    print();
