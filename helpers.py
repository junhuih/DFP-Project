# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""

import pandas as pd

all_states = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]


def get_input(maxInput):
    while True:
        x = input()
        try:
            intX = int(x)
            if 0 < intX and intX <= maxInput:
                return intX
            else:
                errorMessage(x)
        except:
            errorMessage(x)


def get_states():
    while True:
        x = input()
        try:
            if x in all_states:
                return x
            else:
                errorMessage(x)
        except:
            errorMessage(x)


def errorMessage(x):
    print("==========================")
    print("You've entered " + x + ", which is an invalid input.")
    print("Please enter again!")
    return


def exitMessage(x):
    print("==========================")
    print("Thank you for using college helper!")
    return


def demoFunction():
    print("==========================")
    print("fill up demo function, program ends here")
    print("==========================")


def read_final_data():
    d = pd.read_excel("Merged_data.xlsx")
    d = d.drop_duplicates(
        subset=[
            "School Name",
            "20 Year Net ROI",
            "Total 4 Year Cost",
            "Graduation Rate",
            "Typical Years to Graduate",
        ]
    )
    d["Rank"] = range(len(d))
    d["School Name"] = [
        (s.split("-")[0] + " - " + s.split("-")[1]).strip()
        if s.find("-") != -1
        else s
        for s in d["School Name"]
    ]
    return d
