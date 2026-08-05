'''
Date: 22/06/26
Author: Mr Wright
Purpose: Create a Frame Using GUI
'''

# Retrieve the library
import tkinter as tk
from tkinter import ttk

# --------------------------FUNCTIONS

# SECOND WINDOW
def open_second_win():
    second_win = tk.Tk()
    second_win.configure(bg= "blue")
    
# ---------------------------FIRST WINDOW

root = tk.Tk()

# ----------------------------- STYLING

root.geometry("800x600")
root.title("My First Window")
root.configure(bg = "indian red")

# ---------------------------Image

image = tk.PhotoImage(file="forest.png")
# -------------------------- WIDGETS

first_button = ttk.Button(root, command=open_second_win)
first_button.pack()

main_frame = tk.Frame(root, width = 400, height = 300, bg= "black")
main_frame.pack(padx = 50, pady = 50)
tk.Label (main_frame, text ="Original Image").pack(padx = 5, pady = 5)
thumbnail_image = image.subsample (5, 5)

image_frame=tk.Frame(root, width = 400, height = 400, bg = "grey")
display_image=image.subsample (2,2)
image_frame.pack()
tk.Label(image_frame, image=display_image).pack




#--------------------MAIN LOOP

root.mainloop()
