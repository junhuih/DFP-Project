# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""

# import os
import time
import random
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from pandas.core.frame import DataFrame
from user_agent import DESKTOP_USER_AGENTS
from selenium.common.exceptions import NoSuchElementException
import csv


edge_driver_path = (
    "path/to/webdriver"
)


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
        bsyc = BeautifulSoup(html.read(), "html.parser")
        fout = open("payscale_temp.txt", "wt", encoding="utf-8")
        fout.write(str(bsyc))
        fout.close()
        # get lists
        tc_table = list(bsyc.body.div.div)
        table = list(tc_table[1].children)
        body = table[4].tbody
        for i in body.children:
            li = list(
                i.find_all("span", {"class": "roi-grid__schoolname--text"})
            )
            for j in li:
                school_name.append(str(j).split(">")[2][:-3])
        for i in body.children:
            li = list(i.find_all("span", {"class": "roi-grid__rank--text"}))
            for j in li:
                rank.append(str(j).split(">")[1][:-6])
        datas = []
        for i in body.children:
            li = list(i.find_all("span", {"class": "data-table__value"}))
            for j in li:
                datas.append(str(j).split(">")[1][:-6])
        for i in range(len(datas)):
            if i % 7 == 2:
                twenty_year_roi.append(datas[i])
            if i % 7 == 3:
                total_4_year_cost.append(datas[i])
            if i % 7 == 4:
                graduation_rate.append(datas[i])
            if i % 7 == 5:
                typical_years_to_graduate.append(datas[i])
            if i % 7 == 6:
                average_loan_amount.append(datas[i])
    # convert to dictionary
    dataf = {
        "Rank": rank,
        "School Name": school_name,
        "20 Year Net ROI": twenty_year_roi,
        "Total 4 Year Cost": total_4_year_cost,
        "Graduation Rate": graduation_rate,
        "Typical Years to Graduate": typical_years_to_graduate,
        "Average Loan Amount": average_loan_amount,
    }
    # Convert to dataFrame and output as Excel
    dataframe = DataFrame(dataf, index=rank)
    dataframe.to_excel("output.xlsx")


# read ROI data
# since the time to crawl is long, I stored them in an excel, and now I will read from the excel
def clean_roi():
    roi = pd.read_excel("output.xlsx")
    roi = roi.drop_duplicates(
        subset=[
            "School Name",
            "20 Year Net ROI",
            "Total 4 Year Cost",
            "Graduation Rate",
            "Typical Years to Graduate",
        ]
    )
    roi["Rank"] = range(len(roi))
    roi["School Name"] = [
        (s.split("-")[0] + " - " + s.split("-")[1]).strip()
        if s.find("-") != -1
        else s
        for s in roi["School Name"]
    ]
<<<<<<< Updated upstream
    #os.remove("output.xlsx")
=======
>>>>>>> Stashed changes
    return roi


#######################NICHE DATA#######################
# Crawl the NICHE SAT data with beautifulsoup
# Time Warning: about 10 minutes
def send_request(link):
    time.sleep(random.choice(range(2, 10)))
    headers = {"user-agent": random.choice(DESKTOP_USER_AGENTS)}
    res = requests.get(link, headers=headers)
    if res == None:
        print("res is empty")
        return res
    return res

def get_niche():
    # create a list with the url of all 82 pages of the ranking
    allurl = ["https://www.niche.com/colleges/search/best-value-colleges/",]
    nexturl = "https://www.niche.com/colleges/search/best-value-colleges/?page="
    for i in range(2,82):
        myurl = nexturl+str(i)
        allurl.append(myurl)
    
    school_name = []
    fact = []
    location = []
    # iterate and scrape through each link 
    for url in allurl:
        #define the link to be scrape and sent request
        res =send_request(url)
        #parse data from each page 
        newsoup = BeautifulSoup(res.text,'html.parser')
        #find the info on each school
        #for each school, create a new dict that contain its name and fact 
        for div in newsoup.find_all("div", class_="card"):
            # remove the sponsered colleges
            if len(div.find_all("div", class_="search-result__sponsered-bar"))==0:
                school_name.append(div.find("h2", class_="search-result__title"))
                fact.append(div.find_all("span", class_= "search-result-fact__value"))
                if len(div.find_all("li", class_= "search-result-tagline__item"))!=0:
                    location.append(div.find_all("li", class_= "search-result-tagline__item")[1])
                else:
                    location.append('null')
                    
    cleaned_school_name = []
    for i in school_name:
        new = str(i).split('>')
        if (len(new)<2):
            cleaned_school_name.append("null")
        else: 
            cleaned_school_name.append(new[1].split('<')[0])

    cleaned_fact = []
    for list in fact:
        temp = []
        for i in list:
            new = str(i).split('>')
            if (len(new)<2):
                temp.append("null")
            else: 
                temp.append(new[1].split('<')[0])
        cleaned_fact.append(temp)

    cleaned_location = []
    for i in location:
        new = str(i).split('>')
        if (len(new)<2):
            cleaned_location.append("null")
        else: 
            cleaned_location.append(new[1].split('<')[0])
    
    city = []
    state = []
    for i in cleaned_location:
        new = i.split(', ')
        if (len(new)<2):
            city.append("null")
            state.append("null")
        else: 
            city.append(new[0])
            state.append(new[1])
    
    Acceptance_Rate = []
    Net_Price = []
    SAT_Range = []
    
    for eachfact in cleaned_fact:
        if len(eachfact)>0:
            Acceptance_Rate.append(eachfact[0]), Net_Price.append(eachfact[1])
            if len(eachfact)==3:
                if len(eachfact[2])>1:
                    SAT_Range.append(eachfact[2])
                else:
                    SAT_Range.append("null")
            else:
                SAT_Range.append("null")
        else: 
            Acceptance_Rate.append("null"), Net_Price.append("null"), SAT_Range.append("null")
    
    file = open("cleaned_niche.csv", "w", newline = "")
    writer = csv.writer(file)
    # field names 
    fields = ['School Name', 'City', 'State', 'Acceptance Rate', 'Net Price', 'SAT Range'] 
    writer.writerow(fields)
    for i in range(len(cleaned_school_name)):
        if cleaned_school_name[i] != "null":
            writer.writerow([cleaned_school_name[i], city[i], state[i], Acceptance_Rate[i], Net_Price[i], SAT_Range[i]])    
    file.close()
    

