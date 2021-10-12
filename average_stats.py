# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:53:39 2021

@author: Mark He
"""
import pandas as pd


us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

# Get the average statistics for a given state
def get_average_stats(dataframe):
    newR = []
    for i, row in dataframe.iterrows():
        roi = (row['20 Year Net ROI'][1:].replace(',',''))
        cost = (row['Total 4 Year Cost'][1:].replace(',',''))
        loan = (row['Average Loan Amount'][1:].replace(',',''))
        try:
            roi = int(roi)
        except:
            roi = 0
        try:
            cost = int(cost)
        except:
            cost = 0
        try:
            graduate = int(row['Typical Years to Graduate'])
        except:
            graduate = 0
        try:
            loan = int(loan)
        except:
            loan = 0
        newR.append((roi, cost, graduate, loan))
    newR = pd.DataFrame(newR)
    print(newR.mean())
    
# Funciton adapted from https://stackoverflow.com/questions/39742305/how-to-use-basemap-python-to-plot-us-with-50-states
# Draw the data based on the input, with regards to state and value
def draw_map(inputValue, title):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap as Basemap
    from matplotlib.colors import rgb2hex
    from matplotlib.patches import Polygon
    from matplotlib.colors import Normalize
    
    from matplotlib.colorbar import ColorbarBase
    # Lambert Conformal map of lower 48 states.
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    shp_info = m.readshapefile('st99_d00','states',drawbounds=True)
    # choose a color for each state based on population density.
    colors={}
    statenames=[]
    cmap = plt.cm.hot # use 'hot' colormap
    vmin = min(inputValue.values()); vmax = max(inputValue.values()) # set range.
    for shapedict in m.states_info:
        statename = shapedict['NAME']
        # skip DC and Puerto Rico.
        if statename not in ['District of Columbia','Puerto Rico']:
            curValue = inputValue[statename]
            # calling colormap with value between 0 and 1 returns
            # rgba value.  Invert color range (hot colors are high
            # population), take sqrt root to spread out colors more.
            colors[statename] = cmap(1-np.sqrt((curValue-vmin)/(vmax-vmin)))[:4]
        statenames.append(statename)
    # cycle through state names, color each one.
    ax = plt.gca() # get current axes instance
    for nshape,seg in enumerate(m.states):
        # skip DC and Puerto Rico.
        if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
            color = rgb2hex(colors[statenames[nshape]]) 
            poly = Polygon(seg,facecolor=color,edgecolor=color)
            ax.add_patch(poly)
    plt.title(title)
    
    norm = Normalize(vmin=min(inputValue.values()), vmax=max(inputValue.values()))
    cax = plt.gcf().add_axes([0.27, 0.1, 0.5, 0.05]) # posititon
    cb = ColorbarBase(cax,cmap=cmap.reversed(),norm=norm, orientation='horizontal')
    plt.show()
    
def compute_stats_and_draw_map(dataframe):
    average = dict()
    for value in abbrev_to_us_state.values():
        average[value] = (0,0)
    
    for i, row in dataframe.iterrows():
        roi = (row['20 Year Net ROI'][1:].replace(',',''))
        cost = (row['Total 4 Year Cost'][1:].replace(',',''))
        loan = (row['Average Loan Amount'][1:].replace(',',''))
        try:
            roi = int(roi)
        except:
            roi = 0
            
        try:
            state = abbrev_to_us_state[(row['State'])]
            (allVal, count) = average[state]
            average[state] = (allVal + roi, count + 1)
        except:
            pass
    print("Passed")
    print(average)
    for key in average.keys():
        a, b = average[key]
        try:
            average[key] = a/b
        except:
            average[key] = 0
    print(average)
    draw_map(average, "Average ROI By States ($)")