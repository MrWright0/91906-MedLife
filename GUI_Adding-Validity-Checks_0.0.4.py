'''
Date: 24 June 26
Author: Your Name
Purpose: Saving files to a folder using python using tkinter

'''

# ------------------------- Libraries
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# ------------------------- Functions

def save_file():
    #Save the current file as a new file.
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def open_file():
    #Open a file for editing.
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

# -------------------------- Window
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Add a third row to the window grid for the validation panel
window.rowconfigure(1, minsize=60, weight=0)

# -------------------------- Widgets

txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Create the bottom frame that holds the entry fields
frm_validation = tk.Frame(window, relief=tk.GROOVE, bd=2, padx=10, pady=10)
frm_validation.grid(row=1, column=0, columnspan=2, sticky="ew")


window.mainloop()