#######################Merge the data#######################
def add_calculation_columns(merged_data):
    def convert_currency_to_int(currency):
        try:
            return int(currency.replace(",", "").replace("$", ""))
        except:
            return np.NaN

    def get_sat_range_min(sat_range):
        if type(sat_range) is float and np.isnan(sat_range):
            return np.nan
        else:
            return int(sat_range.split("-")[0])

    def get_sat_range_max(sat_range):
        if type(sat_range) is float and np.isnan(sat_range):
            return np.nan
        else:
            return int(sat_range.split("-")[1])

    merged_data["SAT Min"] = merged_data["SAT Range"].map(
        lambda cell: get_sat_range_min(cell)
    )
    merged_data["SAT Max"] = merged_data["SAT Range"].map(
        lambda cell: get_sat_range_max(cell)
    )
    merged_data["Total 4 Year Cost (Integer)"] = merged_data[
        "Total 4 Year Cost"
    ].map(lambda x: convert_currency_to_int(x))


def merge_data():
    roi = clean_roi()
    roi["Rank"] = roi["Rank"] + 1
    niche = pd.read_csv("cleaned_niche.csv", encoding='ISO-8859-1')
    niche = niche.drop_duplicates()
    merged_data = pd.merge(roi, niche, how="left", on="School Name")
    merged_data = merged_data.drop(labels="Unnamed: 0", axis=1)
    add_calculation_columns(merged_data)
    merged_data.to_excel("merged_data.xlsx")


##################### Combining Fetch ###############
def refresh_all_data():
    get_roi()
    get_niche()
    merge_data()
    # get_careers_data() - uncomment if you have webdriver path set
    print("Success! All data is refreshed.")


#################### Best Colleges Data ####################
# this portion of the script is to scrape bestcollege.com
# for information on career data


def get_careers_data():
    # Call your browser
    driver = webdriver.Edge(executable_path=edge_driver_path)

    # Get all career links
    driver.get("https://www.bestcolleges.com/careers/")
    career_anchors = driver.find_elements_by_css_selector(
        "div.swiper-slide a[data-wpel-link='internal']"
    )
    career_links = [career.get_attribute("href") for career in career_anchors]

    career_data_list = []

    # Loop through urls collected and collect data
    for career in career_links:
        driver.get(career)
        career_name = driver.find_element_by_css_selector(
            "section.hero h1"
        ).text
        career_info = driver.find_element_by_css_selector(
            "section.container.content>p:first-child"
        ).text

        try:
            why_career = driver.find_element_by_css_selector(
                'a[id^="why-pursue"]+h2+p'
            ).text
            why_career += (
                " "
                + driver.find_element_by_css_selector(
                    'a[id^="why-pursue"]+h2+p+div+p'
                ).text
            )
        except NoSuchElementException:
            why_career = ""

        try:
            how_to_start = driver.find_element_by_css_selector(
                "a#advancing-your-career+h2+p"
            ).text
            how_to_start += driver.find_element_by_css_selector(
                "a#advancing-your-career+h2+p+div+p"
            ).text
        except NoSuchElementException:
            how_to_start = ""

        career_data_list.append(
            {
                "career_name": career_name,
                "career_info": career_info,
                "why_career": why_career,
                "how_to_start": how_to_start,
            }
        )

    # Create a data frame of the data collected
    career_data = pd.DataFrame(
        career_data_list,
        columns=["career_name", "career_info", "why_career", "how_to_start"],
    )

    # Save the data frame created for future use.
    career_data.to_csv(
        "bestcolleges_careers.csv", index=False, encoding="utf-8"
    )

    driver.close()
    
merge_data()