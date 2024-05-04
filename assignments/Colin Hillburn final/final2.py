import random, math, sys,json
import pathlib
my_path=pathlib.Path(__file__).parent.resolve()
def the_list():
    words=[]
    bring_them_to_me=f"{my_path}/{'final2.txt'}"
    with open(bring_them_to_me,'r') as c:
        for line in c.readlines():
            l=line.strip().split(' ')
            words.append(l)
    the_word=random.choice(l)
    
    return(the_word)
    
def wordle_wish_version(the_word):
    number_of_guess=6
    GREEN = '\033[32m'
    RED = '\033[31m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    while number_of_guess>0:
        guess = str(input("Guess the word: "))
        
        if guess==the_word:
            print("you guessed the word")
            break
        else:
            number_of_guess-=1
            print(f"you didnt guess the word, you have {number_of_guess} left ")
            for c_the_word,c_guess in zip(the_word,guess):
            
                #if c_the_word in guess:
                    if c_guess in the_word and c_guess in c_the_word:          #if c_the_word==c_guess original code written with help
                        #print(c_the_word,)
                        #print(GREEN, end='')
                        print(GREEN+c_the_word+WHITE, end=''" ")
                        
                        
                        #print(WHITE, end='')
                        #print()

                    elif c_guess in the_word:                     # original code written with help if c_guess==c_the_word:
                        print(YELLOW+c_guess+WHITE,end=''" ")
                        
                        
                    else:
                        print('_', end=''" ")
                    
        if number_of_guess==1:
            print(the_word[::-1])
        if number_of_guess==0:
            print(f"You didnt get it, the answer was {the_word}")
            break

def main():
    the_juice=the_list()
    print(the_juice)
    the_game=wordle_wish_version(the_juice)
    


main()
