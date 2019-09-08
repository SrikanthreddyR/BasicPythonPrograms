# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:26:00 2019

Maximum Numeric in a string;

@author: Admin
"""


"""          for j in range(i,len(in_str)):
                if(in_str[i]=='0' or in_str[i]=='1' or in_str[i]=='2' or in_str[i]=='3' or in_str[i]=='4' or in_str[i]=='5' or in_str[i]=='6' or in_str[i]=='7' or in_str[i]=='8' or in_str[i]=='9'):
                    x.append(in_str[i]);
                else:
                    break;
            st=''.join(x);
            num.append(st);
"""


in_str=input();

num=[];
x=[];

for i in range(len(in_str)):
        if(in_str[i]=='0' or in_str[i]=='1' or in_str[i]=='2' or in_str[i]=='3' or in_str[i]=='4' or in_str[i]=='5' or in_str[i]=='6' or in_str[i]=='7' or in_str[i]=='8' or in_str[i]=='9'):
            x.append(in_str[i]);

        else:
            x.append('-'); 
        
print(x);