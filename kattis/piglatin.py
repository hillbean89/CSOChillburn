def piglatin(word: str):
    vowels=['a','e','i','o','u']
    if(word[0] in vowels):
            word= word + 'yay'
    else:
        index=0
        for c in word:
            index+=1
            if c in vowels:
                beg=word[0:index]
                word = word[index::]+beg+'ay'
                break
    return word

words= input().split()
print (words)
for word in words:
     translation= piglatin(word)
     print(translation, end=' ')
