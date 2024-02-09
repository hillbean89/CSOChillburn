a, b, c =(input('Give me 3 numbers, ')).split(' ')
(a,b,c)=sorted([a,b,c})
print(string.ascii_letters)
print(string.hexdigits)
print(string.punctuation)

a = "1"

print(a in string.digits)
print(a in string.ascii_letters)

print(string.capwords(('title of movie is')))
phrase = "hello wor'ld!"
for c in phrase:
    if(c not in string.punctuation):
        new_phrase=c

def main():
