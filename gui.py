#!/usr/bin/env python3

import tkinter as tk
from covid19 import *


def button_func():
    selected_countries = [lb.get(idx) for idx in lb.curselection()]
    infected = infected_calc(selected_countries, dates)
    plot(selected_countries, infected)


root = tk.Tk()
root.title("Covid19")


# list
lb = tk.Listbox(root, height=40, selectmode=tk.MULTIPLE)
for country in sorted(countries):
    lb.insert(tk.END, country)
lb.pack()

button = tk.Button(root, text="Plot", command=button_func)
button.pack()


root.mainloop()
