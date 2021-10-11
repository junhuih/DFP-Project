# This is a sample Python script.
import openpyxl as openpyxl
from urllib.request import urlopen  # b_soup_1.py

import pandas as pd
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from urllib.request import urlopen
import json
import re
import matplotlib.pyplot as plt
import time
import requests
import random
# import user_agents
# from user_agents import DESKTOP_USER_AGENTS
import csv

import numpy as np
#######################ROI DATA#######################
# Crawl the ROI data with beautifulsoup
# Time Warning: about 10 minutes
def get_roi():
    school_name = []
    rank = []
    twenty_year_roi = []
    total_4_year_cost = []
    graduation_rate = []
    typical_years_to_graduate = []
    average_loan_amount = []
    for page in range(1, 199, 1):
        html = "https://www.payscale.com/college-roi/page/" + str(page)
        # get HTML
        html = urlopen(html)
        bsyc = BeautifulSoup(html.read(), "html")
        fout = open('payscale_temp.txt', 'wt', encoding='utf-8')
        fout.write(str(bsyc))
        fout.close()
        # get lists
        tc_table = list(bsyc.body.div.div)
        table = list(tc_table[1].children)
        body = table[4].tbody
        for i in body.children:
            li = list(i.find_all("span", {"class": "roi-grid__schoolname--text"}))
            for j in li:
                school_name.append(str(j).split('>')[2][:-3])
        for i in body.children:
            li = list(i.find_all("span", {"class": "roi-grid__rank--text"}))
            for j in li:
                rank.append(str(j).split('>')[1][:-6])
        datas = []
        for i in body.children:
            li = list(i.find_all("span", {"class": "data-table__value"}))
            for j in li:
                datas.append(str(j).split('>')[1][:-6])
        for i in range(len(datas)):
            if i % 7 == 2: twenty_year_roi.append(datas[i])
            if i % 7 == 3: total_4_year_cost.append(datas[i])
            if i % 7 == 4: graduation_rate.append(datas[i])
            if i % 7 == 5: typical_years_to_graduate.append(datas[i])
            if i % 7 == 6: average_loan_amount.append(datas[i])
    # convert to dictionary
    dataf = {"Rank": rank, "School Name": school_name, "20 Year Net ROI": twenty_year_roi,
             "Total 4 Year Cost": total_4_year_cost, "Graduation Rate": graduation_rate,
             "Typical Years to Graduate": typical_years_to_graduate, "Average Loan Amount": average_loan_amount}
    # Convert to dataFrame and output as Excel
    dataframe = DataFrame(dataf, index=rank)
    dataframe.to_excel('output.xlsx')

# read ROI data
# since the time to crawl is long, I stored them in an excel, and now I will read from the excel
def clean_roi():
    roi = pd.read_excel("output.xlsx")
    roi = roi.drop_duplicates(
            subset=['School Name', '20 Year Net ROI', 'Total 4 Year Cost', 'Graduation Rate', 'Typical Years to Graduate'])
    roi["Rank"] = range(len(roi))
    roi["School Name"] = [(s.split("-")[0]+" - "+s.split("-")[1]).strip() if s.find("-")!=-1 else s for s in roi["School Name"]]
    # for i in roi["School Name"]:
    #     if i.find("-") == -1:
    #         i = i
    #     else: i = str(i).split('-')[0]+" - "+ str(i).split('-')[1]
    return roi


#######################NICHE DATA#######################
# Crawl the NICHE SAT data with beautifulsoup
# Time Warning: about 10 minutes
def send_request(link):
    time.sleep(random.choice(range(2,10)))
    headers = {'user-agent':random.choice(DESKTOP_USER_AGENTS)}
    res = requests.get(link, headers=headers)
    if res == None:
        print('res is empty')
        return res
    return res

