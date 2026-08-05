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

# ---------------------- Validation Functions

def is_alpha(proposed_value):
    if proposed_value =="": return True
    for char in proposed_value:
        if not (char.isalpha() or char == " "): return False
    return True

def is_integer(proposed_value):
    if proposed_value in ("", "-"): return True
    try:
        int(proposed_value); return True
    except ValueError:
        return False
# ------------------------ Invalid-input Callbacks

def on_invalid_alpha():
    lbl_error.config(text='X Author name: Please only use letters and spaces.')
    window.after(2000, lambda: lbl_error.config(text=''))

def on_invalid_int():
    lbl_error.config(text='X Page number: Please only use whole numbers (e.g. 42).')
    window.after(2000, lambda: lbl_error.config(text=''))
    

# def my_check(proposed_value):# Return True to accept, False to reject
#    return some_condition(proposed_value)


# -------------------------- Window
window = tk.Tk()
# ------------- Register with Tkinter — required before use
window.title("Simple Text Editor")
window.geometry ("800x300")
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=400, weight=1)
# Add a third row to the window grid for the validation panel
window.rowconfigure(1, minsize=60, weight=0)

vcmd_alpha = window.register (is_alpha)
ivcmd_alpha = window.register(on_invalid_alpha)
vcmd_int = window.register (is_integer)
ivcmd_int = window.register(on_invalid_int)

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
lbl_name = tk.Label(frm_validation, text="Author name (letters only):", fg = "pink", bg = "black" )
lbl_name.grid(row=1, column=0, padx=(0,2))
lbl_page = tk.Label(frm_validation, text="Go to page (integers only):", fg = "pink", bg = "black"  )
lbl_page.grid(row=1, column=1, padx=(0,2))
# ------------------ Label error code
lbl_error = tk.Label(frm_validation, text='', fg='red')
lbl_error.grid(row=1, column=0, columnspan=4, sticky='w', pady=(4,0))

# --- Entry widgets (no validation yet — we'll add it next) ---
ent_name = tk.Entry(frm_validation, width=30, validate = "key", validatecommand=(vcmd_alpha, "%p"),
                    invalidcommand=ivcmd_alpha)
ent_name.grid(row=0, column=0, padx=(0,20))

ent_page = tk.Entry(frm_validation, width=10, validate = "key", validatecommand=(vcmd_int, "%P"),
                    invalidcommand=ivcmd_int)
ent_page.grid(row=0, column=3)

window.mainloop()

