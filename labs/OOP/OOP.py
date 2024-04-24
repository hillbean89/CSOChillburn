"""
Lab - Object Oriented Programming (OOP)
By: Colin Hillburn  

CSCI 110
Date: FIXME0

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self,r=0):
        return math.pi*2*self.radius

    def __str__(self):
         # Fixed: Modify the statement to return circumference as well (20 pts)
        return "Circle - radius: {:.2f} and area: {:.2f} and circumferance {:.2f}".format(self.radius, self.area,self.circumference)


def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)
    # FIXME3: (20 pts)
    # Instantiate another circle with radius 5
    bCir=Circle(5)
    # Print the circle
    print(bCir)

    # FIMXE4: (20 pts)
    # prompt user to enter radius and store into a variable
    radius=float(input('enter a number: '))

    # FIXME5: (20 pts)
    # create a circle with the user provided radius
    UserCir=Circle(radius)
    # print the circle
    print(UserCir)


if __name__ == "__main__":
    main()