def get_niche():
    # create a list with the url of all 82 pages of the ranking
    allurl = ["https://www.niche.com/colleges/search/best-value-colleges/", ]
    nexturl = "https://www.niche.com/colleges/search/best-value-colleges/?page="
    for i in range(2, 82):
        myurl = nexturl + str(i)
        allurl.append(myurl)

    school_name = []
    fact = []
    location = []
    # iterate and scrape through each link
    for url in allurl:
        # define the link to be scrape and sent request
        res = send_request(url)
        # parse data from each page
        newsoup = BeautifulSoup(res.text, 'html.parser')
        # find the info on each school
        # for each school, create a new dict that contain its name and fact
        for div in newsoup.find_all("div", class_="card"):
            # remove the sponsered colleges
            if len(div.find_all("div", class_="search-result__sponsered-bar")) == 0:
                school_name.append(div.find("h2", class_="search-result__title"))
                fact.append(div.find_all("span", class_="search-result-fact__value"))
                if len(div.find_all("li", class_="search-result-tagline__item")) != 0:
                    location.append(div.find_all("li", class_="search-result-tagline__item")[1])
                else:
                    location.append('null')

    cleaned_school_name = []
    for i in school_name:
        new = str(i).split('>')
        if (len(new) < 2):
            cleaned_school_name.append("null")
        else:
            cleaned_school_name.append(new[1].split('<')[0])

    cleaned_fact = []
    for list in fact:
        temp = []
        for i in list:
            new = str(i).split('>')
            if (len(new) < 2):
                temp.append("null")
            else:
                temp.append(new[1].split('<')[0])
        cleaned_fact.append(temp)

    cleaned_location = []
    for i in location:
        new = str(i).split('>')
        if (len(new) < 2):
            cleaned_location.append("null")
        else:
            cleaned_location.append(new[1].split('<')[0])
    city = []
    state = []
    for i in cleaned_location:
        new = i.split(', ')
        if (len(new) < 2):
            city.append("null")
            state.append("null")
        else:
            city.append(new[0])
            state.append(new[1])

#######################CRIME DATA#######################
# FBI DATA api key
API_KEY = "YsQEzTwMdMPRymtS4Fp7XYFBQmT5A6kSe62h5laI"

# assult category
all_categories_string = "aggravated-assault,all-other-larceny,all-other-offenses,animal-cruelty,arson,assisting-or-promoting-prostitution,bad-checks,betting,bribery,burglary-breaking-and-entering,counterfeiting-forgery,credit-card-automated-teller-machine-fraud,destruction-damage-vandalism-of-property,driving-under-the-influence,drug-equipment-violations,drug-violations,drunkenness,embezzlement,extortion-blackmail,false-pretenses-swindle-confidence-game,fondling,gambling-equipment-violation,hacking-computer-invasion,human-trafficking-commerical-sex-acts,human-trafficking-commerical-involuntary-servitude,identity-theft,impersonation,incest,intimidation,justifiable-homicide,kidnapping-abduction,motor-vehicle-theft,murder-and-nonnegligent-manslaughter,negligent-manslaughter,operating-promoting-assiting-gambling,curfew-loitering-vagrancy-violations,peeping-tom,pocket-picking,pornography-obscence-material,prostitution,purchasing-prostitution,purse-snatching,rape,robbery,sexual-assult-with-an-object,sex-offenses-non-forcible,shoplifting,simple-assault,sodomy,sports-tampering,statutory-rape,stolen-property-offenses,theft-from-building,theft-from-coin-operated-machine-or-device,theft-from-motor-vehicle,theft-of-motor-vehicle-parts-or-accessories,theft-from-motor-vehicle,weapon-law-violation,welfare-fraud,wire-fraud,not-specified,liquor-law-violations,crime-against-person,crime-against-property,crime-against-society,assault-offenses,homicide-offenses,human-trafficking-offenses,sex-offenses,sex-offenses-non-forcible, fraud-offenses,larceny-theft-offenses, drugs-narcotic-offenses,gambling-offenses,prostitution-offenses,all-offenses"
all_categories = [s.strip() for s in all_categories_string.split(",")]
selected_categories = all_categories[0:15]


# all states
all_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
              'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
              'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


# def getCrimeData(assult_category, state):
#     state_data_link = "https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/" + all_categories[
#         assult_category] + "/victim/states/" + all_states[state] + "/count?API_KEY=" + API_KEY
#     response = urlopen(state_data_link)
#     if response is None:
#         return pd.DataFrame(columns=['count', 'data_year'])
#     else:
#         data_json = json.loads(response.read())
#         crimedf = pd.DataFrame(data_json["results"])
#         return crimedf
categories_of_interest = ['murder-and-nonnegligent-manslaughter', 'rape', 'robbery', 'drug-violations']
def getCrimeDataOfInterest(assult_category, state):
    state_data_link = "https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/" + categories_of_interest[
        assult_category] + "/victim/states/" + all_states[state] + "/count?API_KEY=" + API_KEY
    response = urlopen(state_data_link)
    if response is None:
        return pd.DataFrame(columns=['count', 'data_year'])
    else:
        data_json = json.loads(response.read())
        crimedf = pd.DataFrame(data_json["results"])
        return crimedf

