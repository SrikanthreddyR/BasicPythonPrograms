# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:27:20 2019

Guess the movie name

@author: Admin
"""
import random
movies=["tagaru","bellbottom","manasare","gajakesari","vishvasam"];

def play():
    name=list(random.choice(movies));
    print(name);
    user_guess=["_"]*len(name);
    c=0;
    while(1):
        c=c+1;
        print(user_guess,"\n");
        gl=input("Guess and enter the charecter : ");
        g=0;
        for i in range(len(user_guess)):
            if (name[i]==gl):
                user_guess[i]=gl;
                g=1;
                
        if(g==1):
            print("Guessed letter is correct\n",)
        else:
            print("try again");
        
        if(name==user_guess):
            print("The movie name is : ", name);
            break;
    
    return c;

print("The Game is ON");

count=play();

print("No of guesses: ",count);