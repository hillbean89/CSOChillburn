'''This program will take a users input and use it as a key to identify a 5 letter word.  It will then give the user 5 guesses.
if the user does not guess the answer then they lose the game'''


import random, math, sys,json
import pathlib
my_path=pathlib.Path(__file__).parent.resolve()
def libraries():
    clues=f"{my_path}/{'clues.txt'}"
    jumble=f"{my_path}/{'jumble_clue.txt'}"
    wordle=f"{my_path}/{'wordle_dictionary.txt'}"
    #filename2="wordle_dictionary.txt"
    #filename3="jumble_clue.txt"
    with open(clues,'r') as c:
        for line in c.readlines():
            l=line.strip().split(',')
            l_string=''.join(map(str,l))
            clues_dictionary=json.loads(l_string)
            
    with open(jumble, 'r') as j:
        for line in j.readlines():
            jl=line.strip().split(',')
            jl_string=''.join(map(str,jl))
            jumbled_hogwashdictionary=json.loads(jl_string)
    with open(wordle, 'r') as w:
        for line in w.readlines():
            wl=line.strip().split(',')
            wl_string=''.join(map(str,wl))
            wordle_dictionary=json.loads(wl_string)
    clue=clues_dictionary
    jumbled_clue=jumbled_hogwashdictionary
    word=wordle_dictionary        
    print(clue)
    print(jumbled_clue)
    print(word)
    return  clue,jumbled_clue,word
    

'''def input():
    user_input= print("Pick a capital letter from the alphabet: ")
    return user_input

def My_winkie_is_a_key(user_input,clue,jumbled_clue,word):
    the_word=[]
    the_clue=[]
    jumbled_cluelist=[]
    
    if user_input in clue:
        riddle=the_clue.append(user_input)
        return riddle
    if user_input in jumbled_clue:
        jumbled=jumbled_cluelist.append(user_input)
        return jumbled
    if user_input in word:
        word=the_word.append(user_input)
        return word
    thirdguess_clue=riddle
    fourth_guess=jumbled
    word_for_the_game=word
    
    return word_for_the_game,thirdguess_clue,fourth_guess


def wordle_wish_version(word_for_the_game,thirdguess_clue,fourth_guess):'''

libraries()