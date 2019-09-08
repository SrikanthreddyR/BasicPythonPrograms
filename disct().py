# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:35:05 2019

@author: Admin
"""
#import string

#s=string.ascii_letters

##print(s)

#print(s[-4]);

#print(int(li))...


def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
print(test(4,7))