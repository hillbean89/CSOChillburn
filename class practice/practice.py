import math
def main():
        print("hello world")
        A= calc_area (1)
        print(A)
        greet("Corin")
        name= getName()
        greet(name)

def greet(name):
      print(f"hello {name}!")

def calc_area(radius):
    area = math.pi * radius**2
    return area 

def getName():
      name= input("Hi there, enter your full name: ")
      return name
      print(f"Hi {name}, nice meeting you!")
    
        

main()