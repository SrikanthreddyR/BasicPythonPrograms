fo=open('C:/Users/rangamma/Music/sample.txt','r')

l=fo.readlines()

f=[]
for i in l:
    if (i!='\n'):
        if('\n' in i):
            f.append(i[:len(i)-2])
        else:
            ## If \n is not present at the end of the file, i.e. after last line in the file
            f.append(i)
fo.close()

entstr=". ".join(f)   ## To convert the list of lines to single string

fo=open('sample.txt','w+')

fo.write(entstr)

fo.seek(0)

print(fo.read())
