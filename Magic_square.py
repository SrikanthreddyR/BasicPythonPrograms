"""

Magic Square 


Created on Tue Mar 19 17:50:14 2019

@author: Admin
"""

n=int(input());

#list_length=n*n;

magic_square=[];

for i in range (n*n):
    magic_square.append("-");
        

def index(p,q,i):
    pos=p*n+q;
    
    if(magic_square[pos]=="-"):
        magic_square[pos]=i;
    else:
        p=p+1;
        q=q-2;
        index(p,q,i);

for i in range (1,n*n):
    if(i==1):
        p=int(n/2);
        q=n-1;
        index(p,q,i);
    else:
        p=p-1;
        q=q+1;
        
        if(p==-1 and q==n):
            p=0;
            q=n-1;
            index(p,q,i);
        
        elif(p==-1):
            p=n-1;
            index(p,q,i);
            
        elif(q==n):
            q=0;
            index(p,q,i);
        else:
            index(p,q,i);

print(magic_square);
    