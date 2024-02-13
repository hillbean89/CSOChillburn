#function definitions will be above the first running line of code

def greet():
    print("hello world")


def main():#usually this is defined at the very beggining with main()
    # being called as the very first unindented line
    greet()
    fancier_greet("Corin")
    my_name= greet_with_return()
    print(my_name)

def fancier_greet(name):
    '''This is a slightly more complicated function that take a name as an argument
    Also, a triple quoted string like this at the beg. of a function is 
    read by vsCode and displayed as a function
    '''
   
    print("Hello ",name)

def greet_with_return():
    '''this is a fruitful function example that collects a name and returns it to the rest of the program
    '''
    name=input("enter your name: ")
    print("Hello", name)

    return name

#first unindented line that is not a function definion or import beginning of program
main()