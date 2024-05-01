import random, math, sys,json
import pathlib
my_path=pathlib.Path(__file__).parent.resolve()
def the_list():
    words=[]
    bring_them_to_me=f"{my_path}/{'final2.txt'}"
    with open(bring_them_to_me,'r') as c:
        for line in c.readlines():
            l=line.strip().split('')
            words.append(l)
    the_word=random.choice(l)
    
    return(the_word)
    
def wordle_wish_version(the_word):
    number_of_guess=6
    guess = str(input("Guess the word: "))
    if guess==the_word:
        print("you guessed the word")
    else:
        number_of_guess-=1
        print(f"you didnt guess the word, you have{number_of_guess} left ")
        for c_the_word,c_guess in zip(the_word,guess):
            if c_the_word in guess:
                if c_the_word==c_guess:
                    print(c_the_word.upper(), end='')
                else:
                    print(c_the_word+'!', end='')
            else:
                print(c_guess, end=' ')
    if number_of_guess==1
        print