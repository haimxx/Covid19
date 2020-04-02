#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from covid19 import *


def button_func():
    selected_countries = [lb.get(idx) for idx in lb.curselection()]
    infected = infected_calc(selected_countries, dates, df)
    plot(selected_countries, infected, dates)


def download_error():
    tk.messagebox.showerror("Error", "Could not download data\nExiting")


root = tk.Tk()
root.title("Covid19")
# root.geometry("800x800")
# root.iconbitmap("CV.ico")

""" date = "1/3/20"
    status = tk.Label(
    root, text=f"Data is updated to {date}", bd=1, relief=tk.SUNKEN, anchor=tk.W)
label = tk.Label(root, text="Covid19")
label.grid()
status.grid(sticky=tk.W+tk.E) """

df = download_data(infected_url)
if df.empty:
    download_error()
    exit(1)
dates = dates_create(df)
countries = countries_infected_details(df)


# list
countries_frame = tk.LabelFrame(text="Infected Countries", padx=5, pady=5)
lb = tk.Listbox(countries_frame, height=40, selectmode=tk.MULTIPLE)
for country in sorted(countries):
    lb.insert(tk.END, country)
lb.pack()
countries_frame.grid(row=0, column=1, padx=10, pady=10)

# scrollbar
yscroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=lb.yview)
lb.config(yscrollcommand=yscroll.set)
yscroll.grid(row=0, column=0, sticky=tk.W+tk.N+tk.S)

# plot button
button = tk.Button(root, text="Plot", command=button_func)
button.grid(row=1, column=1)

# sum datails
sum_frame = tk.LabelFrame(root, text="Totals", padx=5, pady=5)
tk.Label(sum_frame, text=f"Countries {len(countries)}", bg="violet").grid(
    row=0, column=0)
tk.Label(sum_frame, text=f"Infected {total_calc(df)}", bg="red").grid(
    row=1, column=0)
tk.Label(sum_frame, text="Recovered").grid(row=2, column=0)
tk.Label(sum_frame, text="Dead").grid(row=3, column=0)

country_sum = tk.Listbox(sum_frame)

countries.sort()
infected_all_countries = infected_calc(countries, dates, df)

for country in range(len(countries)):
    country_sum.insert(tk.END, infected_all_countries[country][len(dates)-1])
country_sum.grid(row=4, column=0)
sum_frame.grid(row=0, column=3)

root.mainloop()
