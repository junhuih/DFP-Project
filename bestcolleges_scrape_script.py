import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# sanity
driver = webdriver.Edge(
    executable_path="C:\\Users\\Yashash Gaurav\\Downloads\\edgedriver_win64 (2)\\msedgedriver.exe"
)


# get all career links
driver.get("https://www.bestcolleges.com/careers/")
career_anchors = driver.find_elements_by_css_selector(
    "div.swiper-slide a[data-wpel-link='internal']"
)
career_links = [career.get_attribute("href") for career in career_anchors]
# loop through urls collected and collect data


career_data_list = []
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

career_data = pd.DataFrame(
    career_data_list,
    columns=["career_name", "career_info", "why_career", "how_to_start"],
)

career_data.to_csv(
    ".output\\bestcolleges_careers.csv", index=False, encoding="utf-8"
)

career_data.head()

driver.close()
