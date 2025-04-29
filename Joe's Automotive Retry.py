# Author: Lucia Floan
# Date: 04-25-2025
# Name: Joe's Automotive

import tkinter as tk

def calc_total():
    total = 0
    if oil_change.get() == 1:
        total += 30
    if lube_job.get() == 1:
        total += 20
    if radiator_flush.get() == 1:
        total += 40
    if trans_fluid.get() == 1:
        total += 100
    if inspection.get() == 1:
        total += 35
    if muffler.get() == 1:
        total += 200
    if tire_rotaet.get() == 1:
        total += 20
    total_label.config(text="Total: $" + str(total))

# Main window
root = tk.Tk()
root.title("Joe's Automotive")

# Service options
oil_change = tk.IntVar()
lube_job = tk.IntVar()
radiator_flush = tk.IntVar()
trans_fluid = tk.IntVar()
inspection = tk.IntVar()
muffler = tk.IntVar()
tire_rotaet = tk.IntVar()

tk.Checkbutton(root, text="Oil Change - $30", variable=oil_change).pack()
tk.Checkbutton(root, text="Lube Job - $20", variable=lube_job).pack()
tk.Checkbutton(root, text="Radiator Flush - $40", variable=radiator_flush).pack()
tk.Checkbutton(root, text="Transmission Fluid - $100", variable=trans_fluid).pack()
tk.Checkbutton(root, text="Inspection - $35", variable=inspection).pack()
tk.Checkbutton(root, text="Muffler Replacement - $200", variable=muffler).pack()
tk.Checkbutton(root, text="Tire Rotation - $20", variable=tire_rotaet).pack()

# Button to calculate and label for result
tk.Button(root, text="Calculate Total", command=calc_total).pack()
total_label = tk.Label(root, text="")
total_label.pack()

root.mainloop()