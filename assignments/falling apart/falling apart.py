import sys, math, random
'''Colin Hillburn, April 17, 2024
Takes two lines of inputs and assigns the highest value to one person then the next highest to bob.  It does this til there are no numbers left from the input
it then adds all of the numbers that each person has and returns the sum'''


def entry():
    n=int(input())
    list=[int(x) for x in input().split()]
    list.sort(reverse=True)
    
    return list
def falling_apart(list):
    alice=0
    bob=0
    
    while list:
        list.remove(max(list))
        alice += max(list)
        #alice.append(max(List))
        #alice_score=sum(alice)
        
        if list:
            list.remove(max(list))
            alice += max(list)
         
    print (alice,bob)
    return alice,bob


#assert falling_aprt()== 4,2
#assert falling_aprt(4,1,2,1,2)==3,3

#def main():
    gimme_dat_money=entry()
    falling_apart(gimme_dat_money)



main()