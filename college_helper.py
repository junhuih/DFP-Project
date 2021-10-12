import helpers as h
import bestcolleges_helper as bs_helper
import recommender_helper as r_helper

def collegeHelper():
    print("Welcome to college helper!")
    print("Please select the following prompt:")
    print("1. See recommended college based on my preferences")
    print("2. View colleges through filters")
    print("3. Browse careers")
    print("4. Search colleges")
    print("5. Help")
    print("6. Exit")

    x = h.getInput(4)

    if x == 1:
        getRecommendation()
    elif x == 2:
        viewThroughFilter()
    elif x == 3:
        browse_careers()
    elif x == 4:
        h.demoFunction()
    elif x == 5:
        helpMessage()
    else:
        h.exitMessage(x)


def getRecommendation():
    print("Please input your preferences:")

    print("What state would you prefer to study in: (ex. LA, PA) ")
    preferred_state = input()

    print("Your SAT Score:")
    sat_score = int(input())

    print("How much are you ready to pay for college: (in numbers)")
    total_4_year_cost = input()

    r_helper.view_recommendations(
        preferred_state, sat_score, total_4_year_cost
    )

    print("==========================")
    collegeHelper()


def getPreferences():
    x = []
    x.append(h.getInput(4))
    x.append(h.getInput(4))
    x.append(h.getInput(4))
    x.append(h.getInput(4))

    file1 = open("preferences.txt", "w")
    stringS = ""
    for content in x:
        stringS = stringS + str(content) + " "

    file1.write(stringS)
    print("New preference entered: " + stringS)
    getRecommendation()


def viewThroughFilter():
    print("==========================")
    print("Viewing college by filters:")
    print("1. View colleges with best rankings")
    print("2. View colleges by location")
    print("3. View colleges by tuition")
    print("4. View colleges by returns")
    print("5. View colleges by test scores")
    print("6. Go back to menu")

    x = h.getInput(6)

    if x == 1:
        h.demoFunction()
    elif x == 2:
        h.demoFunction()
    elif x == 3:
        h.demoFunction()
    elif x == 4:
        h.demoFunction()
    elif x == 5:
        h.demoFunction()
    else:
        collegeHelper()


def browse_careers():
    print(
        """How do you want to browse careers? (choose option)
1. Show all careers:
2. View career information by name:"""
    )
    user_input = input()
    if user_input == "1":
        bs_helper.view_all_careers()
    elif user_input == "2":
        print("Career Name:")
        user_input = input()
        bs_helper.view_career_info_by_name(user_input)


def helpMessage():
    print("==========================")
    print("College helper is good to help you find colleges!")
    print("==========================")
    collegeHelper()


collegeHelper()
