# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:59:38 2021

@author: Mark He
"""

def getInput(maxInput):
    while (True):
        x = input()
        try:
            intX = int(x)
            if (0 < intX and intX <= maxInput):
                return intX
            else:
                errorMessage(x)
        except:
            errorMessage(x)

    
def errorMessage(x):
    print('==========================')
    print("You've entered " + x + ", which is an invalid input.")
    print("Please enter again!")
    return
    
def exitMessage(x):
    print('==========================')
    print("Thank you for using college helper!")
    return

def demoFunction():
    print('==========================')
    print('fill up demo function, program ends here')
    print('==========================')