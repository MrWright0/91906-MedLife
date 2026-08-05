import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Input Validation Example")
root.geometry("400x300")

# Validation Functions
def validate_number(input_value):
    if input_value.isdigit() and len(input_value) <= 5:
        return
    elif input_value == "":
        messagebox.showwarning("Warning", "Entry box is empty or invalid!")
    else:
        messagebox.showerror("Invalid Input", "Please enter a number with a maximum of 5 digits.")
    number_var.set("")

def validate_alphabet(input_value):
    if input_value.isalpha() and len(input_value) <= 10:
        return
    elif input_value == "":
        messagebox.showwarning("Warning", "Entry box is empty or invalid!")
    else:
        messagebox.showerror("Invalid Input", "Please enter alphabets with a maximum of 10 characters.")
    alphabet_var.set("")

def validate_float(input_value):
    try:
        float_value = float(input_value)
        if len(input_value) <= 7:
            return
        elif input_value == "":
            messagebox.showwarning("Warning", "Entry box is empty or invalid!")
        else:
            messagebox.showerror("Invalid Input", "Please enter a float with a maximum of 7 characters.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid float.")
    float_var.set("")

# Number Entry Field
number_var = tk.StringVar()
number_var.trace("w", lambda name, index, mode: validate_number(number_var.get()))

number_label = tk.Label(root, text="Enter a number (max 5 digits):")
number_label.pack()
number_entry = tk.Entry(root, textvariable=number_var)
number_entry.pack()

# Alphabet Entry Field
alphabet_var = tk.StringVar()
alphabet_var.trace("w", lambda name, index, mode: validate_alphabet(alphabet_var.get()))

alphabet_label = tk.Label(root, text="Enter alphabets (max 10 characters):")
alphabet_label.pack()
alphabet_entry = tk.Entry(root, textvariable=alphabet_var)
alphabet_entry.pack()

# Float Entry Field
float_var = tk.StringVar()
float_var.trace("w", lambda name, index, mode: validate_float(float_var.get()))

float_label = tk.Label(root, text="Enter a float (max 7 characters):")
float_label.pack()
float_entry = tk.Entry(root, textvariable=float_var)
float_entry.pack()

# Submit Button
def submit():
    number = number_var.get()
    alphabet = alphabet_var.get()
    float_value = float_var.get()
    messagebox.showinfo("Submitted Values", f"Number: {number}\nAlphabets: {alphabet}\nFloat: {float_value}")

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
