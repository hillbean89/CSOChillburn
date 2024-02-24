'''Colin Hillburn, this program will take a user input and add, subtract, multiply, divide those numbers then run asserts to test itself'''
import sys
import math

num1,num2=input("please enter two numbers ").split(" ")
num1= float(num1)
num2= float(num2)


def add(num1,num2):
    sum = num1+num2
    return sum

def multiply(num1,num2):
    product=num1*num2
    return product

def divide(num1,num2):
    quotient=num1/num2
    return quotient
def subtract(num1,num2):
    difference=num1-num2
    return difference

#def numbers(num1,num2):
    num1,num2=input("please enter two numbers ").split(" ")
    num1,num2= float

def power (num1,num2):
    exponent=num1**num2
    return exponent

def square_root(num1):
    answer= math.sqrt(num1)
    return answer

def maximum(num1,num2):
    if num1==num2:
        return ("your numbers are equal")
    return f"your biggest number is, {max(num1,num2)}"

    
    



def test():
    assert add(1,2)==3
    assert add(3,4)==7
    assert square_root(4)==2
    assert square_root(9)==3
    assert power(3,2)==9
    assert power(3,4)==81
    assert subtract(3,2)==1
    assert subtract(5,2)==3
    assert multiply(4,2)==8
    assert multiply(3,9)==27
    assert divide(14,2)==7
    assert divide(4,8)==.5
    return print("all test have passed")

test()

def main ():
    print ("Your first number to the power of your second number is", power(num1,num2))
    print ("The sqaure root of your first number is ", square_root(num1))
    print ("The sum is ",add(num1,num2))
    print ("The product is ",multiply(num1,num2))
    print ("The difference is ",subtract(num1,num2))
    print (maximum(num1,num2))
    

main()