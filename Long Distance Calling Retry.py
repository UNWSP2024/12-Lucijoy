# Author: Lucia Floan
# Date: 04-25-2025
# Name: Long-Distance Calls.py

import tkinter as tk
def calc_charge():
    mins = float(minutes_entry.get())
    if rate.get() == 1:
        cost = mins * 0.02
    elif rate.get() == 2:
        cost = mins * 0.12
    else:
        cost = mins * 0.05
    charge_label.config(text="Charge: $" + str(round(cost, 2)))
root = tk.Tk()
root.title("Long-Distance Charges")

tk.Label(root, text="Minutes:").pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

rate = tk.IntVar()
tk.Radiobutton(root, text="Daytime ($0.02)", variable=rate, value=1).pack()
tk.Radiobutton(root, text="Evening ($0.12)", variable=rate, value=2).pack()
tk.Radiobutton(root, text="Off-Peak ($0.05)", variable=rate, value=3).pack()

tk.Button(root, text="Calculate the Charge", command=calc_charge).pack()
charge_label = tk.Label(root, text="")
charge_label.pack()

root.mainloop()