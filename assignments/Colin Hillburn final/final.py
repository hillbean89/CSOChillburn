'''This program will take a users input and use it as a key to identify a 5 letter word.  It will then give the user 5 guesses.
if the user does not guess the answer then they lose the game'''


import random, math, sys
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
            clues_dictionary={l}
            
    with open(jumble, 'r') as j:
        for line in j.readlines():
            jl=line.strip().split(',')
            jumbled_hogwash={jl}
    with open(wordle, 'r') as w:
        for line in w.readlines():
            wl=line.strip().split(',')
            wordle_dictionary={wl}
            
    return jumbled_hogwash,clues_dictionary,wordle_dictionary

'''def input():
    user_input= print("Pick a capital letter from the alphabet: ")
    return user_input

def My_winkie_is_a_key(user_input):
    if user_input in clues_dictinoary:
        
libraries()'''