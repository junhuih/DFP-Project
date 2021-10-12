# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""

import pandas as pd

merged_data_path = "data\\merged_data.xlsx"

merged_data = pd.read_excel(merged_data_path, index_col=0)


def view_recommendations(preferred_state, sat_score, total_4_year_cost):
    in_range_college = merged_data[
        (merged_data["State"] == preferred_state)
        & (merged_data["SAT Min"] < sat_score)
        # & (merged_data['SAT Max'] > sat_score) - the more the score the better?
        & (
            merged_data["Total 4 Year Cost (Integer)"]
            < (float(total_4_year_cost) * 1.1)
        )
    ]

    if len(in_range_college) > 0:
        print("Here are the schools that we recommend!:")
        for index, college in in_range_college.iterrows():
            print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"20 Year Net ROI:   {str(college[2]):>30}")
            print(f"College Name:      {str(college[1]):>30}")
            print(f"Total 4 Year Cost: {str(college[3]):>30}")
            print(f"Graduation Rate:   {str(college[4]):>30}")
            print(f"City:              {str(college[7]):>30}")
            print(f"State:             {str(college[8]):>30}")
            print(f"Acceptance Rate:   {str(college[9]):>30}")
    else:
        print("\nConsider updating preferences to find better results!")
