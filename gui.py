#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from covid19 import *


def button_func():
    selected_countries = [lb.get(idx) for idx in lb.curselection()]
    infected = infected_calc(selected_countries, dates, df)
    plot(selected_countries, infected, dates)


def download_error():
    tk.messagebox.showerror("Error", "Could not download data\nExiting")


def flash_screen():
    root = tk.Tk()
    root.title("Covid19")


root = tk.Tk()
root.title("Covid19")
# root.geometry("800x800")
# root.iconbitmap("CV.ico")


about_text = """
Developed by haimxx.
github.com/haimxx"""


def show_about():
    tk.messagebox.showinfo("About Covid19", about_text)


help_text = """This app shows details about the Coronavirus spread around the world.
It plots the numbers of the selected infected countries.

Please select the desired countries from the list and hit \"Plot\".\n\n
Data is being updated once a day(source: JHU CSSE)"""


def show_help():
    tk.messagebox.showinfo("Help", help_text)


# menu
menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=show_help)
helpmenu.add_command(label="About", command=show_about)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Menu", menu=helpmenu)


df = download_data(infected_url)
if df.empty:
    download_error()
    exit(1)
dates = dates_create(df)
countries = countries_infected_details(df)

# radio buttons infected details type
r_infected = tk.IntVar()

radio_frame_infected = tk.LabelFrame(padx=5, pady=5)
rad1 = tk.Radiobutton(radio_frame_infected,
                      text="Confirmed", variable=r_infected, value=1)
rad1.grid(row=0, column=0)
rad2 = tk.Radiobutton(radio_frame_infected, text="Recovered",
                      variable=r_infected, value=2, state="disabled")
rad2.grid(row=0, column=1)
rad3 = tk.Radiobutton(radio_frame_infected, text="Dead", variable=r_infected,
                      value=3, state="disabled")
rad3.grid(row=0, column=2)
radio_frame_infected.grid(row=0, column=0, columnspan=2)

rad1.select()


# radio buttons total/daily
r_details = tk.IntVar()

radio_frame_details = tk.LabelFrame(padx=5, pady=5)
rad1 = tk.Radiobutton(radio_frame_details, text="Total",
                      variable=r_details, value=1)
rad1.grid(row=0, column=0)
rad2 = tk.Radiobutton(radio_frame_details, text="Daily",
                      variable=r_details, value=2, state="disabled")
rad2.grid(row=0, column=1)
radio_frame_details.grid(row=1, column=0, columnspan=2)

rad1.select()

# list
countries_frame = tk.LabelFrame(
    root, text="Infected Countries", padx=5, pady=5)
lb = tk.Listbox(countries_frame, height=30, selectmode=tk.MULTIPLE)
for country in sorted(countries):
    lb.insert(tk.END, country)
lb.pack()
countries_frame.grid(row=2, column=1, padx=5, pady=10, sticky=tk.NW)

# scrollbar
yscroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=lb.yview)
lb.config(yscrollcommand=yscroll.set)
yscroll.grid(row=2, column=0, sticky=tk.W+tk.N+tk.S)

# plot button
button = tk.Button(root, text="Plot", command=button_func)
button.grid(row=3, column=1)

# sum datails
sum_frame = tk.LabelFrame(root, text="Totals", padx=5, pady=5)
tk.Label(sum_frame, text=f"Countries {len(countries)}", bg="violet").grid(
    row=0, column=0)
tk.Label(sum_frame, text=f"Infected {total_calc(df)}", bg="red").grid(
    row=1, column=0)
tk.Label(sum_frame, text="Recovered").grid(row=2, column=0)
tk.Label(sum_frame, text="Dead").grid(row=3, column=0)

"""
country_sum = tk.Listbox(sum_frame)

countries.sort()
infected_all_countries = infected_calc(countries, dates, df)

for country in range(len(countries)):
    country_sum.insert(tk.END, infected_all_countries[country][len(dates)-1])
country_sum.grid(row=4, column=0)
"""
sum_frame.grid(row=0, column=3, rowspan=3, sticky=tk.NW)

root.config(menu=menubar)
root.mainloop()
