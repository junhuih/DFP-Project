import helpers as h

def collegeHelper():
    print('Welcome to college helper!')
    print('Please select the following prompt:')
    print('1. See recommended college based on my preferences')
    print('2. View colleges through filters')
    print('3. Search colleges')
    print('4. Help')
    print('5. Exit')

    x = h.getInput(4)
            
    if (x == 1):
        getRecommendation()
    elif (x == 2):
        viewThroughFilter()
    elif (x == 3):
        h.demoFunction()
    elif (x == 4):
        helpMessage()
    else:
        h.exitMessage(x)


    
def getRecommendation():
    print("Recommendation!")
    print("Not implemented yet, return to menu!")
    print('==========================')
    collegeHelper()
    
def getPreferences():
    x = []
    x.append(h.getInput(4))
    x.append(h.getInput(4))
    x.append(h.getInput(4))
    x.append(h.getInput(4))
    
    file1 = open("preferences.txt","w")
    stringS = ""
    for content in x:
        stringS = stringS + str(content) + " "
    

    file1.write(stringS)
    print("New preference entered: " + stringS)
    getRecommendation()
    
def viewThroughFilter():
    print('==========================')
    print('Viewing college by filters:')
    print('1. View colleges with best rankings')
    print('2. View colleges by location')
    print('3. View colleges by tuition')
    print('4. View colleges by returns')
    print('5. View colleges by test scores')
    print('6. Go back to menu')
    
    x = h.getInput(6)
            
    if (x == 1):
        h.demoFunction()
    elif (x == 2):
        h.demoFunction()
    elif (x == 3):
        h.demoFunction()
    elif (x == 4):
        h.demoFunction()
    elif (x == 5):
        h.demoFunction()
    else:
        collegeHelper()
        

def helpMessage():
    print('==========================')
    print("College helper is good to help you find colleges!")
    print('==========================')
    collegeHelper()

collegeHelper()