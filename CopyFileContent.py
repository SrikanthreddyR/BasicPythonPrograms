fo=open('sample.txt','r')

s=fo.read()

print(s,'\n')

fo.close()

fc=open('samplecopy.txt','w+')

fc.write(s)

fc.seek(0)

print(fc.read())