# This is a sample Python script.
import openpyxl as openpyxl
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame

if __name__ == '__main__':
    school_name = []
    rank = []
    twenty_year_roi = []
    total_4_year_cost = []
    graduation_rate = []
    typical_years_to_graduate = []
    average_loan_amount = []


    for page in range(1,199,1):
        html = "https://www.payscale.com/college-roi/page/"+str(page)

        html = urlopen(html)
        bsyc = BeautifulSoup(html.read(), "html")
        fout = open('payscale_temp.txt', 'wt', encoding='utf-8')
        fout.write(str(bsyc))
        fout.close()

        tc_table = list(bsyc.body.div.div)
        table = list(tc_table[1].children)
        body = table[4].tbody
        for i in body.children:
            li = list(i.find_all("span", {"class":"roi-grid__schoolname--text"}))
            for j in li:
                school_name.append(str(j).split('>')[2][:-3])
        for i in body.children:
            li = list(i.find_all("span", {"class":"roi-grid__rank--text"}))
            for j in li:
                rank.append(str(j).split('>')[1][:-6])
        datas = []
        for i in body.children:
            li = list(i.find_all("span", {"class":"data-table__value"}))
            for j in li:
                datas.append(str(j).split('>')[1][:-6])
        for i in range(len(datas)):
            if i%7==2: twenty_year_roi.append(datas[i])
            if i%7==3: total_4_year_cost.append(datas[i])
            if i%7==4: graduation_rate.append(datas[i])
            if i%7==5: typical_years_to_graduate.append(datas[i])
            if i%7==6: average_loan_amount.append(datas[i])
    dataf = {"Rank":rank, "School Name":school_name, "20 Year Net ROI":twenty_year_roi,
             "Total 4 Year Cost":total_4_year_cost, "Graduation Rate":graduation_rate,
             "Typical Years to Graduate":typical_years_to_graduate, "Average Loan Amount":average_loan_amount}
    dataframe = DataFrame(dataf)
    dataframe.to_excel('output.xlsx')