# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""
import pandas as pd
import numpy as np

from fuzzywuzzy import fuzz
from fuzzywuzzy import process


bestcolleges_data_path = "data\\bestcolleges_careers.csv"

bestcolleges_data = pd.read_csv(bestcolleges_data_path)


# Print all the careers
def view_all_careers():
    print("We are ready to guide you on the following careers : ")
    for index, careers_name in enumerate(
        bestcolleges_data.career_name.to_list()
    ):
        print(str(index + 1) + ". " + careers_name)

# Search and print all information for the given career
def view_career_info_by_name(searched_career):
    closest_result = process.extractOne(
        searched_career,
        bestcolleges_data.career_name.to_list(),
        scorer=fuzz.partial_ratio,
    )
    if len(closest_result) > 0:
        search_result_row = bestcolleges_data[
            bestcolleges_data.career_name == closest_result[0]
        ]
        print(
            "Here is some guidance on " + search_result_row.career_name.iloc[0]
        )

        if search_result_row.career_info is not np.nan:
            print("----  Info ----")
            print(search_result_row.career_info.iloc[0])

        if search_result_row.why_career is not np.nan:
            print(
                "----  Why " + search_result_row.career_name.iloc[0] + " ----"
            )
            print(search_result_row.why_career.iloc[0])

        if search_result_row.how_to_start.iloc[0] is not np.nan:
            print(
                "----  How to start on "
                + search_result_row.career_name.iloc[0]
                + " ----"
            )
            print(search_result_row.how_to_start.iloc[0])
