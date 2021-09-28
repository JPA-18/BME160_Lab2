#!/usr/bin/env python3
# Name: Jonathan Postel (jpostel)
# Group Members: None

'''
This program takes a user input and looks to see if the user input is equal to a key in one of the four constructed dictionaries.
If the user input is in one of the dictionaries the program will print the value matched to the key.
If the user input is not in one of the dictionaires the program will print "Unknown" without the quotes.

Input: A DNA or RNA codon, a one letter amino acid code or a three letter amino acid code
Output: The matching value of the input


'''
short_AA = {
            'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
            'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
            'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
            'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
            }

long_AA = {value:key for key,value in short_AA.items()}

RNA_codon_table = {
# Second Base
# U             C             A             G
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}

DNA_codon_table = {key.replace('U','T'):value for key, value in RNA_codon_table.items()}

def main():
    '''
	This function asks for the userInput and checks to see if the userInput is equal to any of the keys in the four dictionaries. If true the method will return the value that matches the key which is the userInput
    '''
    firstInput = input("Enter a codon, a amino acid three letter code or a one letter code: ") #asks for userinput
    userInput = firstInput.upper() #makes the input all upercase
    if userInput in short_AA: #sees if the userInput is a key in the short_AA dictionary and if true prints out the value of the userInput
        print(userInput, "=", short_AA.get(userInput))
    elif userInput in long_AA: #sees if the userInput is a key in the long_AA dictionary and if true prints out the value of the userInput
        print(userInput,"=", long_AA.get(userInput))
    elif userInput in RNA_codon_table: #sees if the userInput is a key in the RNA_codon_table dictionary and if true prints out the value of the userInput
        print(userInput, "=", RNA_codon_table.get(userInput))
    elif userInput in DNA_codon_table: #sees if the userInput is a key in the DNA_codon_table dictionary and if true prints out the value of the userInput
        print(userInput, "=", DNA_codon_table.get(userInput))
    else:
        print("Unknown") #if all the previous statements are false, the main function prints out "Unknown"

main()
