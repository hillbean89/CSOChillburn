import random, math, sys,json
import pathlib
my_path=pathlib.Path(__file__).parent.resolve()
print('Wordle is a game where you guess a word with 5 letters.  If the letter is in the word it prints yellow, if its in the right place it prints the letter green, if its not in the word it prints a dash')
def the_list():
    words=[]
    bring_them_to_me=f"{my_path}/{'final2.txt'}" #makes a path to go and find the text document with my words in it 
    with open(bring_them_to_me,'r') as c:  #opens the document as a read document as c
        for line in c.readlines():      #this function strips and seperates the lines from the text doc then appends them to a list
            l=line.strip().split(' ')
            words.append(l)
    the_word=random.choice(l) #goes through the words and randomly selects one and sets it as variable the word
    
    return(the_word) #returns the word so it can be used in another function
    
def wordle_wish_version(the_word):  #this function compares a users guess to the randomly selected word.  If the letter is not in the word it prints a blank spac.
    number_of_guess=6               #if the letter is in the right place it prints it as green    
    GREEN = '\033[32m'              #if the letter is in the guess and the word but in the wrong place it prints that letter yellow
    RED = '\033[31m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    while number_of_guess>0:
        guess = str(input("Please guess a 5 letter word word: "))#prompts the user to enter a word
        
        if guess==the_word:   #if they guess the word it says you guessed the word then breaks the loop and ends the program
            print("you guessed the word")
            break
        else:
            number_of_guess-=1 #everytime the user makes a guess, it subtracts one from guesses taken then prints how many guesses they have left
            print(f"you didnt guess the word, you have {number_of_guess} left ")
            for c_the_word,c_guess in zip(the_word,guess):#zip takes two arguments and then passes them as iterables, then creates a an iterable that turns into a pair of variables E.G. 
                    #d1=[1,2,3] d2=['a','b','c']zip(d1,d2)= [1:a,2:b,3:c]
                    #this function goes through the_word and the guess and compares them to each other. If there are characters that match they get 
                                                        #stored as a seperate variable each time
                #if c_the_word in guess:
                    if c_guess in the_word and c_guess in c_the_word:          #if c_the_word==c_guess original code written with help
                        #if the guess is in the_word and in c_the word it compares the two varialbes and if the letter placement matches it prints that letter green
                        
                        print(GREEN+c_the_word+WHITE, end=''" ")
                        
                        
                        #print(WHITE, end='')
                        #print()

                    elif c_guess in the_word:                     # original code written with help if c_guess==c_the_word:
                        print(YELLOW+c_guess+WHITE,end=''" ")
                        #if the c_guess variable is just in the_word but not in c_the_word it knows that the variable is in both but not in the right place.  It prints the letter in yellow
                        
                    else:
                        print('_', end=''" ")
                    #if none of the other conditions are met then the letter is not in any of the variables and it prints a white dash in the guess
        if number_of_guess==1:  #if it is on their last guess this functions prints a hint by printing the word in random order
            s=the_word #makes the word equal to s
            s_the_word=''.join(random.sample(s,len(s))) #takes s and then joins it in a random order through the entire length of s making s_the_word the_word printed in random order
            print(s_the_word)  #prints s_the_word
            
        if number_of_guess==0:#after all the guesses if the user isnt right it prints the answer and tells them they did not get it 
            print(f"You didnt get it, the answer was {the_word}")
            break

def main():
    the_juice=the_list()#sets the_juice as the_word
    #print(the_juice)
    the_game=wordle_wish_version(the_juice)#passes the_juice into the game and then allows the user to play the game
    


main()  #calls and runs the main function
