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


df = download_data(url)
if df.empty:
    download_error()
    exit(1)
dates = dates_create(df)
countries = countries_infected_details(df)


# list
lb = tk.Listbox(root, height=40, selectmode=tk.MULTIPLE)
for country in sorted(countries):
    lb.insert(tk.END, country)
lb.grid(row=0, column=1)

yscroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=lb.yview)
lb.config(yscrollcommand=yscroll.set)
yscroll.grid(row=0, column=0, sticky=tk.W+tk.N+tk.S)

button = tk.Button(root, text="Plot", command=button_func)
button.grid(row=1, column=1)


root.mainloop()
