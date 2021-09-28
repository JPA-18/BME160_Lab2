#!/usr/bin/env python3
# Name: Jonathan Postel (jpostel)
# Group Members: none

'''
Program takes three points in space and calculates the distance between them and the angle between all three points.

Input: C = (any three numbers seperated by commas), N = (any three numbers seperated by commas), Ca = (any three numbers seperated by commas)
Output:
C-N bond length = (calculated value based off input)
N-Ca bond length = (calculated value based off input)
C-N-Na bond angle = (calculated value based off input)
'''

import math
class Triad :
    """
    Calculate angles and distances among a triad of points.

    Author: David Bernick
    Date: March 21, 2013
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()

    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r

    """

    def __init__(self,p,q,r) :
        """ Construct a Triad.

        My consturction
            MyTriad = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ).
        """

        self.p = p
        self.q = q
        self.r = r

# private helper methods
    def d2 (self,a,b) : # calculate squared distance of point a to b
        return float(sum((ia-ib)*(ia-ib)  for  ia,ib in zip (a,b)))

    def dot (self,a,b) : # dotProd of standard vectors a,b
        return float(sum(ia*ib for ia,ib in zip(a,b)))

    def ndot (self,a,b,c) : # dotProd of vec. a,c standardized to b
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))

# calculate lengths(distances) of segments PQ, PR and QR
    def dPQ (self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p,self.q))

    def dPR (self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p,self.r))

    def dQR (self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q,self.r))

    def angleP (self) :
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(self.ndot(self.q,self.p,self.r) /   math.sqrt(self.d2(self.q,self.p)*self.d2(self.r,self.p)))

    def angleQ (self) :
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(self.ndot(self.p,self.q,self.r) /  math.sqrt(self.d2(self.p,self.q)*self.d2(self.r,self.q)))

    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(self.ndot(self.p,self.r,self.q) /  math.sqrt(self.d2(self.p,self.r)*self.d2(self.q,self.r)))

def main():
    ''' This function takes the user input string and replaces all the parenthesis into commas. This way the string can be split into a list by each comma.
    Then by looking at where each coordinate value ended up it assigns those values to an object that corresponds to one of the x, y, or z coordinates of one of the three points.
    Those objects are used to make a tuple for each point in space. Those tuples are assigned to values that are already instantiated in the class Triad.
    Then an object (myTriad) is built of the class Triad.
    The object calls upon methods of the Triad class and prints out the returned values
    '''

    inString = input("Enter Three Points in 3D space: ")
    fixedC = inString.replace("(", ",").replace(")",",") #replaces the parenthesis in the input string into commas
    coordinates = fixedC.split(",") #split the input string by the commas into a list

    xCordOfA = float(coordinates[1]) #after looking at the newly made list turned the appropriate value into a float and assigned it to an object
    yCordOfA = float(coordinates[2]) #^ same as above
    zCordOfA = float(coordinates[3]) # same logic as before
    A = tuple((xCordOfA, yCordOfA, zCordOfA)) #made a tuple contains the values of x,y,z coords for point A

    xCordOfB = float(coordinates[5])
    yCordOfB = float(coordinates[6])
    zCordOfB = float(coordinates[7])
    B = tuple((xCordOfB, yCordOfB, zCordOfB))

    xCordOfC = float(coordinates[9])
    yCordOfC = float(coordinates[10])
    zCordOfC = float(coordinates[11])
    C = tuple((xCordOfC, yCordOfC, zCordOfC))

    p = A #assigning A to p because p was instantiated in the Triad Class
    q = B #the same as above
    r = C #same as above



    myTriad = Triad(p,q,r) #here making an object (myTriad) of the class Triad and giving it the three parameters p,q,r. Allows myTriad to use methods of class Triad
    print ("N-C bond length = {0:0.2f}".format(myTriad.dPQ())) #using method of class Triad to calculate the distance between point A and B
    print("N-Ca bond length = {0:0.2f}".format(myTriad.dQR())) #using method of class Triad to calculate the distance between point B and C
    print("C-N-Ca bond angle = {0:0.2f}".format(myTriad.angleQ() * 57.2958)) #using method of class Triad to calculate the bond angle at point B and converting to degrees


main()
