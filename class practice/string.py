random_word="skiing"
print("random word is")
for c in random_word:
    print(c, end = ' ')

guess='i'

for c in random_word:
    if(guess == c):
        print(c, end=' ')
    else:
        print('_', end=' ')

print()