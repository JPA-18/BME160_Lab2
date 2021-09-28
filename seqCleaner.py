#!/usr/bin/env python3 
# Name: Jonathan Postel (jpostel) 
# Group Members: None

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example: 
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring (str):
    
    def uppercase(self):
        return (self.upper())
    
    def countN(self):
        num_N = self.count("N")
        return (num_N)
    
    def findN(self):
        position_N = self.find("N")
        return (position_N)
        
def main():
    ''' Get user DNA data and clean it up.'''
    data = input('DNA data? ')
    thisDNA = DNAstring (data)
    upperDNA = thisDNA.uppercase()
    numOfNs = DNAstring (upperDNA).countN()
    location_N = DNAstring (upperDNA).findN()
    
    dnaPurified = upperDNA[0:location_N] + "{" + str(numOfNs) + "}" + upperDNA[location_N + numOfNs : len(upperDNA)]  
    
    print (dnaPurified)
    
   
    
main()