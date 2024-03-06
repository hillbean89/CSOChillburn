word=input()
found=False
for x in range(len(word)-1):
    if word[x]=='s':
        if word[x+1]=='s':
            found=True

if found==True:
    print('hiss')
else:
    print('no hiss')
