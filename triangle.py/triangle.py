#Colin Hillburn, this program will ask the user for 3 numbers and then calculate the area and perimeter of the trianngle.  Once thats done it will tell the user if they made a triangle or not
import math
num1,num2,num3=input('please give me a three numbers ').split(' ')
num1,num2,num3=float(num1),float(num2),float(num3)

#num2=float(input('please give me a second number '))#changed code for a better user input
#num3=float(input('What is your last number? '))# changed code for a better user input
area=(num1+num2+num3)/2 #this is the formula for the area of a triangle
perimeter= (num1+num2+num3) #this is the formula for  the perimeter of a traingle
str(area)#I have to convert my area from a float to a string so that it can be printed as a text
str(perimeter)# convert perimeter from float to string so that it prints 
print("the area of your triangle is", area)
print("the perimeter of your triangle is",perimeter)
print('Now lets see if you made a real triangle or not!!!')
if (num1==num2==num3):
    print("You made an Isoceles Triangle\n")
    print('   0\n  000\n 00000\n0000000')
    exit()
    
#if all sides are equal its an isoceles triganlge, Set this first so that program does not need to assign values if the statement is true and the program ends
def maximum (num1,num2,num3):
    if (num1>=num2) and (num1>=num3):
        C=num1
    elif(num2>=num1) and (num2>=num3):
        C=num2
    else :
        C=num3
        return C
C=float(maximum(num1,num2,num3))
# need to find the maximum number and label it is c to use in the pythagorean theorem

def min (num1,num2,num3):
    if (num1<=num2) and (num1<=num3):
        a=num1
    elif(num2<=num1) and (num2<=num3):
        a=num2
    else: a=num3
    return a
#need to find the minimum number so that we can use it in the theorem
A=float(min(num1,num2,num3))

def rem (A,B,C):
    if (num1==C) and (num2==A):
        B=num3
    elif(num3==C) and (num1==A):
        B=num2
    else: B=num1
    return B
B=float(rem(num1,num2,num3))
#need to define what number is left and then assign it as B to use in our triangle ineqaulity theorem
#tested section with print statements to make sure that program returns A as min, C as max, and B as the number that is not yet assigned a var
#set A,B,C as floats so they can be used to determine if they are mathematically triangles or not
if A+B<=C:
    print('You didnt make a triangle :(')
    exit()
#by the triangle inequality theorem if the sums of the small and medium side arent larger then the biggest side it is not a triangle
if A**2+B**2==C**2:
    print('You made a right triangle\n')
    
    print('0\n00\n000')
#A right triangle is when A squared + B squared = C squared
if C**2<A**2+B**2:
    print('You made an acute Triangle\n')
    
    print('   0\n  000\n 00000\n0000000')
#Triangle inequality therom makes this statement true
if C**2>A**2+B**2:
    print('You made an obtuse triangle\n')
    
    print('    0\n   000\n 0000000')
#Triangle inequality therom makes this statement true







    
        

