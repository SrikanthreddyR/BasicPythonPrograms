fo=open('sample.txt','r+')

l=fo.read().split()

## Capitalize first letter of every word
for i in range(len(l)):
    l[i]=l[i].capitalize()

s=" ".join(l)

fo.seek(0)

fo.write(s)

fo.seek(0)

print(fo.read())