# Author: Lucia Floan
# Date: 04-25-2025
# Name: MPG Calculator

import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        messagebox.showinfo("Result", f"MPG: {mpg:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter actual numbers.")

window = tk.Tk()
window.title("MPG Calculator")

tk.Label(window, text="Gallons:").grid(row=0, column=0)
gallons_entry = tk.Entry(window)
gallons_entry.grid(row=0, column=1)

tk.Label(window, text="Miles:").grid(row=1, column=0)
miles_entry = tk.Entry(window)
miles_entry.grid(row=1, column=1)

tk.Button(window, text="Calculate MPG", command=calculate_mpg).grid(row=2, columnspan=2)

window.mainloop()