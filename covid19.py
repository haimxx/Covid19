#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates

countries = []
selected_countries = ["Israel", "Netherlands"]
dates = []
infected = []
date_interval = 5

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


def download_data(source):
    """Download details"""
    try:
        return pd.read_csv(source)
    except OSError:
        print("Error in downloading data!\nExiting...")
        exit()


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
fig, ax = plt.subplots()
x = [dt.datetime.strptime(d, '%m/%d/%y').date() for d in dates]

ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=date_interval))


for i in range(len(selected_countries)):
    plt.plot(x, infected[i])

plt.xlabel("Date")
plt.ylabel("Cases")
plt.title("Covid-19")
plt.legend(selected_countries)

fig.autofmt_xdate()

plt.show()
