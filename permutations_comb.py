# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:32:51 2019

@author: Admin
"""

#from itertools import permutations 

n,m=map(int,input().split());

inp_list=list(map(int,input().split()));

#perm = permutations(inp_list, m) 
#  
#perm=list(perm);
#
#val_list=[];
#
#for i in range(len(perm)):
#    s=sorted(perm[i]);
#    val=s[m-1]-s[0];
#    val_list.append(val);
#    
#val_list=sorted(val_list);
#
#print(val_list[0]);


import sys; 
  
# arr[0..n-1] represents sizes of packets 
# m is number of students. 
# Returns minimum difference between maximum 
# and minimum values of distribution. 
def findMinDiff(arr, n, m): 
  
    # if there are no chocolates or number 
    # of students is 0 
    if (m==0 or n==0): 
        return 0
  
    # Sort the given packets 
    arr.sort() 
  
    # Number of students cannot be more than 
    # number of packets 
    if (n < m): 
        return -1
  
    # Largest number of chocolates 
    min_diff = sys.maxsize 
  
    # Find the subarray of size m such that 
    # difference between last (maximum in case 
    # of sorted) and first (minimum in case of 
    # sorted) elements of subarray is minimum. 
    first = 0
    last = 0
    i=0
    while(i+m-1<n ): 
      
        diff = arr[i+m-1] - arr[i] 
        if (diff < min_diff): 
          
            min_diff = diff 
            first = i 
            last = i + m - 1
          
        i+=1
          
    return (arr[last] - arr[first]) 
  
# Driver Code 
if __name__ == "__main__": 
    print(findMinDiff(inp_list, n, m))