fo=open('C:/Users/rangamma/Music/sample.txt','r')

text=fo.read()

l=list(text.split()) ## Splitting text into words

print('Word Count:',len(l))

fo.close()
