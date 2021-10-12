
# This is a sample Python script.
import openpyxl as openpyxl
from urllib.request import urlopen  # b_soup_1.py

import pandas as pd
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from urllib.request import urlopen
import json
import re
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


#######################Merge the data#######################
def merge_data():
    roi = clean_roi()
    roi["Rank"] = roi["Rank"]+1
    niche = pd.read_csv("cleaned_niche.csv").drop_duplicates()
    merged_data = pd.merge(roi, niche, how='left', on="School Name")
    merged_data = merged_data.drop(labels='Unnamed: 0',axis=1)
    merged_data.to_excel("Merged_data.xlsx")

