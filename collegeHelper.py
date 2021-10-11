def collegeHelper():
    print('Welcome to college helper!')
    print('Please select the following prompt:')
    print('1. See recommended college based on my preferences')
    print('2. View colleges through filters')
    print('3. Help')
    print('4. Exit')

    x = getInput(4)
            
    if (x == 1):
        getRecommendation()
    elif (x == 2):
        viewThroughFilter()
    elif (x == 3):
        helpMessage()
    else:
        exitMessage(x)

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
    
    
def getRecommendation():
    print("Recommendation!")
    collegeHelper()
    
def viewThroughFilter():
    print('==========================')
    print('Viewing college by filters:')
    print('1. View colleges with best rankings')
    print('2. View colleges by location')
    print('3. View colleges by tuition')
    print('4. View colleges by returns')
    print('5. View colleges by test scores')
    print('6. Go back to menu')
    
    x = getInput(6)
            
    if (x == 1):
        demoFunction()
    elif (x == 2):
        demoFunction()
    elif (x == 3):
        demoFunction()
    elif (x == 4):
        demoFunction()
    elif (x == 5):
        demoFunction()
    else:
        collegeHelper()

def helpMessage():
    print('==========================')
    print("College helper is good to help you find colleges!")
    print('==========================')
    collegeHelper()
    
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

collegeHelper()