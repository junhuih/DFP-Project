# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""

import twitter_comment as tc
import fbi_crime_data as fbi
import pandas as pd
import matplotlib.pyplot as plt
import helpers as h


#######################Display the data#######################
def search_colleges(college, dataframe):
    college_name = dataframe["School Name"]
    dataset = pd.read_excel("merged_data.xlsx")
    dataset = dataset.fillna("missing")
    for i in college_name:
        if i.upper().find(college.upper()) != -1:
            print("******************" + i + "******************")
            print(
                "%-30s" % "State: "
                + dataset.loc[dataset["School Name"] == i, ["State"]].values[
                    0
                ][0]
            )
            print(
                "%-30s" % "City: "
                + dataset.loc[dataset["School Name"] == i, ["City"]].values[0][
                    0
                ]
            )
            print(
                "%-30s" % "20 Year Net ROI: "
                + dataframe.loc[
                    dataframe["School Name"] == i, ["20 Year Net ROI"]
                ].values[0][0]
            )
            print(
                "%-30s" % "Total 4 Year Cost: "
                + dataframe.loc[
                    dataframe["School Name"] == i, ["Total 4 Year Cost"]
                ].values[0][0]
            )
            print(
                "%-30s" % "Typical Years to Graduate: "
                + (
                    dataframe.loc[
                        dataframe["School Name"] == i,
                        ["Typical Years to Graduate"],
                    ].values[0][0]
                )
            )
            print(
                "%-30s" % "Average Loan Amount: "
                + str(
                    dataframe.loc[
                        dataframe["School Name"] == i, ["Average Loan Amount"]
                    ].values[0][0]
                )
            )
            print(
                "%-30s" % "Acceptance Rate: "
                + dataset.loc[
                    dataset["School Name"] == i, ["Acceptance Rate"]
                ].values[0][0]
            )
            print(
                "%-30s" % "SAT Range: "
                + dataset.loc[
                    dataset["School Name"] == i, ["SAT Range"]
                ].values[0][0]
            )
            print()
            print("The most recent Twitter Comments: ")
            plt.style.use("seaborn-white")
            tc.get_twitter_comments(i)
            if (
                dataset.loc[dataset["School Name"] == i, ["State"]].values[0][
                    0
                ]
                == "missing"
            ):
                break
            else:
                plt.style.use("seaborn-white")
                fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
                for x in range(2):
                    for y in range(2):
                        df = fbi.get_crime_data_of_interest(
                            x * 2 + y,
                            fbi.all_states.index(
                                dataset.loc[
                                    dataset["School Name"] == i, ["State"]
                                ].values[0][0]
                            ),
                        )
                        df = df.fillna(0)
                        if df.empty:
                            axes[x, y].plot()
                            axes[x, y].set_title(
                                "There's not enough data to plot"
                            )
                        else:
                            df = df[df["data_year"] > 2009]
                            axes[x, y].plot(df.iloc[:, 1], df.iloc[:, 0])
                            axes[x, y].set_title(
                                fbi.categories_of_interest[x * 2 + y]
                                .replace("-", " ")
                                .title()
                            )
                            fig.tight_layout()
                            # axes[x, y].xticks(df['data_year'])
                            # axes[x, y].xticks(df['count'])
                plt.show()
                break
            print("Crime data displayed by plot.")
        else:
            if i == college_name[len(college_name) - 1]:
                print(
                    "We can not find the "
                    + college
                    + ". Please check your input. "
                )


def search_colleges_wrapper():
    college = input("Please enter the college name you want to search: ")
    search_colleges(college, h.read_final_data())


if __name__ == "__main__":
    college = input("Please enter the college name you want to search: ")
    search_colleges(college, h.read_final_data())
