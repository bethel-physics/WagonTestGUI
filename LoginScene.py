# importing necessary modules
import tkinter as tk
from tkinter import ttk

# creating the login frame
class LoginScene(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window)
        
        # Remove All Packed Frame, Unnecessary
        # Creating frame for packed items to use grid
        frm_packed = tk.Frame(self)
        frm_packed.grid(column=0, row=0)

        # Creating a list of users for dropdown menu
        # Eventually need to add a way for a database to have control over this array
        User_List = [
            "Bob Johnson",
            "Spencer Higgins",
            "Amanda Holmes"
        ]

        # Creating the title for the window
        lbl_title = tk.Label(frm_packed, text="Please Select Your Name", font=('Times', '20'))
        lbl_title.pack(pady=25)

        # Creating intial value in dropdown menu
        user_selected = tk.StringVar(frm_packed)
        user_selected.set("") # default value is empty

        # Creating the dropdown menu itself
        opt_user_dropdown = tk.OptionMenu(frm_packed, user_selected, *User_List)
        opt_user_dropdown.pack(pady=10)
        opt_user_dropdown.config(width = 20)

        # Creating the submit button
        # Need to add shift frame functionality later
        btn_submit = tk.Button(frm_packed, text="Submit", relief=tk.RAISED)
        btn_submit.pack()

        # # Creating logout button in grid
        # btn_logout = tk.Button(self, text = "Logout")
        # btn_logout.grid(column=1, row=1, sticky='se')