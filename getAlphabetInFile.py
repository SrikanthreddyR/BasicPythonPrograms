fo= open("alphabetInFile.txt","w+")

def alphabetInFile(count,n):
    for i in range(count,n+count):
        while(i>90):
            i=i-26;
        fo.write(chr(i)+" ")
    fo.write("\n")

count=65;
while(True):
    m=input('Wanna enter a value ? Enter T\F: ')
    if(m=="T" or m=="t"):
        n=int(input('Enter a number'));
        alphabetInFile(count,n)
        count=count+n;
    else:
        fo.close()
        break