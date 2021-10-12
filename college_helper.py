import helpers as h
import bestcolleges_helper as bs_helper
import recommender_helper as r_helper
import search_colleges as sc
import average_stats as avg_stat

def college_helper():
    print("Welcome to college helper!")
    print("Please select the following prompt:")
    print("1. See recommended college based on my preferences")
    print("2. See top level stats about colleges")
    print("3. Browse careers")
    print("4. Search colleges")
    print("5. Help")
    print("6. Exit")

    x = h.get_input(6)

    if x == 1:
        getRecommendation()
    elif x == 2:
        viewGeneralData()
    elif x == 3:
        browse_careers()
    elif x == 4:
        sc.search_colleges_wrapper()
        print("\n==========================")
        college_helper()
    elif x == 5:
        helpMessage()
    else:
        h.exitMessage(x)
        return


def getRecommendation():
    print("Please input your preferences:")

    print("What state would you prefer to study in: (ex. LA, PA) ")
    preferred_state = h.get_states()

    print("Your SAT Score:")
    sat_score = h.get_input(1600)

    print("How much are you ready to pay for college: (in numbers)")
    total_4_year_cost = h.get_input(1000000)

    r_helper.view_recommendations(
        preferred_state, sat_score, total_4_year_cost
    )

    print("\n==========================")
    college_helper()

def viewGeneralData():
    print("==========================")
    print("Viewing college by filters:")
    print("1. View the average stats of all states")
    print("2. View ROI by states")
    print("3. View total 4 year costs by states")
    print("4. View average loan amount by states")
    print("5. Go back to menu")

    x = h.get_input(5)

    if x == 1:
        avg_stat.get_average_stats()
        viewGeneralData()
    elif x == 2:
        avg_stat.compute_roi_and_draw_map()
        viewGeneralData()
    elif x == 3:
        avg_stat.compute_cost_and_draw_map()
        viewGeneralData()
    elif x == 4:
        avg_stat.compute_loan_and_draw_map()
        viewGeneralData()
    else:
        print("\n==========================")
        college_helper()


def browse_careers():
    print(
        """How do you want to browse careers? (choose option)\n1. Show all careers:\n2. View career information by name:"""
    )
    user_input = input()
    if user_input == "1":
        bs_helper.view_all_careers()
    elif user_input == "2":
        print("Career Name:")
        user_input = input()
        bs_helper.view_career_info_by_name(user_input)
        
    print("\n==========================")
    college_helper()


def helpMessage():
    print("==========================")
    print("College helper is good to help you find colleges!")
    print("You can navigate through the menu and browse useful informations! The information would be valuable for you to find the college that matches the best with your preferences!")
    print("==========================")
    college_helper()


if __name__ == '__main__':
    college_helper()
