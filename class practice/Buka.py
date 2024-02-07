'''Date 2/5/202
program: Kattis https://open.kattis.com/problems/buka
Algorithm steps:
input a number: A
input an operator
input second number, b
use eval() to evaluate the expression A operator b (ex:a+b)'''

a = input ()
operand = input()
b= input()


expression=a+operand+b
print(expression)
print(eval(expression))



