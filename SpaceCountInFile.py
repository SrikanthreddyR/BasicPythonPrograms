fo=open('C:/Users/rangamma/Music/sample.txt','r')

text=fo.read()
print(text);

count=0;

## Counting number of bank spaces
for i in text:      
    if(i==' '): 
        count=count+1

print(count)
