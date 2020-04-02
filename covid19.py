#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates

countries = []
infected = []
date_interval = 7
df = pd.DataFrame()

# Source datails
infected_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
dead_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


def download_data(source):
    """Download details"""
    try:
        return pd.read_csv(source)
    except OSError:
        return pd.DataFrame()


def dates_create(df):
    """Creating dates list"""
    dates_list = []
    columns = list(df)

    for column in columns[4:]:  # first four columns aren't dates
        dates_list.append(column)
    return dates_list


def countries_infected_details(df):
    """Creating infected people numbers list"""
    countries = []

    for row in df.iterrows():
        countries.append(row[1][1])
    countries = list(set(countries))
    return countries


def empty_matrix_create(row, columns):  # currently not in use
    """Creating matrix (row X columns) with zeroes inside each cell"""
    matrix = []

    for i in range(row):
        matrix.append([])
        for j in range(columns):
            matrix[i].append([])
            matrix[i][j] = 0
    return matrix


def infected_calc(selected_countries, dates, df):
    """Calculating infected numbers"""
    # create infected matrix
    infected = np.zeros((len(selected_countries), len(dates)), dtype=int)

    # sum infected numbers(source contains duplicates)
    for i in range(len(selected_countries)):
        for row in df.iterrows():
            if selected_countries[i] == row[1][1]:
                for date in range(len(dates)):
                    infected[i][date] += row[1][4+date]
    return infected


def total_calc(df):
    """Calculating total pepole numbers"""

    total = 0
    for row in df.iterrows():
        total += row[1][len(df.columns)-1]
    return total


def plot(selected_countries, figures, dates):
    """Plot the selected countries details"""
    fig, ax = plt.subplots()
    x = [dt.datetime.strptime(d, '%m/%d/%y').date() for d in dates]

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=date_interval))

    for i in range(len(selected_countries)):
        plt.plot(x, figures[i])

    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.title("Covid-19")
    plt.legend(selected_countries)

    fig.autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    # download data
    df = download_data(infected_url)
    if df.empty:
        print("Error while downloading data\nExiting...")
        exit(1)

    # generate dates list
    dates = dates_create(df)

    # creating countries infected numbers list
    countries = countries_infected_details(df)

    # plot
    selected_countries = ["Israel", "Netherlands"]
    infected = infected_calc(selected_countries, dates, df)
    plot(selected_countries, infected, dates)
