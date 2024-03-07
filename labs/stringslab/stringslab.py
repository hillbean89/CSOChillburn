"""
Lab - String
By: FIXME0

CSCI 110
Date: FIXME0

Program prompts user to enter a phrase and tells the user various properties about the phrase.
"""

import sys
import string

def isReversible(phrase):
    # Function to determine whether given phrase is same forward and backward, i.e.,
    # reversible or not.
    length = len(phrase)  # get the length of phrase
    reversible = True  # lets assume every phrase is reversible!
    j = length - 1 # right index
    for i in range(0, length, 1):  # start at 0 end at length-1, step to increment is 1
        # Algorithm steps:
        # 1. go through each character
        #       a. ignore all the non-alphabetic characters on both ends of the phrase
        # 2. compare the corresponding
        #     characters from left and right of the phrase
        # 3. if a single pair is not equal
        #     the phrase is NOT reversible
        # 4. else, if all the pairs are same, the word is reversible
        if not phrase[i].isalpha():
            continue
        while not phrase[j].isalpha():
            j -= 1
            if j < 0: #if passed the first letter; return False or not reversible
                return True

        if phrase[i] != phrase[j]:
            reversible = False
            break
        j -= 1

    return reversible


def hasLowerCase(phrase):
    for i in range(len(phrase)):
        if phrase[i].islower():
            return True
    return False


def hasUpperCase(phrase):
    for ch in phrase:
        if ch.isupper():
            return True
    return False


def hasDigit(phrase):
    for ch in phrase:
        if ch.isdigit():
            return True

    # FIXME1: return True if phrase has at least 1 digit, false otherwise
    pass


def hasSymbol(phrase):

    for c in phrase:
            if c in string.punctuation:
                return True
    return False

    # FIXME2: return True if phrase has at least one of these symbols: ~!@#$%
    # return False otherwise
    pass


def main():
    print("Program tells various properties of a given phrase")

    while True:
        phrase = input("Enter a word or phrase: ")

        if isReversible(phrase):
            print("{} is reversible!".format(phrase))
        else:
            print("{} is not reversible!".format(phrase))

        # FIXME - # FIXED #
        # print if the phrase has a upper case character by calling the proper function
        if hasLowerCase(phrase):
            print('{} has a lower case character.'.format(phrase))
        else:
            print('{} does not have a lower case character.'.format(phrase))

        # FIXME3
        # print if the phrase has a lower case character by calling the proper function
        if hasUpperCase(phrase):
            print('{} has a upper case character.'.format(phrase))
        else:
            print('{} does not have a upper case character.'.format(phrase))
        # FIXME4
        # print if the phrase has a digit by calling the proper function
        if hasDigit(phrase):
            print('{} has a digit.'.format(phrase))
        else:
            print(('{} does not have a digit.'.format(phrase)))

        # FIXME5
        # print if the phrase has a symbol by calling the proper function
        if hasSymbol(phrase):
            print('{} has a symbol.'.format(phrase))
        else:
            print(('{} does not have a symbol.'.format(phrase)))

        ans = input('Want to continue? [y/n]: ')
        ans = ans.lower()
        #continue of user enters yes or Yes or y or anything that starts with y
        if ans.startswith('y'): 
            continue
        else:
            print('Good bye!')
            break

def test():
    print('run unit test cases...')
    assert isReversible('race car!') == True
    assert isReversible('jeep!') == False
    assert hasLowerCase('Welcome!') == True
    assert hasLowerCase('ABC235!') == False
    assert hasUpperCase('WELcome!!') == True
    assert hasUpperCase('$!#%#@asdfdsf') == False
    assert hasDigit('22424ADSFDS') == True
    assert hasDigit('asdfdsfWASDFASDG') == False
    assert hasSymbol('!@$DAD$%') == True
    assert hasSymbol('asdfASF3424') == False
    print('all test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test()
    else:
        main()