#######################TWITTER#######################
# credential
bearer_token = "AAAAAAAAAAAAAAAAAAAAALw%2FTwEAAAAA5mGzkkQRzM5lUExaBkZDfYbS3Y0%3DwqRFpCaqzANZn3kiEwO85WoxjE5PAsQ54tSokCZFvPZy0zI2JT"


def getTwitterComments(school_name):
    url = "https://api.twitter.com/2/tweets/search/recent?query="
    url = url + school_name + '&tweet.fields=created_at'

    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    if response is None:
        print("No tweets for "+school_name)
    else:
        try:
            res_json = response.json()
            print(res_json['data'][0]['text'])
        except:
            print("No tweets for "+school_name)

#######################Merge the data#######################
def merge_data():
    roi = clean_roi()
    roi["Rank"] = roi["Rank"]+1
    niche = pd.read_csv("cleaned_niche.csv").drop_duplicates()
    merged_data = pd.merge(roi, niche, how='left', on="School Name")
    merged_data = merged_data.drop(labels='Unnamed: 0',axis=1)
    merged_data.to_excel("Merged_data.xlsx")


#######################Display the data#######################
def search_colleges(college, dataframe):
    college_name = dataframe["School Name"]
    dataset = pd.read_excel("Merged_data.xlsx")
    dataset = dataset.fillna('missing')
    # if college.title() not in college_name.values:
    #     print("We can not find the "+college+". Please check your input. ")
    # else:
    for i in college_name:
        if i.upper().find(college.upper()) != -1:
            print("******************" + i + "******************")
            print('%-30s' % "State: " + dataset.loc[dataset["School Name"] == i, ["State"]].values[0][0])
            print('%-30s' % "City: " + dataset.loc[dataset["School Name"] == i, ["City"]].values[0][0])
            print('%-30s' % "20 Year Net ROI: " +
                  dataframe.loc[dataframe["School Name"] == i, ["20 Year Net ROI"]].values[0][0])
            print('%-30s' % "Total 4 Year Cost: " +
                  dataframe.loc[dataframe["School Name"] == i, ["Total 4 Year Cost"]].values[0][0])
            print('%-30s' % "Typical Years to Graduate: " + (
            dataframe.loc[dataframe["School Name"] == i, ["Typical Years to Graduate"]].values[0][0]))
            print('%-30s' % "Average Loan Amount: " + str(
                dataframe.loc[dataframe["School Name"] == i, ["Average Loan Amount"]].values[0][0]))
            print('%-30s' % "Acceptance Rate: " + dataset.loc[dataset["School Name"] == i, ["Acceptance Rate"]].values[0][0])
            print('%-30s' % "SAT Range: " + dataset.loc[dataset["School Name"] == i, ["SAT Range"]].values[0][0])
            print("The most recent Twitter Comments: ")
            plt.style.use('seaborn-white')
            getTwitterComments(i)
            plt.style.use('seaborn-white')

            fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
            for x in range(2):
                for y in range(2):
                    df = getCrimeDataOfInterest(x * 2 + y, all_states.index(dataset.loc[dataset["School Name"] == i, ["State"]].values[0][0]))
                    df = df.fillna(0)
                    if df.empty:
                        axes[x, y].plot()
                        axes[x, y].set_title("There's not enough data to plot")
                    else:
                        df = df[df['data_year'] > 2009]
                        axes[x, y].plot(df.iloc[:, 1], df.iloc[:, 0])
                        axes[x, y].set_title(categories_of_interest[x * 2 + y].replace("-", " ").title())
                        fig.tight_layout()
                        # axes[x, y].xticks(df['data_year'])
                        # axes[x, y].xticks(df['count'])
            plt.show()
        else:
            if i == college_name[len(college_name)-1]:
                print("We can not find the " + college + ". Please check your input. ")
            else: continue

if __name__ == '__main__':
    # merge_data()
    search_colleges("United States Merchant Marine Academy", clean_roi())