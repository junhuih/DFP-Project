# -*- coding: utf-8 -*-
"""
@author: Yifan Cheng, Skylar Du, Yashash Gaurav, Mark He
"""
# this script is to scrape bestcollege.com for information on career data
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# Sanity
driver = webdriver.Edge(
    executable_path="C:\\Users\\Yashash Gaurav\\Downloads\\edgedriver_win64 (2)\\msedgedriver.exe"
)


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
    career_name = driver.find_element_by_css_selector("section.hero h1").text
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
    "data\\bestcolleges_careers.csv", index=False, encoding="utf-8"
)

driver.close()
