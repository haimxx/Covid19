#!/usr/bin/env python3


import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []
countries = []

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


data = pd.read_csv(url)
