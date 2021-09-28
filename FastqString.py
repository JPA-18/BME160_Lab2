#!/usr/bin/env python3 
# Name: Jonathan Postel (jpostel) 
# Group Members: None

'''
This program takes an input on one line and places a part of the input each onto different lines. The input contains colons and that is how the input is split up.
'''

class FastqString (str):
    ''' This class has one method named parse.'''
    def parse(self):
        ''' Finds the location of a colon in the input string'''
        findColon = self.find(':')
        return findColon
def main():
    ''' Takes a string from the user and makes an object of class FastqString.
    Then makes an object called firstColon where it locates the location of the first colon in the string object of class FastqString.
    Then it makes an object called dataAfterFirstColon of class FastqString that is assigned  with the values in the orginal object of class FastqString but from the location of the firstColon + 1 to the rest of the string.
    This logic continues by looking at the previous object, finding where the colon is, then making a new object by assigning it the value of the next found colon + 1 to the end of the string '''
    data = input("Enter FASTQ seqname line : ")
    fastqData = FastqString (data)
    firstColon = FastqString (fastqData).parse()
    dataAfterFirstColon = fastqData[firstColon + 1:]
    secondColon = FastqString (dataAfterFirstColon).parse() 
    dataAfterSecondColon = dataAfterFirstColon[secondColon + 1:]
    thirdColon = FastqString (dataAfterSecondColon).parse()
    dataAfterThirdColon = dataAfterSecondColon[thirdColon + 1:]
    fourthColon = FastqString (dataAfterThirdColon).parse()
    dataAfterForthColon = dataAfterThirdColon[fourthColon + 1:]
    fifthColon = FastqString (dataAfterForthColon).parse()
    dataAfterFifthColon = dataAfterForthColon[fifthColon + 1:]
    sixthColon = FastqString (dataAfterFifthColon).parse()
    dataAfterSixthColon = dataAfterFifthColon[sixthColon + 1:]
    seventhColon = FastqString (dataAfterSixthColon).parse()

    
    print ('Instrument =', fastqData[1:firstColon])
    print ('Run ID =', dataAfterFirstColon[0:secondColon])
    print ('Flow Cell ID =', dataAfterSecondColon[0:thirdColon])
    print ('Flow Cell Lane =', dataAfterThirdColon[0:fourthColon])
    print ('Tile Number =', dataAfterForthColon[0:fifthColon])
    print ('X-coord =', dataAfterFifthColon[0:sixthColon])
    print ('Y-coord =', dataAfterSixthColon[0:seventhColon])
    
    
    
    

main()