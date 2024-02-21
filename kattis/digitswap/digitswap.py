'''Written by: Colin Hillburn
2/16/2024
program desc.:  kattis problem enter 2 digits with no space and then have the digits swap places (https://open.kattis.com/problems/digitswap)
algorithm steps
input a 2 digit number with no spaces
switch the position of the intergers '''
import sys
def solution(number):
    first = number[0]
    second = number[1]
    return (second+first)




def main():

    assert(solution("12")=="21")
    assert(solution("32")=="23")
    print('enter a number ',file=sys.stderr)
    number=input()#collects user input number
    ans= solution(number)
    print(ans)

    #print(second+first)#prints numbers in revers of how they were entered
if __name__ == "__main__":
    main()

