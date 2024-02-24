#Colin Hillburn, this program takes a user input of five numbers then add, multiplys, and averages them.  It then runs test to confirm the program is running right

import sys
import math

def user_input(): 
    (num1,num2,num3,num4,num5)=input("Please enter 5 numbers ").split(" ")
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    num4 = float(num4)
    num5 = float(num5)
    return num1,num2,num3,num4,num5

def sum(num1,num2,num3,num4,num5):
    sum = num1+num2+num3+num4+num5
    sum=float(sum)
    return sum

def average_number(sum):
    average=sum/5
    return average

def product(num1,num2,num3,num4,num5):
    product=num1*num2*num3*num4*num5
    return product

def maximum(num1,num2,num3,num4,num5):
    if num1>num2 and num1>num3 and num1>num4 and num1>num5:
        max=num1
    if num2>num1 and num2>num3 and num2>num4 and num2>num5:
        max=num2
    if num3>num1 and num3>num2 and num3>num4 and num3>num5:
        max=num3
    if num4>num1 and num4>num2 and num4>num3 and num4>num5:
        max=num4
    if num5>num1 and num5>num2 and num5>num3 and num5>num4:
        max=num5
    return max

def minimum(num1,num2,num3,num4,num5):
    if num1<num2 and num1<num3 and num1<num4 and num1<num5:
        min=num1
    if num2<num1 and num2<num3 and num2<num4 and num2<num5:
        min=num2
    if num3<num1 and num3<num2 and num3<num4 and num3<num5:
        min=num3
    if num4<num1 and num4<num2 and num4<num3 and num4<num5:
        min=num4
    if num5<num1 and num5<num2 and num5<num3 and num5<num4:
        min=num5
    return min
    
def test():
    assert sum(1,2,3,4,5)==15
    assert sum(2,3,4,5,6)==20
    assert average_number(sum(1,1,1,1,1))==1
    assert average_number(sum(2,2,2,2,2))==2
    assert product(1,1,1,1,1)==1
    assert product(0,0,0,0,0)==0
    assert maximum(1,2,3,4,5)==5
    assert maximum(2,3,4,5,6)==6
    assert minimum(1,2,3,4,5)==1
    assert minimum(2,3,4,5,6)==2

def loop():
    answer=input( "Would you like to check some more numbers? Enter y or yes: anything else to quit ")
    while answer == 'y' or answer == 'yes':
         main()
    else:
        print('Thanks for using the program')
        sys.exit
        
        


def main():
     num1,num2,num3,num4,num5=user_input()
     print ("The sum is ",sum(num1,num2,num3,num4,num5))
     print ("The average is ",average_number(sum(num1,num2,num3,num4,num5)))
     print ("The product is ",product(num1,num2,num3,num4,num5))
     print ("The biggest number is ",maximum(num1,num2,num3,num4,num5))
     print ("The smallest number is ",minimum(num1,num2,num3,num4,num5))
     loop()


test()
main()
