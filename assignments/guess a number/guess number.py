import random
def greeting():
    name=input("What is your name????")
    print('nice meeting you', name)

#number=random.randint(1,20)
#print(number)
#if guess<number:
    #print('you guessed to low')
#if guess>number:
    #print('your guess is to high')
#else:
    #print('You bet your sweet cheeks thats the number')
def game():
    take_guess=1
    number=random.randint(1,20)
    tries=1
    right=0
    
    while take_guess<6:
        guess=input('Pick a number between 1 and 20 ')
        guess=int(guess)
        if guess<number:
            print('you guessed to low',)
            take_guess+=1
            
            
        elif guess>number:
            print('your guess is to high',)
            take_guess+=1

        if guess==number:
            print('Yay you guessed my number in', take_guess, ' tries')
            

            
            break 


    
    if take_guess==6:
            print('thank you for trying, the number is ',number)
            SystemExit

def main():
    game()


greeting()

if __name__=="__main__":
    while True:
        main()
        answer= input( "Would you like to check some more numbers? Enter y or yes: anything else to quit ")
        if answer=="y" or answer=="yes":
            continue
        else:
            print('Thanks for using the program')
            break
