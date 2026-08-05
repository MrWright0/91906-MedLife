'''
Date: 18/06/2026
Author: Mr Wright
Purpose: Create a window using a GUI Library tkinter
'''

# Retrieve the library
import tkinter as tk
from tkinter import ttk

# --------------------------FUNCTIONS

# SECOND WINDOW
def open_second_win():
    second_win = tk.Tk()

# ---------------------------FIRST WINDOW

root = tk.Tk()

# ----------------------------- STYLING

root.geometry("800x600")
root.title("My First Window")
root.configure(bg = "indian red")

# -------------------------- WIDGETS

first_button = ttk.Button(root, command=open_second_win)
first_button.pack()

#--------------------MAIN LOOP

root.mainloop()
