#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


countries = []
selected_countries = ["Israel", "Netherlands"]
dates = []
infected = []

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


def download_data(source):
    """Download details"""
    return pd.read_csv(source)


# download data
df = download_data(url)


# creating dates list
columns = list(df)
for column in columns[4:]:  # first four columns aren't dates
    dates.append(column)

# creating countries numbers list
for row in df.iterrows():
    countries.append(row[1][1])
countries = list(set(countries))

# create infected matrix
infected = np.zeros((len(selected_countries), len(dates)), dtype=int)
""" for i in range(len(selected_countries)):
    infected.append([])
    for j in range(len(dates)):
        infected[i].append([])
        infected[i][j] = 0 """

# sum infected numbers(source contains duplicates)
for i in range(len(selected_countries)):
    for row in df.iterrows():
        if selected_countries[i] == row[1][1]:
            for date in range(len(dates)):
                infected[i][date] += row[1][4+date]

# plot
for i in range(len(selected_countries)):
    plt.plot(infected[i])
plt.xlabel("Time")
plt.ylabel("Cases")
plt.title("Covid-19")
plt.legend(selected_countries)
plt.show()
